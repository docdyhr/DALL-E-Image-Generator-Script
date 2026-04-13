"""Generate images using OpenAI's DALL-E API."""

import argparse
import json
import os
import sys
from pathlib import Path

import requests


def validate_size(value):
    """Validate image size argument."""
    allowed_sizes = ["1024x1024", "1792x1024", "1024x1792"]
    if value not in allowed_sizes:
        raise argparse.ArgumentTypeError(
            f"Size must be one of {', '.join(allowed_sizes)}."
        )
    return value


def validate_quality(value):
    """Validate image quality argument."""
    if value not in ["standard", "hd"]:
        raise argparse.ArgumentTypeError("Quality must be 'standard' or 'hd'.")
    return value


def validate_style(value):
    """Validate image style argument."""
    if value not in ["vivid", "natural"]:
        raise argparse.ArgumentTypeError(
            "Style must be 'vivid', 'natural', or not specified."
        )
    return value


def download_image(url, filename, custom_name=None):
    """Download an image from a URL to ~/Downloads."""
    downloads_path = str(Path.home() / "Downloads")
    if custom_name:
        if not custom_name.lower().endswith(".png"):
            custom_name += ".png"
        filepath = os.path.join(downloads_path, custom_name)
    else:
        filepath = os.path.join(downloads_path, filename)
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Image downloaded successfully to {filepath}\n")
    else:
        print("Failed to download image.\n")


def main():
    """Parse arguments and generate images via the DALL-E API."""
    parser = argparse.ArgumentParser(
        description="Generate images using OpenAI's DALL-E."
    )
    parser.add_argument(
        "-m", "--model", default="dall-e-3", help='Model to use, default is "dall-e-3".'
    )
    parser.add_argument(
        "-p", "--prompt", required=True, help="Prompt for the generation (obligatory)."
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of images to generate, default is 1.",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=validate_size,
        default="1024x1024",
        help='Size of the generated image, default is "1024x1024".',
    )
    parser.add_argument(
        "--quality",
        type=validate_quality,
        default="standard",
        help="Image quality: 'standard' or 'hd'. Default is 'standard'.",
    )
    parser.add_argument(
        "--style",
        type=validate_style,
        help="Image style: 'vivid' or 'natural'. Optional.",
    )
    parser.add_argument(
        "--output",
        choices=["json", "text"],
        default="text",
        help="Output format: json or text (default).",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download the generated image to ~/Downloads.",
    )
    parser.add_argument(
        "--filename",
        type=str,
        help="Optional custom filename for the downloaded image. "
        'Extension ".png" will be added if omitted.',
    )

    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.\n")
        sys.exit(1)

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {
        "model": args.model,
        "prompt": args.prompt,
        "n": args.number,
        "size": args.size,
        "quality": args.quality,
    }
    if args.style:
        data["style"] = args.style

    try:
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            json=data,
            headers=headers,
            timeout=60,
        )
        response.raise_for_status()

        print("Image generation successful.\n")
        result = response.json()
        if args.output == "json":
            print(json.dumps(result, indent=4) + "\n")
        else:
            for item in result["data"]:
                print(f"Revised Prompt: {item['revised_prompt']}\n")
                print(f"Image URL: {item['url']}\n")
                if args.download:
                    filename = (
                        item["url"].split("/")[-1]
                        if not args.filename
                        else args.filename
                    )
                    download_image(item["url"], filename, args.filename)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code}\n{e.response.text}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
