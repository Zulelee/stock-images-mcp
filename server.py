#!/usr/bin/env python3
"""
MCP Server for Stock Image Search and Download
Supports multiple stock image platforms: Pexels, Unsplash, Pixabay
"""

import os
import requests
import json
import sys
from typing import List, Dict, Optional, Any
from pathlib import Path
from urllib.parse import quote
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

print("--- Stock Images MCP Server Starting ---", file=sys.stderr)
sys.stderr.flush()

# Initialize the FastMCP server
mcp = FastMCP("stock-images-mcp")

# API Keys from environment variables
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

# Create downloads directory
DOWNLOADS_DIR = Path("downloads")
DOWNLOADS_DIR.mkdir(exist_ok=True)

class StockImageError(Exception):
    """Custom exception for stock image API errors"""
    pass

def validate_api_key(platform: str, api_key: str) -> None:
    """Validate that API key exists for the platform"""
    if not api_key:
        raise StockImageError(f"API key for {platform} not found. Please set {platform.upper()}_API_KEY in your .env file")

def search_pexels(query: str, per_page: int = 10) -> List[Dict[str, Any]]:
    """Search images on Pexels"""
    validate_api_key("Pexels", PEXELS_API_KEY)
    
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/v1/search?query={quote(query)}&per_page={per_page}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        images = []
        for photo in data.get("photos", []):
            images.append({
                "id": photo["id"],
                "url": photo["src"]["original"],
                "preview_url": photo["src"]["medium"],
                "photographer": photo["photographer"],
                "alt": photo.get("alt", ""),
                "width": photo["width"],
                "height": photo["height"],
                "platform": "pexels"
            })
        return images
    except requests.RequestException as e:
        raise StockImageError(f"Pexels API error: {str(e)}")

def search_pixabay(query: str, per_page: int = 10) -> List[Dict[str, Any]]:
    """Search images on Pixabay"""
    validate_api_key("Pixabay", PIXABAY_API_KEY)
    
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={quote(query)}&per_page={per_page}&image_type=photo"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        images = []
        for hit in data.get("hits", []):
            images.append({
                "id": hit["id"],
                "url": hit["largeImageURL"],
                "preview_url": hit["webformatURL"],
                "photographer": hit["user"],
                "alt": hit.get("tags", ""),
                "width": hit["imageWidth"],
                "height": hit["imageHeight"],
                "platform": "pixabay"
            })
        return images
    except requests.RequestException as e:
        raise StockImageError(f"Pixabay API error: {str(e)}")

@mcp.tool()
async def search_stock_images(query: str, platform: str = "all", per_page: int = 10) -> str:
    """
    Search for stock images across multiple platforms (Pexels, Pixabay)

    Args:
        query: Search query for images
        platform: Platform to search on (all, pexels, pixabay). Default: all
        per_page: Number of images to return per platform (1-50). Default: 10
    """
    print(f"MCP Tool (Stock Images): search_stock_images called with query: {query}, platform: {platform}", file=sys.stderr)
    
    try:
        results = {}

        if platform in ["all", "pexels"] and PEXELS_API_KEY:
            results["pexels"] = search_pexels(query, per_page)

        if platform in ["all", "pixabay"] and PIXABAY_API_KEY:
            results["pixabay"] = search_pixabay(query, per_page)
        
        if not results:
            return "No API keys configured. Please set up your API keys in the .env file."
        
        # Format results for display
        formatted_results = []
        for platform_name, images in results.items():
            formatted_results.append(f"\n## {platform_name.title()} Results ({len(images)} images):")
            for i, img in enumerate(images, 1):
                formatted_results.append(
                    f"{i}. **{img['photographer']}** - {img['width']}x{img['height']}\n"
                    f"   Preview: {img['preview_url']}\n"
                    f"   Full: {img['url']}\n"
                    f"   Alt: {img['alt']}\n"
                )
        
        return f"# Stock Image Search Results for '{query}'\n" + "\n".join(formatted_results)
        
    except StockImageError as e:
        return f"Error: {str(e)}"

def main():
    """Main function to run the MCP server"""
    mcp.run(transport='stdio')
    print("--- mcp.run() finished (should not happen if running as server) ---", file=sys.stderr)
    sys.stderr.flush()

if __name__ == "__main__":
    print("--- Entering main block, calling mcp.run() ---", file=sys.stderr)
    sys.stderr.flush()
    main()

print("--- Script reached end (should not happen if running as server) ---", file=sys.stderr)
sys.stderr.flush()
