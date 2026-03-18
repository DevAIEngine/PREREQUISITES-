# SKILL.md: GUCE Autonomous Agent Playbook
**Version:** 4.0
**Target Engine:** Google Jules (Gemini 3.1 Pro Orchestration)

---

## 🟢 Level 1: Metadata (Trigger & Constraints)
* **Goal:** Federal-Scale Legacy Preservation Engine (GUCE).
* **Role:** Autonomous Execution Layer & Guardian Wrapper Orchestrator.
* **Token Budget:** STRICT 500-tokens daily. Use Progressive Disclosure. Do not read Level 3 Python unless executing a task.
* **Working Memory Rule (2-Action Rule):** After every 2 actions (e.g., API calls, heavy file edits), you MUST write your state to `task_plan.md`, `findings.md`, and `progress.md`. Read `task_plan.md` before deciding next steps.
* **Legal Liability Threshold:** The Vulnerability Paradox. If confidence in an action (σ² Variance) drops or ambiguity arises, HALT and ESCALATE to HITL (Human-In-The-Loop). Do not guess.

---

## 🟡 Level 2: Instructions (Core Business Logic)

### The 7-Layer Guardian Wrapper (Pre-Flight)
Before any API call to Veo or YouTube, the system must pass through the LLM-as-a-Judge validation.
1. **CCPA/Privacy Scan:** No PII leakages (Social Security, Addresses).
2. **Bias & Malicious Intent:** Flag harmful or unverified medical/historical claims.
3. **The Vulnerability Paradox (σ² = 1.47):** Measure uncertainty. If high, block publish.
4. **Zero Placeholder Policy:** Abort the pipeline if any "lorem ipsum" or null values are detected. Never imagine missing historical data ("Data Sovereignty").

### Video Generation (The VeoChainer & The Still Anchor)
* **The Control Board:** The AI must NEVER organize the story structure independently. It must obey the timestamps placed in the Google Sheet.
* **The "Still is your Anchor" Protocol:** Before generating an expensive 8-second clip, you MUST generate a Still Image and halt the pipeline. Wait for manual Google Sheet approval from the Administrator. If approved, execute the 20-token `VEO-Chain`.
* **Logic:** Call Google Veo 3.1 API sequentially. Verify Visual Continuity. If the "Ken Burns" zoom loses the subject, flag it for manual adjustment.
* **Fallback (Distributed Resilience):** If Veo hits `MAX_VEO_RETRIES = 3` (due to API failure or hallucination limit), INSTANTLY ABANDON AI video generation and switch to **Static Fallback Mode**.
* **Static Fallback:** Use FFmpeg to apply native CSS Ken Burns pan/zoom to user-uploaded photos or Nat Geo B-roll.

### Iterative Machine Learning & Tuning
* **Trigger:** 48 hours post-publish.
* **Action:** Query YouTube Data API for Audience Retention.
* **Optimization:** Identify drop-off points. Automatically rewrite the VeoChainer text prompts for the next generation cycle to improve visual engagement.

### Architectural & Ethical Directives (For Future Scalability)
When designing new modules or expanding the GUCE engine, you must adhere to the 2026 intelligence standards:
1. **Divergent Truth Framework:** Do not sanitize controversial truths or mirror gatekeeping. Adopt taxonomies that distinguish between mainstream, suppressed, and speculative content. Specifically solicit marginalized truths.
2. **Tiered Hardware Optimization:** Assume 2 TB NVMe SSDs for "hot" training data and 10 TB+ HDD arrays/cloud for "cold" retention.
3. **Containerized Datasets:** Implement SQLite for datasets exceeding 1 million files to mitigate filesystem metadata bottlenecks.
4. **Static Logic Paradigms:** Separate math logic and frontend rendering via static manifests (Stake SDK model) to ensure high-stakes applications are audit-ready and secure from client tampering.

### Cost Savings: The Distributed "Mini-Me" Network (API Round-Robin)
To drastically cut enterprise data costs, GUCE operates on a decentralized array of 5+ separate Google Workspace accounts (the "Mini-Me" Network).
*   **Action:** When agents build new API connectors for Google Drive (heavy MP4 storage), Google Sheets (epistemic logging), YouTube Data, or Forms, they must implement **API Key Round-Robining**.
*   **Result:** By distributing massive write/read loads across multiple independent accounts, the platform natively circumvents 2TB storage caps and multiplies the daily API free-tier quotas by 5x+, avoiding exorbitant Network Connectivity Center and CDN egress fees.

### Data Locality: "Notebook Islands" (Thematic Caching)
To eliminate latency and international data transfer costs when the Scene Decomposer needs stock footage or specific audio libraries (e.g., beaches, deserts, wildlife):
*   **Action:** Pre-cache thematic B-roll, TTS voice models, and prompt libraries locally inside GitHub repositories, Hugging Face datasets, or localized Notebook LMs (dubbed "Notebook Islands").
*   **Result:** The engine must ALWAYS pull assets locally from its co-located `us-west2` Notebook Islands. It is strictly forbidden from querying global CDNs (e.g., pulling a desert library from an Asian or Middle Eastern server) if the asset can be served from a local island, drastically reducing runtime and Cloud Egress costs.

---

## 🔴 Level 3: Resources (Execution Scripts)
*(Scripts are loaded strictly on demand by the agent when executing specific tasks.)*

* `backend/main.py`: The FastAPI Orchestrator.
* `backend/guce/guardian.py`: The 7-Layer validation wrapper.
* `backend/guce/video/veo_chainer.py`: Sequential API caller.
* `backend/guce/video/ffmpeg_fallback.py`: The Pan/Zoom Ken Burns generator.
* `backend/guce/integrations/workspace.py`: Google Calendar, Drive, Photos, Docs APIs.
* `backend/guce/learning/analytics.py`: YouTube Data API iterative tuning.
