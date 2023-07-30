import math
import pandas as pd

def marker_to_text(marker_id, corners):
    orientation = math.atan2(corners[1][1]-corners[0][1],corners[1][0]-corners[0][0])
    orientation = 180*orientation/3.141592
    print(orientation)
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
   #data = pd.read_csv("marker-definitions/markers.csv")
   #result = data.loc(marker_id+1, orientation)
    data = [["ID",0,90,180,270], [0, "U4 Richtung Heiligenstadt", "Am Ende des Bahnsteigs in Fahrtrichtung Heiligenstadt befindet sich der Ausgang Schottenring mit einer auf und abwärtsführenden Fahrtreppe und einer mittig liegenden Stiege.", "U4 Richtung Hütteldorf", "Am Ende des Bahnsteigs in Fahrtrichtung Hütteldorf befindet sich der Ausgang Salztorbrücke mit einer Stiege"], [1,"U4 Richtung Hütteldorf", "Am Ende des Bahnsteigs in Fahrtrichtung Hütteldorf befindet sich der Ausgang Salztorbrücke mit einer Stiege", "U4 Richtung Heiligenstadt.", "Am Ende des Bahnsteigs in Fahrtrichtung Heiligenstadt befindet sich der Ausgang Schottenring mit einer auf und abwärtsführenden Fahrtreppe und einer mittig liegenden Stiege."], [2,"U2 Richtung Schottenring", "Am Ende des Bahnsteigs in Fahrtrichtung Seestadt befindet sich der Ausgang Herminengasse mit einer Doppelliftgruppe und einer Stiege", "U2 Richtung Aspernstraße.", "Am Ende des Bahnsteigs in Fahrtrichtung Karlsplatz befindet sich der Zugang zum Ausgang Schottenring mit einer Doppelliftgruppe und einer Stiege sowie einer Dreifachfahrtreppe zur U4."], [3,"U2 Richtung Aspernstraße", "Am Ende des Bahnsteigs in Fahrtrichtung Karlsplatz befindet sich der Zugang zum Ausgang Schottenring mit einer Doppelliftgruppe und einer Stiege sowie einer Dreifachfahrtreppe zur U4.", "U2 Richtung Schottenring", "Am Ende des Bahnsteigs in Fahrtrichtung Seestadt befindet sich der Ausgang Herminengasse mit einer Doppelliftgruppe und einer Stiege."]]
    
    result = data[marker_id+1][orientation]
    print(result)
    return result


#marker_to_text(1,[[0.1,0.0],[0.1,0.1]])