import imageio

from Zone import *

zone = Zone()


img_list = []
for i in range (100):

    zone.iteration()
    img_list.append(zone.map_img())

imageio.mimsave("imgChache/"+str(zone.prob_inf)+"%.gif", img_list)