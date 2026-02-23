# Webperformance-Agent

## Overview
The Webperformance-Agent is an AI-powered tool designed to act as an expert web performance analyst. It leverages the Gemini-3-Flash LLM to interact with a browser environment, analyze critical web performance metrics (such as FCP, FID, LCP, and CLS), and provide deep insights into user experience and responsiveness. This agent is capable of simulating various user interactions and capturing performance data to help optimize web applications.

## Architecture
The agent's architecture is centered around the `LlmAgent` from `google.adk.agents`. It uses a large language model (Gemini-2.5-Flash) for its analytical capabilities and decision-making. For interacting with the web browser, it utilizes an `MCPToolset` (Managed Code Program Toolset) which connects to `chrome-devtools-mcp`. This allows the agent to control browser actions and gather detailed performance data.

**Conceptual Infographic for Architecture:**
Imagine a diagram with three main components:
1.  **"Gemini-3-Flash LLM (Brain)"**: Represented as a cloud or a brain icon.
    *   *Input*: User Commands (e.g., "Analyze webpage X", "Take a screenshot of Y").
    *   *Output*: Actions/Analysis requests.
2.  **"Webperformance-Agent (Orchestrator)"**: Represented as a central hub or a robot icon. This is the `LlmAgent` that interprets LLM output and orchestrates tool calls.
3.  **"Browser Environment (The Web)"**: Represented as a web browser window icon.
    *   *Controlled by*: `MCPToolset` (connecting to `chrome-devtools-mcp`).
    *   *Actions*: Taking screenshots, resizing page, uploading files, filling forms, managing tabs (close, hover, click), simulating key presses.
    *   *Data Collected*: FCP, FID, LCP, CLS, network requests, console logs, trace data.
Arrows would flow from LLM to Agent, and from Agent to Browser (for actions) and back from Browser to Agent (for data/feedback), and then to LLM for analysis.

## Project Structure

```
.
├── chromedevagent/
│   ├── __init__.py
│   ├── agent.py                 # Main agent logic and configuration
│   ├── evalset064343.evalset.json # Evaluation dataset (example)
│   ├── .env                     # Environment variables (ignored)
│   └── __pycache__/             # Python cache files (ignored)
├── performance_reports/
│   ├── desktop_2g.json          # Example performance reports for different conditions
│   ├── desktop_3g.json
│   ├── desktop_4g.json
│   ├── desktop_5g.json
│   ├── mobile_2g.json
│   ├── mobile_3g.json
│   ├── mobile_4g.json
│   └── mobile_5g.json
├── .adk/                        # ADK-related artifacts (ignored)
├── .venv/                       # Python virtual environment (ignored)
├── makemytrip_landing_page.png  # Example asset
├── makemytrip_performance_report.md # Example performance analysis report
└── README.md                    # This file
```

## Getting Started

To get started with the Webperformance-Agent, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Madhu-712/Webperformance-Agent.git
    cd Webperformance-Agent
    ```
2.  **Set up a Python virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    *(Assuming dependencies are specified in a `requirements.txt` or similar file, which would need to be created based on the `adk` and `mcp` imports)*
    ```bash
    pip install google-generativeai google-cloud-aiplatform mcp chrome-devtools-mcp
    ```
    *Note: The exact dependencies might need to be refined based on the full `adk` and `mcp` setup.*

4.  **Configure Environment Variables:**
    Create a `.env` file in the `chromedevagent/` directory (if not already present) and add any necessary API keys or configuration. *Refer to `chromedevagent/.env` for examples or specific requirements, though it's typically ignored for security reasons.*

5.  **Run the agent:**
    *(Specific execution command for the agent would be needed, e.g., `python -m chromedevagent.agent` or a command provided by the `adk` framework)*
    ```bash
    # Example command (may vary based on ADK setup)
    python chromedevagent/agent.py 
    ```
    *Ensure `npx chrome-devtools-mcp` is accessible in your PATH for the `MCPToolset` to function correctly.*

## Contributions
We welcome contributions to the Webperformance-Agent! Please refer to our `CONTRIBUTING.md` (to be created) for guidelines on how to submit issues, features, and pull requests.

## Licenses
This project is licensed under the [Your License Here] - see the `LICENSE` file for details. (A `LICENSE` file would need to be created).

## Resources
*   [Google ADK Documentation](https://ai.google.dev/adk)
*   [Gemini API Documentation](https://ai.google.dev/docs/gemini_api_overview)
*   [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
*   [Chrome DevTools MCP: Debug your browser session](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session)
