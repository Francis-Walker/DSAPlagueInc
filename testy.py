

from Zone import *

zone = Zone()


img_list = []
for i in range (10):
    for j in range(100):
        zone.iteration()
    img_list.append(zone.mapImg())







