# main.tf - GUCE Native Universe (Converged)

variable "project_id" {
  description = "The GCP project ID"
  type        = string
  default     = "guce-nextgen-prod-001"
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-west2"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# --- 1. API Provisioning (The Keys) ---
resource "google_project_service" "guce_apis" {
  for_each = toset([
    "iam.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "sts.googleapis.com",
    "secretmanager.googleapis.com",
    "run.googleapis.com",
    "aiplatform.googleapis.com",   # Gemini & Veo
    "vids.googleapis.com",         # Cinematic assembly
    "keep.googleapis.com",         # Story sparks
    "forms.googleapis.com",        # Community intake
    "sheets.googleapis.com",       # Narration Library & Logs
    "drive.googleapis.com",        # Project Manifest storage
    "youtube.googleapis.com",      # Publishing & Analytics
    "slides.googleapis.com",       # Storyboarding
    "cloudscheduler.googleapis.com" # Automation Heartbeat
  ])
  project            = var.project_id
  service            = each.key
  disable_on_destroy = false
}

# --- 2. 7-Layer Guardian Identity ---
resource "google_service_account" "guardian_sa" {
  account_id   = "guce-guardian-native"
  display_name = "GUCE Native Guardian Service Account"
}

# Granting "Universe" Access to the Guardian
resource "google_project_iam_member" "guardian_roles" {
  for_each = toset([
    "roles/aiplatform.user",
    "roles/sheets.editor",
    "roles/drive.file",
    "roles/run.invoker"
  ])
  project = var.project_id
  role    = each.key
  member  = "serviceAccount:${google_service_account.guardian_sa.email}"
}

# --- 3. Compute Layer: Google Cloud Run ---
resource "google_cloud_run_v2_service" "guce_engine" {
  name     = "guce-vertex-orchestrator"
  location = var.region

  template {
    service_account = google_service_account.guardian_sa.email
    containers {
      image = "gcr.io/${var.project_id}/guce-engine:latest"
      env {
        name  = "PROJECT_MANIFEST_ID"
        value = "GUCE_MASTER_MANIFEST"
      }
    }
  }
}

# --- 4. Automation Heartbeat: Cloud Scheduler ---
resource "google_service_account" "scheduler_sa" {
  account_id   = "guce-scheduler-sa"
  display_name = "GUCE Automated Heartbeat SA"
}

resource "google_cloud_run_v2_service_iam_member" "scheduler_invoker" {
  name     = google_cloud_run_v2_service.guce_engine.name
  location = google_cloud_run_v2_service.guce_engine.location
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.scheduler_sa.email}"
}

resource "google_cloud_scheduler_job" "daily_assembly" {
  name             = "guce-daily-assembly"
  description      = "Wakes up the engine to process Kimiy's scripts at 2 AM."
  schedule         = "0 2 * * *"
  time_zone        = "America/Los_Angeles"
  region           = var.region

  http_target {
    http_method = "POST"
    uri         = "${google_cloud_run_v2_service.guce_engine.uri}/process-queue"
    oidc_token {
      service_account_email = google_service_account.scheduler_sa.email
    }
  }
}
