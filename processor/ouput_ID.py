import cv2
from cv2 import aruco
print(dir(aruco))
import os

def detect_aruco_ids_in_dir(directory):
    # Load the predefined dictionary
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

    # Initialize the detector parameters using default values
    parameters = aruco.DetectorParameters_create()

    # Iterate over every file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG file
        if filename.endswith('.png'):
            # Get the full path of the file
            image_path = os.path.join(directory, filename)
            
            # Load the image
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect the markers in the image
            corners, ids, rejectedImgPoints = aruco.detectMarkers(grayscale, aruco_dict, parameters=parameters)

            # If at least one marker detected
            if len(corners) > 0:
                print(f'Detected IDs in {filename}:', ids)
                # draw a square around the markers
                cv2.aruco.drawDetectedMarkers(image, corners, ids)
                
                # Display the resulting frame
                cv2.imshow('frame', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

# Call the function providing the path to your directory
detect_aruco_ids_in_dir('Aruco_Markers_50mm')
