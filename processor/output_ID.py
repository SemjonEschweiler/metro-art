import cv2
from cv2 import aruco

def detect_aruco_ids_in_image(image):
    # Load the predefined dictionary
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

    # Initialize the detector parameters using default values
    parameters = aruco.DetectorParameters()

    # Check if image is loaded
    if image is None:
        print(f'Failed to load image from path: {image}')
        return

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create the Aruco detector
    detector = aruco.ArucoDetector(aruco_dict, parameters)

    # Detect the markers in the image
    corners, ids, _ = detector.detectMarkers(grayscale)
    print(corners)

    if ids is not None:
        return [ids[0], corners]
    else:
        return None, None

