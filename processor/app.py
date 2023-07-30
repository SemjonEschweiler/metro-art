import base64
import cv2
import flask
import numpy
import output_ID

app = flask.Flask(__name__)

def base64ToNp(imageAsBase64):
    nparr = numpy.frombuffer(base64.b64decode(imageAsBase64), numpy.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

@app.route("/process", methods=["POST"])
def process_image():
    openCvImage = base64ToNp(flask.request.data)

    # TODO: check if contains marker, if not return HTTP 404
    # TODO: get id + corners of a marker in the image
    id, corners = output_ID.find_marker_id_in_image(openCvImage)

    # TODO: get audio description from id + corners

    response = flask.jsonify({'id': str(id)}, {'corners': str(corners)})
    # response = flask.jsonify({'audio-description': "placeholder"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
app.run()