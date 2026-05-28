<div align="right">

<a href="https://railway.com?referralCode=QhjuBc">

  <img width="160" src="https://raw.githubusercontent.com/docdyhr/.github/main/assets/railway-corner-v2@2x.png" alt="Deploy on Railway — $20 free credits">

</a>

</div>

<p align="center">
  <img src="/images/Dall-E-3-Image-Generator.png" alt="Project Logo" width="200"/>
</p>

# DALL-E Image Generator Script

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pylint](https://github.com/docdyhr/DALL-E-Image-Generator-Script/actions/workflows/pylint.yml/badge.svg)](https://github.com/docdyhr/DALL-E-Image-Generator-Script/actions/workflows/pylint.yml)
[![CodeQL](https://github.com/docdyhr/DALL-E-Image-Generator-Script/actions/workflows/codeql.yml/badge.svg)](https://github.com/docdyhr/DALL-E-Image-Generator-Script/actions/workflows/codeql.yml)

A command-line script for generating images using OpenAI's DALL-E 3 (and DALL-E 2) models. Supports customisation of image quality, style, and size, with optional direct download to `~/Downloads`.

## Installation

Python 3.12 or later is required.

1. **Clone the repository**

   ```bash
   git clone https://github.com/docdyhr/DALL-E-Image-Generator-Script.git
   cd DALL-E-Image-Generator-Script
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**

   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

## Usage

```
python main.py -p <prompt> [options]
```

| Flag | Description | Default |
|---|---|---|
| `-p`, `--prompt` | Image generation prompt (**required**) | — |
| `-m`, `--model` | Model: `dall-e-3` or `dall-e-2` | `dall-e-3` |
| `-n`, `--number` | Number of images to generate | `1` |
| `-s`, `--size` | Image size: `1024x1024`, `1792x1024`, `1024x1792` | `1024x1024` |
| `--quality` | Quality: `standard` or `hd` | `standard` |
| `--style` | Style: `vivid` or `natural` (optional) | — |
| `--output` | Output format: `json` or `text` | `text` |
| `--download` | Download the generated image to `~/Downloads` | — |
| `--filename` | Custom filename for the downloaded image (`.png` appended if omitted) | — |

**Example:**

```bash
python main.py -p "A cute baby sea otter" --download --filename "cute_otter" --quality hd --style vivid
```

Generates an HD vivid-style image, downloads it to `~/Downloads/cute_otter.png`.

## Development

Dependencies are managed with [pip-tools](https://pip-tools.readthedocs.io/).

```bash
pip install pip-tools

# Install exact pinned versions
pip sync requirements.txt

# Upgrade all dependencies
pip-compile --upgrade requirements.in && pip sync requirements.txt

# Upgrade a single package
pip-compile --upgrade-package requests requirements.in
```

## Security

- API key is read from the `OPENAI_API_KEY` environment variable — never hardcoded.
- Secret scanning and push protection are enabled on this repository.
- Dependencies are audited on every CI run with `pip-audit` and `bandit`.
- CodeQL SAST runs on every push and weekly.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
