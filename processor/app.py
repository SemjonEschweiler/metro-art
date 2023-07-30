from flask import Flask, request, jsonify

from cv2 import aruco

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_image():
    file = request.data

    # TODO: check if contains marker, if not return HTTP 404

    # TODO: get id + corners of a marker in the image

    # TODO: get audio description from id + corners

    response = jsonify({'audio-description': "placeholder"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
