import math
import csv

def get_audio_description_at_marker(marker_id, corners):
    orientation = math.atan2(corners[1][1]-corners[0][1],corners[1][0]-corners[0][0])
    orientation = 180*orientation/3.141592
    if orientation >= -10 and orientation <= 10:
        orientation = 0
    elif orientation >= 80 and orientation <= 100:
        orientation = 270
    elif orientation >= 170 and orientation <= 181 or orientation >=-181 and orientation <=-170 :
        orientation = 180
    elif orientation >= -100 and orientation <= -80:
        orientation = 90
    else:
        return "Unknown direction"

    count = 0
    markers = {}
    with open('marker-definitions/markers.csv', mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)

        for rows in reader:
            count += 1
            markers[rows[0]] = { '0': rows[1], '90': rows[2], '180': rows[3], '270': rows[4]}

    if (marker_id > count):
        return None

    return markers[str(marker_id)][str(orientation)]
