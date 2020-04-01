from Node import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageio

import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


class Zone:

    #Init codictions
    height = 1000
    width = 1000
    numNode = 100
    node_list = []

    def __init__(self):
        for i in range(0, 100):
            print(i)
            self.node_list.append(Node(self.width, self.height))


    #each node makes a move
    def iteration(self):

        for i in self.node_list:
            i.step()
            #i.display_postion()

    #gets x/y postions for all nodes
    def gen_xy_lists(self):

        x_arr = []
        y_arr = []
        xy = []

        for i in self.node_list:
            x_arr.append(i.x)
            y_arr.append(i.y)

        return (np.array(x_arr), np.array(y_arr))

    #displays current postions of all nodes
    def map(self,i):
        co_ords = self.gen_xy_lists()

        #ax = plt.subplot(111)

        plt.clf()
        plt.ylim(0,self.height)
        plt.xlim(0,self.width)
        plt.title("Frame: "+str(i))
        plt.plot(co_ords[0], co_ords[1],'bo')

        #plt.savefig('figure.png')


        #img = imageio.imread('figure.png')
        #plt.show()
        fig = plt.gcf()

        return fig

    def mapImg(self,i):

        fig = self.map(i)
        fig.savefig('figure.png')
        img = imageio.imread('figure.png')
        return img

