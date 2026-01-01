"""
This file loads required secrets from the .env file into the mcp_config.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import json


load_dotenv()


def resolve_env_vars(config: dict) -> dict:
    """
    Resolve environment variables in the MCP configuration.

    Args:
        config: Configuration dictionary with potential ${VAR} placeholders

    Returns:
        Configuration with environment variables resolved

    Raises:
        ValueError: If required environment variables are not set
    """
    missing_vars = []

    for server_name, server_config in config["mcpServers"].items():
        for property in server_config.keys():
            if property == "env":
                for key, value in server_config[property].items():
                    if isinstance(value, str) and value.startswith("${"):
                        env_var_name = value[2:-1]
                        env_var_value = os.environ.get(env_var_name, None)
                        if env_var_value is None:
                            missing_vars.append(f"{env_var_name} (required by {server_name})")
                        else:
                            config["mcpServers"][server_name][property][key] = env_var_value
            if property == "args":
                for i, arg in enumerate(server_config[property]):
                    if isinstance(arg, str) and arg.startswith("${"):
                        env_var_name = arg[2:-1]
                        env_var_value = os.environ.get(env_var_name, None)
                        if env_var_value is None:
                            missing_vars.append(f"{env_var_name} (required by {server_name})")
                        else:
                            config["mcpServers"][server_name][property][i] = env_var_value

    if missing_vars:
        print("Warning: Missing environment variables:")
        for var in missing_vars:
            print(f"   • {var}")
        print("\nAdd these to your .env file or set them in your environment")
        print("Some MCP servers may not be available without these variables\n")

    return config


config_file = Path(__file__).parent / "mcp_config.json"
if not config_file.exists():
    raise FileNotFoundError(f"mcp_config.json file {config_file} does not exist")

with open(config_file, "r") as f:
    config = json.load(f)

mcp_config = resolve_env_vars(config)
