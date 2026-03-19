import os

class AntigravityWorkspace:
    """
    Native Google Antigravity Agentic IDE Environment.
    Provisions the GUCE Terraform blueprint for a brand new project.
    Configures the Cloud Scheduler heartbeat to trigger Cloud Run via OIDC,
    authenticates with Vertex AI Model Garden for generation, and outputs
    metadata directly to the Sheets Narration Library.
    """
    def __init__(self, project_id="guce-nextgen-prod-001", region="us-west2"):
        self.project_id = project_id
        self.region = region
        self.workspace_dir = "infrastructure/terraform"

        # Initialize the local Antigravity workspace directory
        os.makedirs(self.workspace_dir, exist_ok=True)

    def build_infrastructure_manifest(self):
        """
        Generates the Terraform manifest to deploy the automated,
        serverless production pipeline from the ground up.
        """
        terraform_hcl = f"""
# --- GUCE Native Architecture: Antigravity to Cloud Run ---
variable "project_id" {{
  description = "The GCP project ID"
  type        = string
  default     = "{self.project_id}"
}}

variable "region" {{
  description = "The GCP region"
  type        = string
  default     = "{self.region}"
}}

provider "google" {{
  project = var.project_id
  region  = var.region
}}

# 1. Enable Core Google Universe APIs
resource "google_project_service" "guce_apis" {{
  for_each = toset([
    "run.googleapis.com",             # Compute Layer (Hosts the Engine)
    "cloudscheduler.googleapis.com",  # Automation Heartbeat
    "aiplatform.googleapis.com",      # Vertex AI Studio & Model Garden
    "sheets.googleapis.com",          # Narration Library (Epistemic Ledger)
    "iam.googleapis.com"              # Security & Identity Federation
  ])
  service            = each.key
  disable_on_destroy = false
}}

# 2. Service Account for Cloud Run (Guardian Wrapper)
resource "google_service_account" "guardian_sa" {{
  account_id   = "guce-guardian-native"
  display_name = "GUCE Native Guardian Service Account"
  depends_on   = [google_project_service.guce_apis]
}}

# 3. Grant Vertex AI & Sheets Access to Guardian
resource "google_project_iam_member" "guardian_vertex_access" {{
  project = var.project_id
  role    = "roles/aiplatform.user"
  member  = "serviceAccount:${{google_service_account.guardian_sa.email}}"
}}

resource "google_project_iam_member" "guardian_sheets_access" {{
  project = var.project_id
  role    = "roles/sheets.editor"
  member  = "serviceAccount:${{google_service_account.guardian_sa.email}}"
}}

# 4. The Compute Layer: Google Cloud Run
resource "google_cloud_run_v2_service" "guce_engine" {{
  name     = "guce-vertex-orchestrator"
  location = var.region

  template {{
    service_account = google_service_account.guardian_sa.email
    containers {{
      image = "gcr.io/${{var.project_id}}/guce-engine:latest" # Deployed via Antigravity
      env {{
        name  = "VERTEX_MODEL_GARDEN_ENDPOINT"
        value = "veo-3.1-flow" # Routing heavy lifting to Vertex AI
      }}
      env {{
        name  = "SHEETS_LEDGER_MODE"
        value = "APPEND_ONLY" # Guaranteeing Epistemic Stability
      }}
    }}
  }}
  depends_on = [google_project_service.guce_apis]
}}

# 5. Service Account for Cloud Scheduler
resource "google_service_account" "scheduler_sa" {{
  account_id   = "guce-scheduler-sa"
  display_name = "GUCE Automated Heartbeat SA"
  depends_on   = [google_project_service.guce_apis]
}}

# 6. Grant Scheduler Permission to Invoke Cloud Run
resource "google_cloud_run_v2_service_iam_member" "scheduler_invoker" {{
  name     = google_cloud_run_v2_service.guce_engine.name
  location = google_cloud_run_v2_service.guce_engine.location
  role     = "roles/run.invoker"
  member   = "serviceAccount:${{google_service_account.scheduler_sa.email}}"
}}

# 7. The Automation Heartbeat (Cloud Scheduler)
resource "google_cloud_scheduler_job" "guce_daily_batch" {{
  name             = "guce-vertex-daily-batch"
  description      = "Wakes up Cloud Run to process A-Roll through Vertex AI and log to Sheets."
  schedule         = "0 2 * * *" # 2:00 AM daily processing
  time_zone        = "America/Los_Angeles"
  region           = var.region

  http_target {{
    http_method = "POST"
    uri         = "${{google_cloud_run_v2_service.guce_engine.uri}}/process-queue"

    # Secure OIDC Authentication (Zero static keys required)
    oidc_token {{
      service_account_email = google_service_account.scheduler_sa.email
    }}
  }}
  depends_on = [google_cloud_run_v2_service_iam_member.scheduler_invoker]
}}
"""
        file_path = os.path.join(self.workspace_dir, "main.tf")
        with open(file_path, "w") as f:
            f.write(terraform_hcl)

        print(f"[ANTIGRAVITY] Terraform blueprint successfully written to: {file_path}")
        return file_path

    def strategize_next_step(self):
        """
        Proposes the next action within the Antigravity IDE.
        """
        print("\n[SYSTEM READY] The architecture securely bridges Antigravity, Cloud Run, Vertex AI, and Sheets.")
        print("Would you like me to write the Antigravity deployment script to automatically run `terraform apply` and initialize this new cloud project?")

if __name__ == "__main__":
    # Initialize the Antigravity Workspace for the new project
    workspace = AntigravityWorkspace()

    # Generate the unified infrastructure code
    workspace.build_infrastructure_manifest()

    # Prompt for execution
    workspace.strategize_next_step()
