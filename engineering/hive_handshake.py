import os
import time
import random
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

# CONSTANTS for the 5-Cell Hive
USER_DATA_DIR = os.path.expanduser("~/jules_pipeline/google_session")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def initialize_stealth_session(account_index=1):
    """
    Launches a persistent session for one of the 5 family accounts.
    First run: Set headless=False to log in manually.
    """
    with sync_playwright() as p:
        context_path = f"{USER_DATA_DIR}_cell_{account_index}"
        browser = p.chromium.launch_persistent_context(
            user_data_dir=context_path,
            headless=False,  # Keep False for manual login verification
            user_agent=USER_AGENT,
            viewport={'width': 1920, 'height': 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser.new_page()
        stealth_sync(page)

        # Navigate to NotebookLM
        print(f"[*] Navigating to Cell {account_index} Hive...")
        page.goto("https://notebooklm.google.com/")

        # Wait for user to verify login or for automated seeding to begin
        print("[!] Perform manual login if prompted. Script will hold for 60s...")
        time.sleep(60)

        # Proceed to ingestion if logged in
        # ingest_shards(page, "/path/to/batch/folder")

        browser.close()

def ingest_shards(page, batch_folder):
    """
    Handles the actual UI interaction for NotebookLM ingestion.
    Assumes 300 .md shards exist in the batch_folder.
    """
    # 1. Create the Notebook
    page.get_by_role("button", name="New Notebook").click()
    page.wait_for_timeout(random.randint(2000, 5000))  # Human-like delay

    # 2. Grab the file paths for this specific batch
    # Tip: Use Markdown tables for structured data triage
    shards = [os.path.abspath(os.path.join(batch_folder, f))
              for f in os.listdir(batch_folder) if f.endswith('.md')]

    if not shards:
        print("[!] No .md shards found in batch folder.")
        return

    # 3. Trigger the file upload (handling the hidden input)
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Upload from computer").click()

    file_chooser = fc_info.value
    file_chooser.set_files(shards[:300])  # Limit to 300 per NotebookLM rules

    print(f"[*] Seeding {min(len(shards), 300)} shards into the Hive. Processing...")

    # Wait for the upload to complete
    try:
        page.wait_for_selector("text='Sources added'", timeout=120000)
        print("[+] Seeding complete.")
    except Exception as e:
        print(f"[-] Timeout or error during seeding: {e}")

if __name__ == "__main__":
    # Execute for Cell 1 (Repeat for 2-5)
    initialize_stealth_session(1)
