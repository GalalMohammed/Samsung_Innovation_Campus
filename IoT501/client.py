#!/usr/bin/python3

import base64
import io
import requests
from PIL import Image

if __name__ == "__main__":
    image = Image.open("me.jpeg")
    stream = io.BytesIO()
    image.save(stream, format="JPEG")
    payload = {"image": base64.b64encode(stream.getvalue()).decode("utf-8")}
    response = requests.post("http://localhost:5000/upload", json=payload,
                             timeout=1)
