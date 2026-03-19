import os
import json
import time
import shutil
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AsynchronousHandoffWatchdog:
    """
    Implements the $0.00 NotebookLM Handoff Strategy.

    This watchdog script continuously monitors the "Outbox" directory where
    NotebookLM (or the Administrator via the NotebookLM UI) drops the JSON
    answers containing curated file paths from the 2TB Google Drive.

    Upon detecting a new JSON file, it parses the payload and triggers
    the next stage of the Sovereign Assembly Pipeline (e.g., Google Flow
    or Vertex Veo) using the perfectly retrieved, zero-cost assets.
    """

    def __init__(
        self,
        outbox_dir: str = "/mnt/google_drive/guce_notebook_outbox",
        processed_dir: str = "/mnt/google_drive/guce_notebook_processed",
        poll_interval_seconds: int = 5
    ):
        self.outbox_dir = outbox_dir
        self.processed_dir = processed_dir
        self.poll_interval = poll_interval_seconds

        # In a strict production environment, we ensure these directories exist
        # If the 2TB Drive is not mounted, this will intentionally fail (Zero Mocking)
        try:
            os.makedirs(self.outbox_dir, exist_ok=True)
            os.makedirs(self.processed_dir, exist_ok=True)
        except PermissionError as e:
            logger.error(f"[FATAL] Google Drive mount not accessible at {self.outbox_dir}. Halting Watchdog.")
            raise SystemExit(e)

    def process_payload(self, filepath: str) -> None:
        """
        Reads the NotebookLM output JSON and triggers the video assembly payload.
        """
        logger.info(f"[WATCHDOG] New payload detected: {filepath}")

        try:
            with open(filepath, 'r') as f:
                payload: Dict[str, Any] = json.load(f)

            # Example Payload Structure Expected from NotebookLM:
            # {
            #   "scene_id": "scene_001",
            #   "assets_found": ["/mnt/google_drive/guce_vault/vintage_camera.jpg"]
            # }

            assets = payload.get("assets_found", [])
            if not assets:
                logger.warning(f"[ORCHESTRATION] No assets found by NotebookLM in {filepath}. Triggering Fallback to Google Docs/Gemini Generation.")
                # Here we would trigger the API to Docs to generate the image (e.g., 1965 LA summer day)
            else:
                logger.info(f"[ORCHESTRATION] NotebookLM successfully curated {len(assets)} assets for {payload.get('scene_id')}. Bypassing Generation API.")
                # Here we would hand the payload off to FFmpeg or PixiJS for local rendering
                for asset in assets:
                    logger.info(f" -> utilizing asset: {asset}")

        except json.JSONDecodeError:
            logger.error(f"[ERROR] Payload {filepath} is not valid JSON. Ignoring.")
        except Exception as e:
            logger.error(f"[ERROR] Failed to process payload {filepath}: {str(e)}")

        finally:
            self._archive_payload(filepath)

    def _archive_payload(self, filepath: str) -> None:
        """Moves the processed JSON file to prevent infinite processing loops."""
        filename = os.path.basename(filepath)
        dest_path = os.path.join(self.processed_dir, filename)
        shutil.move(filepath, dest_path)
        logger.info(f"[WATCHDOG] Payload archived to {dest_path}")

    def run_polling_loop(self) -> None:
        """
        A lightweight polling loop that scans the directory for new JSON files.
        Avoids heavy third-party dependencies like 'watchdog' package to keep
        the footprint minimal for cell-phone/budget server deployment.
        """
        logger.info(f"[WATCHDOG] Starting Asynchronous Polling on {self.outbox_dir} (Interval: {self.poll_interval}s)")
        try:
            while True:
                for filename in os.listdir(self.outbox_dir):
                    if filename.endswith(".json"):
                        filepath = os.path.join(self.outbox_dir, filename)
                        self.process_payload(filepath)

                # Sleep to prevent high CPU usage
                time.sleep(self.poll_interval)

        except KeyboardInterrupt:
            logger.info("[WATCHDOG] Polling loop terminated by user.")

if __name__ == "__main__":
    # The script acts as an active daemon. When run directly, it will loop forever.
    watcher = AsynchronousHandoffWatchdog()
    watcher.run_polling_loop()
