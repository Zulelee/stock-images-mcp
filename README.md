# Stock Images MCP Server

A Model Context Protocol (MCP) server for searching and downloading stock images from multiple platforms. Built for personal use with Cursor and shared with the community.

## One-Click Install

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=stock-images-mcp&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJnaXQraHR0cHM6Ly9naXRodWIuY29tL1p1bGVsZWUvc3RvY2staW1hZ2VzLW1jcCJdfQ==) [![Install in Claude Desktop](https://img.shields.io/badge/Install_in-Claude_Desktop-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/Zulelee/stock-images-mcp/raw/main/stock-images-mcp.mcpb)

| Client | What happens when you click |
| --- | --- |
| **Cursor** | Opens Cursor and adds the MCP server to your config. You'll be prompted to add your API keys in MCP settings. Requires [uv](#prerequisites) to be installed. |
| **Claude Desktop** | Downloads the `.mcpb` bundle. Double-click it (or drag it into Claude Desktop) and click **Install**. You'll be prompted for API keys during setup. |

After installing, add at least one API key (see [Get API Keys](#step-2-get-api-keys-atleast-one-of-the-api-keys-is-required)) and restart the client if needed.

## Prerequisites

Before setting up this MCP server, you need to install `uv`, a fast Python package installer and resolver:

### Install uv

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**

```bash
pip install uv
```

The `uvx` command used in the Cursor MCP configuration requires `uv` to be installed on your system. The Claude Desktop `.mcpb` bundle handles dependencies automatically.

## Manual Setup

### Cursor

#### Step 1: Add to Cursor's MCP Configuration

Add this configuration to your `~/.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "stock-images-mcp": {
      "command": "uvx",
      "args": ["git+https://github.com/Zulelee/stock-images-mcp"],
      "env": {
        "UNSPLASH_API_KEY": "your_unsplash_api_key_here",
        "PEXELS_API_KEY": "your_pexels_api_key_here",
        "PIXABAY_API_KEY": "your_pixabay_api_key_here"
      }
    }
  }
}
```

### Claude Desktop

1. Download [`stock-images-mcp.mcpb`](stock-images-mcp.mcpb) from this repo (or use the **Install in Claude Desktop** button above).
2. Double-click the file, or open Claude Desktop → **Settings** → **Extensions** → **Install Extension…**
3. Enter your API keys when prompted (at least one is required).
4. Restart Claude Desktop.

### Step 2: Get API Keys (Atleast one of the API keys is required)

**Unsplash:**

1. Go to https://unsplash.com/developers
2. Make sure you are logged in
3. Create an app
4. Get your API key from the app dashboard

**Pexels:**

1. Go to https://www.pexels.com/api/
2. Make sure you are logged in
3. Click "Your API Key" button
4. Copy your API key

**Pixabay:**

1. Go to https://pixabay.com/api/docs/
2. Make sure you are logged in
3. Find your API key under "Parameters" in the docs

### Step 3: Activate the Tool in Cursor Settings

Switch on the toggle for stock-images-mcp in cursor settings

### Step 4: Use the Tools

Once the tool connects, you can use the stock images tools directly in your conversations:

- Search for images: "Find tech workspace images"
- Download images: "Download 5 nature photos"
- Search specific platforms: "Search Unsplash for coding setup images"

## Available Tools

- **`search_stock_images`**: Search across Pexels, Unsplash, and Pixabay
