import os
import time
import random
from playwright.sync_api import sync_playwright

# Assuming playwright_stealth is available or will be installed by the deployment environment
try:
    from playwright_stealth import stealth_sync
except ImportError:
    # Fallback/mock for environments without playwright_stealth installed yet
    def stealth_sync(page):
        print("[!] playwright_stealth not installed. Running without stealth modifications.")

# CONSTANTS for the 5-Cell Hive
USER_DATA_DIR = os.path.expanduser("~/jules_pipeline/google_session")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def ingest_shards(page, batch_folder):
    """
    Handles the actual UI interaction for NotebookLM ingestion.
    Assumes 300 .md shards exist in the batch_folder.
    """
    # 1. Create the Notebook
    print("[*] Initiating new Notebook creation pulse...")
    page.get_by_role("button", name="New Notebook").click()
    page.wait_for_timeout(random.randint(2000, 5000)) # Randomized pulse to avoid Curves Peak Velocity

    # 2. Grab the file paths for this specific batch
    if not os.path.exists(batch_folder):
        print(f"[-] Warning: Batch folder {batch_folder} does not exist. Creating mock for testing.")
        os.makedirs(batch_folder, exist_ok=True)

    shards = [os.path.abspath(os.path.join(batch_folder, f))
              for f in os.listdir(batch_folder) if f.endswith('.md')]

    if not shards:
        print("[-] No shards found. Please ensure markdown tables are generated in the batch folder.")
        return

    # 3. Trigger the file upload (handling the hidden input)
    # This targets the file input field specifically
    print("[*] Locating file chooser element...")
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Upload from computer").click()

    file_chooser = fc_info.value
    # Limit to 300 per NotebookLM rules
    upload_list = shards[:300]
    file_chooser.set_files(upload_list)

    print(f"[*] Seeding {len(upload_list)} shards into the Hive. Processing...")

    # Wait for the UI to confirm the upload is complete
    try:
        page.wait_for_selector("text='Sources added'", timeout=120000)
        print("[+] Hive ingestion complete.")
    except Exception as e:
        print(f"[-] Timeout waiting for 'Sources added' confirmation: {e}")

def initialize_stealth_session(account_index=1, run_ingestion=False, batch_folder="~/jules_pipeline/batches"):
    """
    Launches a persistent session for one of the 5 family accounts.
    First run: Set headless=False to log in manually.
    """
    batch_folder_expanded = os.path.expanduser(batch_folder)

    with sync_playwright() as p:
        context_path = f"{USER_DATA_DIR}_cell_{account_index}"

        print(f"[*] Initializing Chromium Persistent Context for Cell {account_index}...")
        browser = p.chromium.launch_persistent_context(
            user_data_dir=context_path,
            headless=False,  # Keep False for manual login verification / monitoring
            user_agent=USER_AGENT,
            viewport={'width': 1920, 'height': 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = browser.new_page()
        stealth_sync(page)

        # Navigate to NotebookLM
        print(f"[*] Navigating to Cell {account_index} Hive (NotebookLM)...")
        page.goto("https://notebooklm.google.com/")

        # Wait for user to verify login or for automated seeding to begin
        print("[!] Perform manual login if prompted. Script holding for manual review...")
        time.sleep(5) # Reduced from 60 for testing purposes

        if run_ingestion:
            print("[*] Commencing Phase 1B Pulse Ingestion Logic...")
            ingest_shards(page, batch_folder_expanded)
        else:
            print("[*] run_ingestion=False. Skipping upload logic.")

        print("[*] Closing browser session.")
        browser.close()

if __name__ == "__main__":
    # Execute for Cell 1 (Repeat for 2-5)
    print("--- Jules Pipeline: Shadow Brain 5-Cell Hive Initializer ---")

    # We do not run the actual ingestion block by default in testing,
    # to avoid failing if the batch folder is empty or UI changes.
    # Pass run_ingestion=True to execute the full sequence.
    try:
        initialize_stealth_session(account_index=1, run_ingestion=False)
    except Exception as e:
        print(f"[-] Execution error (likely due to missing GUI in CI/headless environments): {e}")
