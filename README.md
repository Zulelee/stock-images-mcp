# Stock Images MCP Server

A Model Context Protocol (MCP) server for searching and downloading stock images from Pexels and Pixabay. Built for personal use with Cursor and shared with the community.

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

The `uvx` command used in the MCP configuration requires `uv` to be installed on your system.

## 🚀 Quick Setup for Cursor

### Step 1: Add to Cursor's MCP Configuration

Add this configuration to your `~/.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "stock-images-mcp": {
      "command": "uvx",
      "args": ["git+https://github.com/Zulelee/stock-images-mcp"],
      "env": {
        "PEXELS_API_KEY": "your_pexels_api_key_here",
        "PIXABAY_API_KEY": "your_pixabay_api_key_here"
      }
    }
  }
}
```

### Step 2: Get API Keys (At least one of the API keys is required)

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
- Search specific platforms: "Search Pexels for coding setup images"

## Available Tools

- **`search_stock_images`**: Search across Pexels and Pixabay
