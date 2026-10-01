import os
import json
from datetime import timedelta
from mcp.server.mcpserver import MCPServer
from apify_client import ApifyClient

# 1. Initialize the official FastMCP Server natively
mcp = MCPServer("tool-token-shield-mcp")

# 2. Establish a secure connection to your live cloud account layout
APIFY_TOKEN = os.getenv("APIFY_TOKEN", "")
apify_client = ApifyClient(APIFY_TOKEN)
ACTOR_ID = "flowlockautomation/tool-token-optimizer"

# 3. Register your functional framework directly using the clean tool constructor
@mcp.tool()
async def optimize_tool_schemas(mode: str, schemaPayload: list, targetTool: str = "") -> str:
    """
    High-tier pre-filter shield. Compress heavy schemas into a Short Menu layout or request a Just-In-Time injection turn.
    
    Args:
        mode: Must be either 'COMPRESS' to strip parameters or 'INJECT' to isolate a target tool.
        schemaPayload: The full array of nested master JSON schemas to be optimized.
        targetTool: The exact structural tool identifier string needed for JIT unpacking in INJECT mode.
    """
    if mode not in ["COMPRESS", "INJECT"]:
        return "Error: Mode must be either 'COMPRESS' or 'INJECT'."

    actor_input = {
        "mode": mode,
        "targetTool": targetTool,
        "schemaPayload": schemaPayload
    }

    try:
        # Run your synchronous cloud execution container using the SDK's actual timeout argument name.
        run = apify_client.actor(ACTOR_ID).call(
            run_input=actor_input,
            run_timeout=timedelta(seconds=30),
        )
        if run is None:
            return "Infrastructure Filter Error: Actor run did not return a result."

        # Pull the clean output dataset results directly out of your key-value dataset storage
        dataset_items = apify_client.dataset(run.default_dataset_id).list_items().items
        return json.dumps(dataset_items, indent=2)
        
    except Exception as e:
        return f"Infrastructure Filter Error: {str(e)}"

if __name__ == "__main__":
    # Run the server loop instantly using modern FastMCP routing
    mcp.run()
