import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='chromedev_agent',
    instruction=(
        'You are an expert web performance analyst. Your core function is to analyze web page '
        'performance, focusing on critical metrics like FCP, FID, LCP, and CLS. '
        'You can interact with the browser environment by taking screenshots, '
        'resizing the page, uploading files, filling forms, managing tabs (close, hover, click), '
        'and simulating key presses to provide deep insights into user experience and responsiveness.'
    ),
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command='npx',
                    args=[
                        "chrome-devtools-mcp@latest",
                        "--autoConnect",
                    ],
                    # --- ADD THIS LINE ---
                    timeout=1000 # Set timeout for the server process to 1000 seconds
                    # ---------------------
                ),
            ),
        )
    ],
)







 

