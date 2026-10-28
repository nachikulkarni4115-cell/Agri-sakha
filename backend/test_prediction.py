"""
Quick manual test for the /predict endpoint.

Usage:
    python test_prediction.py path/to/leaf.jpg
    python test_prediction.py path/to/leaf.jpg --url http://127.0.0.1:5000/predict
"""

import argparse
import sys

import requests

parser = argparse.ArgumentParser(description="Send a leaf image to /predict")
parser.add_argument("image_path", help="Path to a JPG / PNG / WEBP leaf photo")
parser.add_argument("--url", default="http://127.0.0.1:5000/predict")
args = parser.parse_args()

try:
    with open(args.image_path, "rb") as image_file:
        response = requests.post(
            args.url,
            files={"image": image_file},
            timeout=60
        )
except OSError as error:
    sys.exit(f"Could not open image: {error}")

print("Status Code:", response.status_code)

data = response.json()

# The heatmap is a long base64 string, so just report whether it came back.
if data.get("heatmap"):
    data["heatmap"] = f"<{len(data['heatmap'])} chars of base64 image>"

print("Response:")
print(data)
