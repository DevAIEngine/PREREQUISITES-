# STRICTLY CONFIDENTIAL / PROPRIETARY / CLOSED-SOURCE
**WARNING:** DO NOT DISTRIBUTE. This repository contains the proprietary architecture, API optimization strategies ("Mini-Me" API Round-Robining), and catastrophic fallback modes ("Browser Vault" offline extraction) of the Google Universe Cinematic Engine. Access is strictly limited to the Principal Administrator and authorized AI Agents.

# Google Universe Cinematic Engine (GUCE)
**Status:** In Development (v5.0 Architecture) | **Primary Orchestrator:** Gemini 3.1 Pro

Welcome to the **Google Universe Cinematic Engine (GUCE)**. This is a federal-scale, fully autonomous documentary production platform designed for civic institutions, historical preservation, and hyper-efficient storytelling.

GUCE operates as a **"Cell Phone First"** platform. You dictate raw transcripts or stream live WebRTC audio; the engine natively decomposes scenes, auto-generates B-Roll, synthesizes multilingual audio clones, and orchestrates broadcast-ready 30-minute documentaries entirely within the cloud.

---

## 🏗️ The Multi-Channel Concurrent Factory
To eliminate enterprise compute costs and pipeline bottlenecks, GUCE utilizes a completely decentralized orchestration strategy:
*   **Branch A (Zero-Cost Native Shorts):** Unlimited 1-minute YouTube Shorts rendered for $0.00 using native Google Docs & Google Photos generation.
*   **Branch B (Heavy AI Chaining):** 30-minute deep dives looping through Vertex AI (Veo 3.1). If Vertex throttles, the load is dynamically rerouted to the massive Google Flow network.

## 🛡️ Epistemic Stability & Security
*   **The 7-Layer Guardian Wrapper:** A strict pre-flight circuit breaker. Enforces CCPA compliance and measures the **Vulnerability Paradox (σ² Variance)**. If the AI is uncertain (σ² > 1.47), it immediately halts rendering, logs to Google Sheets, and schedules a human review on Google Calendar.
*   **Data Locality (`us-west2`):** All Terraform deployments, Vertex endpoints, and Cloud Storage buckets are co-located in Los Angeles to evade crippling Advanced Data Networking (ADN) CDN egress fees.
*   **The "Mini-Me" Architecture:** API reads/writes are round-robined across 5+ free-tier Google Workspace accounts to exponentially expand 2TB storage limits.

---

## 🚀 Getting Started (The Nomadic Admin)
You do not need a heavy IDE to run this platform. Read the [Nomadic Admin Guide](docs/Nomadic_Admin_Guide.md) to manage the engine entirely from your cell phone (Termux) or Chromebook (Google Cloud Shell).

### 1. Trigger an Episode (Mobile/Termux)
To push a single Google Doc script entirely through the assembly line (Docs -> Slides -> Vids -> Vertex -> YouTube):
```bash
chmod +x make_episode.sh
./make_episode.sh "https://docs.google.com/document/d/YOUR_SCRIPT_URL"
```

### 2. Deploy to Google Cloud Run
GUCE is containerized. To push the orchestrator to production:
```bash
./infrastructure/deploy.sh
```

## 📖 Essential Documentation
*   **[Master Blueprint v5.0](GUCE_MASTER_BLUEPRINT_v5.md)** - The definitive architectural diagram.
*   **[Grid Down Resilience](GRID_DOWN_RESILIENCE.md)** - How the engine defaults to local FFmpeg/Notebook Islands during catastrophic internet failures.
*   **[Browser Vault](BROWSER_VAULT.md)** - Secure local storage of the 5+ API keys.
*   **[Jules Meta-Tooling](JULES_CAPABILITIES.md)** - How the AI leverages its Critic Agent and Playwright testing.

---

## 🤖 Summoning the AI (Jules)
This repository is autonomously managed by **Jules (Gemini 3.1 Pro)**.
To assign a new task:
1. Open a new **GitHub Issue**.
2. Add the label `jules`.
3. The AI will instantly read the `AGENTS.md` guidelines, fetch the repository, and autonomously resolve the issue and submit a Pull Request.