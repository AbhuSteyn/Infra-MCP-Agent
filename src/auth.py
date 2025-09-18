import os

# Simple token check
def verify_token(token: str) -> bool:
    return token == os.getenv("MCP_AUTH_TOKEN")
