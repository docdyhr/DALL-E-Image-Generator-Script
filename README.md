<p align="center">
  <img src="/images/Dall-E-3-Image-Generator.png" alt="Project Logo" width="200"/>
</p>

# DALL-E Image Generator Script

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project provides a script for generating images using OpenAI's DALL-E 3 model, with options for customization and downloading the generated images. It offers customization options for the image generation process, including model selection, image quality, and style preferences. Users also have the capability to download the generated images directly to their system.

## Version 1.0

### Installation

Before utilizing the script, ensure Python is installed on your system. This script is compatible with Python version 3.6 and above.

1. **Clone the Repository**

   Begin by cloning this repository to your local machine using Git:

   ```bash
   git clone https://github.com/docdyhr/dall-e-image-generator.git
   cd dall-e-image-generator
   ```

2. **Install Dependencies**

   The script requires the `requests` library. Install all necessary dependencies using pip and the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**

   An OpenAI API key is essential for using this script. Set your API key as an environment variable in your terminal:

   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

   Make sure to replace `your_api_key_here` with your actual OpenAI API key.

### Usage

The script supports several flags to tailor the image generation process:

- `-m`, `--model`: Specifies the model to use, defaulting to "dall-e-3".
- `-p`, `--prompt`: The required prompt for image generation.
- `-n`, `--number`: The number of images to generate, with a default of 1.
- `-s`, `--size`: The size of the generated image, defaulting to "1024x1024". Allowed values include 1024x1024, 1792x1024, and 1024x1792.
- `--output`: Determines the output format, either 'json' or 'text' (default).
- `--download`: If set, downloads the generated image to `~/Downloads`.
- `--filename`: An optional custom filename for the downloaded image. A '.png' extension will be appended if omitted.
- `--quality`: The image quality, either "standard" or "hd" (defaults to "standard").
- `--style`: The image style, either "vivid" or "natural" (optional).

**Example Command:**

```bash
python generate_image.py -p "A cute baby sea otter" --download --filename "cute_otter" --quality "hd" --style "vivid"
```

This command generates an HD, vivid-style image based on the prompt "A cute baby sea otter", downloads it to the `~/Downloads` folder, and names the file `cute_otter.png`.

### Error Handling

The script includes error handling to address issues such as invalid API keys or request parameters. If an error occurs, the script will print the error message and terminate gracefully.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
