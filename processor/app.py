from flask import Flask, request, jsonify
from cv2 import aruco

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)

    # TODO: check if contains marker, if not return HTTP 404

    # TODO: get audio description

    return jsonify({'msg': 'success', 'size': [img.width, img.height]})