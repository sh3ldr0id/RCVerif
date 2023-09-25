from flask import Flask, render_template, request, jsonify
import base64
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_base64 = data.get('imageBase64', '')

    # Decode the base64 image to binary data
    image_data = base64.b64decode(image_base64.split(',')[-1])

    # Process the image using OpenCV
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    cv2.imwrite("pic.png", img)

    print("Done")

    return jsonify({"width": img.shape[1], "height": img.shape[0]})

if __name__ == '__main__':
    app.run()
