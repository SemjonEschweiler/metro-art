import cv2

def generate_marker(aruco_dict, marker_size, count):
   for marker_id in range(count):
      marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

      cv2.imwrite("marker-images/marker_{}.png".format(marker_id), marker_img)


def main():
   aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
   generate_marker(aruco_dict, 10, 5)

if __name__ == "__main__":
   main()
