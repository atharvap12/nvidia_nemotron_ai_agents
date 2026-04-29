# nvidia_nemotron_ai_agents

Hands-on examples covering AI agent fundamentals: a shopping agent, guardrails, and evaluation — powered by Nvidia Nemotron via OpenRouter.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/atharvap12/nvidia_nemotron_ai_agents.git
cd nvidia_nemotron_ai_agents
```

### 2. Configure environment variables

```bash
cp sample.env .env
```

Open `.env` and fill in your API keys:

```
GROQ_API_KEY=<your groq key here>
OPENROUTER_API_KEY=<your openrouter key here>
LANGSMITH_API_KEY=<your langsmith key here>
```

| Key | Where to get it |
|-----|----------------|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) |
| `OPENROUTER_API_KEY` | [openrouter.ai/keys](https://openrouter.ai/keys) |
| `LANGSMITH_API_KEY` | [smith.langchain.com](https://smith.langchain.com) |

### 3. Install dependencies

```bash
uv sync
```

### 4. Activate the virtual environment

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

## Running the examples

### 1. Shopping Agent

Set up the database, then run the agent:

```bash
python 1_shopping_agent/setup_db.py
python 1_shopping_agent/shopping_agent.py
```

### 2. Guardrails

```bash
python 2_guardrails/guardrails.py
```

### 3. Evaluation

```bash
python 3_eval/func_eval.py
```

### 4. Nvidia Nemotron (reasoning demo)

```bash
python nvidia_nemotron.py
```

## Project structure

```
nvidia_nemotron_ai_agents/
├── 1_shopping_agent/     # Tool-calling agent with a product reviews API
├── 2_guardrails/         # PII guardrail patterns (mask/redact)
├── 3_eval/               # Agent evaluation with LangSmith
├── nvidia_nemotron.py    # Nvidia Nemotron reasoning demo (multi-turn)
├── sample.env            # Template for environment variables
└── pyproject.toml        # Project dependencies (managed by uv)
```
