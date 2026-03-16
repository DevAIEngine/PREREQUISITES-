# Findings

* **Initial Discovery:** Repository is currently an empty GitHub classroom setup.
* **Architecture Source:** Extensively ingested "Google Universe Cinematic Engine (GUCE) Blueprint Version 4.0".
* **Key Constraints:** Must strictly follow 500-token daily agent budget via "Progressive Disclosure". Must implement "Working Memory on Disk" (2-Action Rule).
* **Target Execution:** Python-based FastApi backend to orchestrate Gemini, Veo, Cloud TTS, FFmpeg, Google Drive/Photos, Calendar, and the "7-Layer Guardian Wrapper" for legal liability. Focus on backend logic, safeguards, and iterative ML tuning.
* **Infrastructure Discovery:** Hosted on Google Cloud Run via Vertex AI Model Garden, triggered by a Cloud Scheduler heartbeat via OIDC every night at 2:00 AM.
* **Cloud Run / IAM:** The user provided a Flask `app.py` for Cloud Run along with IAM commands to provision `guce-sa@gen-lang-client-0446134261.iam.gserviceaccount.com` with `aiplatform.user`, `drive.editor`, `sheets.editor`, and `run.invoker`. Created `infrastructure/deploy.sh` to automate this deployment.
* **Frontend UI:** The user provided a React/TypeScript `SeniorFriendlyGeminiUI.tsx` frontend that uses WebRTC for camera/mic inputs and WebSockets for real-time Gemini streaming.
* **Cost Optimizations:**
    1. **Data Egress:** To avoid Advanced Data Networking (ADN) costs from Network Connectivity Center and CDN interconnect egress fees, Compute, Storage, and Vertex resources are strictly co-located in `us-west2` (Los Angeles).
    2. **Multi-Account Quota Expansion:** The user dictates a strategy of "cutting corners" by intentionally decentralizing operations across multiple Google free-tier accounts. Drive, Sheets, Forms, and Calendar libraries will be handled by entirely separate depositories and service accounts to stack free limits instead of centralizing billing.
    3. **The Concurrent Factory (Zero-Cost Shorts):** Leveraging Google Docs and Google Photos native AI to generate unlimited 1-minute to 3-minute video montages entirely for free ($0.00 cost) before triggering expensive Vertex AI / Antigravity pipelines for the 30-minute long-form chaining.
    4. **34-Channel Pipeline Resilience:** The `assembly_line.py` orchestrator utilizes a strict load-balancing architecture. If the main Vertex AI generation endpoint (`channel_4_vertex_veo`) fails or is throttled, the orchestrator instantly reroutes the workload to Google Flow (`channel_5_google_flow`) to prevent pipeline stagnation and guarantee 100% production uptime.