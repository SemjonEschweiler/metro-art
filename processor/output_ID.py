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
    corners, ids, rejectedImgPoints = detector.detectMarkers(grayscale)

    # If at least one marker detected
    if len(corners) > 0:
        print(f'Detected IDs in {image}:', ids)
        # draw a square around the markers
        cv2.aruco.drawDetectedMarkers(image, corners, ids)
        
        # Display the resulting frame
        cv2.imshow('frame', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # No Markers in Image
        return None

