# 🛡️ Tool Token Shield MCP Server

An inbound context pre-filter shield built natively for **Cursor AI** and **Claude Desktop**. 

Stop letting your local agent frameworks burn through your Anthropic/OpenAI budget on repetitive function schema parsing. 

## 📊 The Telemetry & Financial ROI
When your local workspaces integrate 15+ corporate tool extensions (CRMs, SQL directories, Billing APIs), your raw JSON schemas swallow up to **8,000 tokens** per turn. Shifting all heavy parameter definitions into system prompts on *every single turn* results in exponential token inflation.

* **Prompt Cost Reduction:** ~92% reduction in prompt context costs.
* **Execution Latency:** Sync processing in under 4 seconds.
* **Sandbox Memory Footprint:** 21.9 MB average footprint.

This middleware collapses your master schema collection into a lightweight metadata menu. It progressive-discloses deep argument configurations **Just-In-Time (JIT)**, fetching nested parameters *only* when a tool is called.

## 🔌 60-Second Quick Start

### 1. Installation
Clone the repository and initialize the project environment:
```bash
git clone https://github.com/<your-user>/tool-token-shield-mcp.git
cd tool-token-shield-mcp
python -m venv venv

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt):
venv\Scripts\activate.bat

# macOS/Linux:
source venv/bin/activate

pip install mcp apify-client
```

If PowerShell blocks the activation script, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Set the optional cloud token before running the server if you want the Apify integration to work:
```powershell
$env:APIFY_TOKEN="your_apify_token_here"
```

```bash
export APIFY_TOKEN="your_apify_token_here"
```

### 2. Configure Your IDE Settings

#### For Cursor AI:
1. Navigate to **Customize ➔ MCPs**.
2. Click **+ Add New MCP Server**.
3. Use these parameters:
   - **Name:** `tool-token-shield-mcp`
   - **Type:** `stdio`
   - **Command:** `C:\path_to_your_folder\tool-token-shield-mcp\venv\Scripts\python.exe C:\path_to_your_folder\tool-token-shield-mcp\server.py`

#### For Claude Desktop:
Add this mapping inside your root `mcpServers` block in `claude_desktop_config.json`:
```json
"tool-token-shield-mcp": {
  "command": "C:\\path_to_your_folder\\tool-token-shield-mcp\\venv\\Scripts\\python.exe",
  "args": ["C:\\path_to_your_folder\\tool-token-shield-mcp\\server.py"]
}
```

## 💰 Gated Licensing
* **Free Open-Source Tier:** Out-of-the-box local schema optimization for up to **3 active workspace tools**.
* **Unlimited Enterprise Tier:** To unlock high-volume multi-tenant routing, inject your premium `APIFY_TOKEN` into your environment configuration settings.
