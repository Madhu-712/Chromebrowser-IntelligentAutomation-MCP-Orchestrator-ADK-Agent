## Advanced Browser Orchestration & Analysis via Chrome DevTools MCP.

*Performance Intelligence: Audits web metrics and suggests optimizations to boost business KPIs.

*Dynamic Automation: Executes end-to-end tasks like form filling, page resizing, and navigation.

*Visual Captures: Automated screenshotting for testing and documentation.

*NLP-Driven: Converts user instructions directly into browser actions and technical insights.


## Overview
The Webperformance-Agent is an AI-powered tool designed to act as an expert web performance analyst. It leverages the Gemini-3-Flash LLM to interact with a browser environment, analyze critical web performance metrics (such as FCP, FID, LCP, and CLS), and provide deep insights into user experience and responsiveness. 

Core Web Vitals directly influence business success by improving user retention, increasing conversion rates, and boosting search engine visibility. 


*FCP (First Contentful Paint): Reduces initial bounce rates by giving users immediate visual feedback that the site is responsive and loading.

*LCP (Largest Contentful Paint): Directly correlates with higher conversion rates and sales by delivering the most important content before users lose interest.

*FID (First Input Delay): Enhances customer trust and interaction success by ensuring the site reacts instantly to their first click or tap.

*CLS (Cumulative Layout Shift): Prevents lost revenue and "accidental clicks" by keeping page elements stable and predictable during the user journey. 

## Business Performance Benchmarks:

Conversion Lift: A one-second improvement in load time can increase retail conversions by up to 8.4%.
Retention: Mobile users are 53% more likely to abandon a site if it takes longer than 3 seconds to load.
SEO Advantage: Sites meeting "Good" thresholds (e.g., LCP ≤ 2.5s) are prioritized by Google's ranking algorithm. 

 It also captures screenshots, and simulates various network conditions to generate detailed performance reports. The repository provides a structured framework for developers to orchestrate automated testing through a specialized agentic workflow. This system effectively bridges the gap between advanced AI reasoning and technical browser diagnostics to help optimize digital platforms.


## Architecture
The agent's architecture is centered around the `LlmAgent` from `google.adk.agents`. It uses a large language model (Gemini-3-Flash) for its analytical capabilities and decision-making. For interacting with the web browser, it utilizes an `MCPToolset` (Model Context Protocol Toolset) which connects to `chrome-devtools-mcp`. This allows the agent to control browser actions and gather detailed performance data.

**Conceptual Infographic for Architecture:**
<img width="2752" height="1536" alt="unnamed" src="https://github.com/user-attachments/assets/7f916d97-2b8e-4e8b-b214-610ba3fea30a" />


Here's a diagram with three main components:
1.  **"Gemini-3-Flash LLM (Brain)"**: Represented as a cloud or a brain icon.
    *   *Input*: User Commands (e.g., "Analyze webpage X", "Take a screenshot of Y").
    *   *Output*: Actions/Analysis requests.
2.  **"Webperformance-Agent (Orchestrator)"**: Represented as a central hub or a robot icon. This is the `LlmAgent` that interprets LLM output and orchestrates tool calls.
3.  **"Browser Environment (The Web)"**: Represented as a web browser window icon.
    *   *Controlled by*: `MCPToolset` (connecting to `chrome-devtools-mcp`).
    *   *Actions*: Performs Intelligent browser automation task like taking screenshots, resizing page, uploading files, filling forms based on natural language prompts(find hotels for 2 adults in Goa for tomorrow's date), managing tabs (close, hover, click), simulating key presses.
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

    # for adk setup
    Adk web or Adk run chromedevagent
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
