import cv2
from cv2 import aruco

def find_marker_id_in_image(image):
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_1000)
    parameters = aruco.DetectorParameters()

    # Create the Aruco detector
    detector = aruco.ArucoDetector(aruco_dict, parameters)

    # Detect the markers in the image
    corners, ids, _ = detector.detectMarkers(image)

    if ids is not None:
        return [ids[0][0], corners[0][0]]
    else:
        return None, None

