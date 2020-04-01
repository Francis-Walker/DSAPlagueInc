import imageio

from Zone import *

zone = Zone()


img_list = []
for i in range (1000):

    zone.iteration()
    img_list.append(zone.mapImg(i))

imageio.mimsave('imgChache/movie.gif', img_list)