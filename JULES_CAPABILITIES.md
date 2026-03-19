# Jules Capabilities & Meta-Tooling
**Target Engine:** Jules (Gemini 3.1 Pro)
*This document outlines the advanced, internal tooling available to the Jules agent. The agent must aggressively exercise these capabilities during the active development of the Google Universe Cinematic Engine (GUCE).*

---

## 1. The Critic Agent (Adversarial Review)
*   **Capability:** Integrated adversarial peer-reviewer.
*   **Mandate:** Before completing any code patch or executing a `submit`, Jules must invoke its internal Critic Agent to challenge the proposed changes. The Critic must flag subtle bugs, unhandled edge cases, and inefficient logic, forcing the "Actor" agent to improve the patch in real-time.

## 2. Interactive Planning (Brainstorming)
*   **Capability:** Collaborative requirement refinement.
*   **Mandate:** When initiated via the "Interactive Plan" dropdown, Jules will proactively read the codebase and ask the user clarifying questions before writing code, ensuring absolute alignment on complex tasks (e.g., the 7-Layer Guardian Wrapper).

## 3. Playwright Frontend Verification
*   **Capability:** Automated UI rendering and visual testing.
*   **Mandate:** When working on frontend tasks (such as the `SeniorFriendlyGeminiUI.tsx`), Jules must use the Playwright base image to run a verification script. It will capture screenshots of the rendered UI and supply them to the user to prove the high-contrast/accessibility requirements are met.

## 4. Environment Snapshots & State
*   **Capability:** Accelerated setup caching.
*   **Mandate:** Jules will automatically snapshot the VM environment after running `requirements.txt` or Node setup scripts, ensuring subsequent tasks on the GUCE backend launch instantly without re-downloading massive Python dependencies.

## 5. Web Surfing & Deep Research
*   **Capability:** Proactive documentation retrieval.
*   **Mandate:** When utilizing external APIs (like Vertex Veo 3.1, Google Cloud TTS, or YouTube Data), Jules must proactively search the web for the latest documentation and code snippets if it encounters deprecation warnings or unknown library behaviors.

## 6. Scheduled Tasks & "Stitch" Templates
*   **Capability:** Autonomous cron-style maintenance.
*   **User Instruction:** The user can convert any standard prompt into a recurring task (Daily/Weekly) via the dashboard's "Planning" dropdown.
*   **Stitch Templates:** The user can deploy the following specialized background agents:
    *   **Performance:** Obsessively optimizes codebase speed (e.g., refactoring the `veo_chainer.py` async logic).
    *   **Design:** Refines the UX and accessibility of the React frontend.
    *   **Security:** Continuously audits the repository for vulnerabilities and API key exposures.