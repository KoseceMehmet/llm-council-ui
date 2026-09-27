```markdown
# LLM COUNCIL // OPERATIONS DASHBOARD

An asynchronous, highly configurable multi-agent parallel reasoning and decision synthesis platform.

Inspired by Andrej Karpathy's `llm-council` architecture and Satya Nadella's vision of collaborative multi-agent LLM teams, this platform provides a centralized Security Operations Center (SOC/NOC) dashboard interface for orchestrating diverse language models, evaluating critical technical queries, and synthesizing optimal decision outputs.

---

## OVERVIEW

Complex engineering and cybersecurity decisions often suffer from single-model bias or hallucinations. The **LLM Council Operations Dashboard** addresses this by dispatching a single target prompt or context payload across an arbitrary number of specialized LLM agents in parallel. 

Each agent operates with isolated system prompts, model endpoints, and provider configurations (e.g., OpenRouter, Groq, OpenAI, or local Ollama instances). A designated Chairman agent aggregates all debate outputs, resolves logical discrepancies, and produces a final, actionable synthesis report.

---

## KEY FEATURES

- **Dynamic Agent Orchestration**: Scale council members dynamically from 1 to N without restarting the application. Configure custom agent names, model IDs, and system missions on the fly.
- **Flexible Key & Endpoint Management**: Manage API keys and custom local/remote endpoints dynamically through an isolated sidebar interface. Supports automatic key resolution and secure masking.
- **Asynchronous Parallel Execution**: High-throughput concurrent API fetching via `asyncio` and `httpx`, eliminating sequential bottlenecks during multi-model debates.
- **Human-in-the-Loop Decision Checkpoint**: Interactive decision controls allowing security analysts and engineers to review individual model outputs prior to triggering Chairman synthesis.
- **Context & Artifact Ingestion**: Native file ingestion supporting shell scripts, source code, JSON payloads, markdown documentation, and raw system logs.
- **Cybersecurity Operations Interface**: Dark-cyan high-contrast theme engineered for readability and high-density technical analysis, inspired by security operation dashboards.

---

## ARCHITECTURE

The repository is structured modularly to isolate core API logic, execution orchestrators, and user interface styling:

```text
llm-council-dashboard/
├── core/
│   ├── __init__.py
│   ├── providers.py      # Asynchronous API fetchers (OpenRouter, Groq, OpenAI, Ollama)
│   └── council.py        # Concurrent execution engine & Chairman synthesis logic
├── ui/
│   ├── __init__.py
│   ├── styles.py         # Custom CSS theme definitions
│   └── components.py     # Sidebar controllers, API managers, and UI panels
├── app.py                # Entrypoint application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

```

---

## PREREQUISITES & INSTALLATION

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/llm-council-dashboard.git](https://github.com/your-username/llm-council-dashboard.git)
cd llm-council-dashboard

```

### 2. Set Up Virtual Environment & Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

---

## USAGE GUIDE

### 1. Launch the Dashboard

```bash
streamlit run app.py

```

### 2. Configure System Parameters (Sidebar)

1. **API Keys & Endpoints**: Enter your API keys (OpenRouter, Groq, OpenAI) or specify your local Ollama endpoint (e.g., `http://localhost:11434`).
2. **Council Setup**: Add or remove council members as needed. Define specific missions for each agent (e.g., Reconnaissance Analyst, Code Auditor, Exploit Specialist).
3. **Chairman Selection**: Select the provider and model responsible for final synthesis.

### 3. Run Analysis

1. Enter your prompt or target query into the main input area.
2. (Optional) Attach a log file, script, or technical documentation.
3. Click **EXECUTE PARALLEL DEBATE** to dispatch requests concurrently.
4. Review individual agent analysis panels side-by-side.
5. Click **APPROVE SYNTHESIS** to generate the final unified decision report.

---

## INSPIRATION & ACKNOWLEDGMENTS

* **Andrej Karpathy**: For pioneering the `llm-council` open-source concept demonstrating multi-agent consensus workflows.
* **Satya Nadella / Microsoft Agentic Vision**: For emphasizing the paradigm shift toward collaborative LLM teams in software architecture and automated problem-solving.

---

## LICENSE

Distributed under the MIT License. See `LICENSE` for more information.

```

```
