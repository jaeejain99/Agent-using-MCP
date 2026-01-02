# Agent-using-MCP

The project showcases a data science assistant that can help users manage their data science projects using various MCP-powered tools.

## Overview

The project implements a conversational AI agent that:
- Uses GPT-4.1 as the base model
- Integrates with multiple MCP servers for different functionalities
- Uses Langgraph for orchestrating the conversation flow
- Provides a streaming interface for real-time responses

## Prerequisites

- Python 3.13+
- Node.js (for filesystem MCP server)
- Docker (for GitHub MCP server)
- UV package manager
- OpenAI API key

## Project Structure

```
my_agent/
├── graph.py           # Langgraph agent implementation
├── client.py          # MCP client and streaming interface
└── my_mcp/           # MCP server configurations
    ├── config.py     # Config loading and env var resolution
    ├── mcp_config.json # MCP server definitions
    └── local_servers/ # Custom MCP server implementations
        └── dataflow.py # Custom implementation for data loading and querying
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Agent-using-MCP
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
uv sync
uv pip install -e .
```

4. Set up environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key
MCP_FILESYSTEM_DIR=/path/to/projects/directory
MCP_GITHUB_PAT=your_github_personal_access_token
```

## MCP Servers

This project integrates with four MCP servers:

1. **Dataflow Server**: Custom implementation for data loading and querying
2. **Filesystem Server**: Uses `@modelcontextprotocol/server-filesystem` for file operations
3. **Git Server**: Uses `mcp-server-git` for local git operations
4. **GitHub Server**: Uses the official GitHub MCP server for GitHub operations

## Usage

1. Start the application:
```bash
python -m my_agent.client
```

2. Interact with the Agent by typing your questions or requests. For example:
```
USER: Can you help me set up a new data science project?
```

3. Agent will use its tools to:
- Create and manage project directories
- Handle data loading and transformation
- Manage version control
- Interact with GitHub repositories

4. Type 'quit' or 'exit' to end the session.

## How It Works

1. The `graph.py` file defines the Langgraph agent structure:
- Sets up the system prompt and agent state
- Configures the LLM (GPT-4)
- Defines the conversation flow graph

2. The `client.py` file:
- Initializes the MCP client with multiple servers
- Handles streaming responses
- Manages the interactive session

3. MCP servers provide tools for:
- File system operations
- Data manipulation
- Git operations
- GitHub interactions