# Agent-using-MCP

The project showcases a data science assistant that can help users manage their data science projects using various MCP-powered tools.

## Overview

The project implements a conversational AI agent that:
- Uses GPT-4.1 as the base model
- Integrates with multiple MCP servers for different functionalities
- Uses Langgraph for orchestrating the conversation flow
- Provides a streaming interface for real-time responses

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