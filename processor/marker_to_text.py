import math
import pandas as pd

def marker_to_text(marker_id, corners):
    orientation = math.atan2(corners[1][1]-corners[0][1],corners[1][0]-corners[0][0])
    orientation = 180*orientation/3.141592
    #print(orientation)
    if orientation >= -10 and orientation <= 10:
        #orientation = 0
        orientation = 1
    elif orientation >= 80 and orientation <= 100:
        #orientation = 270
        orientation = 2
    elif orientation >= 170 and orientation <= 181 or orientation >=-181 and orientation <=-170 :
        #orientation = 180
        orientation = 3
    elif orientation >= -100 and orientation <= -80:
        #orientation = 90
        orientation = 4
    else:
        print("None")
        return None
    print(orientation)
    data = pd.read_csv("marker-definitions/markers.csv")
    #print(data)
    result = data.loc[(marker_id+1)][orientation]
    #result = data[marker_id+1][orientation]
    print(result)
    return result


#marker_to_text(1,[[0.1,0.0],[0.1,0.1]])