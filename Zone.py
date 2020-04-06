from Node import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageio

import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def is_within(node1, node2):
    x1 = node1.get_x()
    y1 = node1.get_y()
    x2 = node2.get_x()
    y2 = node2.get_y()

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    print(type(distance))
    print(type(node1.get_rad()))
    if distance > node1.get_rad():
        return False
    else:
        return True


def is_within_xy(x1, y1, x2, y2, r):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if distance > r:
        return False
    else:
        return True


class Zone:
    # Init codictions
    node_r = 5
    node_inf_dur = (14, 48)
    current_iteration = 0
    height = 100
    width = 100
    numNode = 200
    sus_list = []
    inf_list = []
    rec_list = []
    prob_inf = 30
    prob_safely_recover = 50

    def __init__(self):
        for i in range(0, self.numNode):
            self.sus_list.append(Node(self))

        ran_index = random.randint(0, len(self.sus_list) + 1)
        node = self.sus_list.pop(ran_index)
        # print(node.status)
        node.infected()
        # print(node.status)

        self.inf_list.append(node)

    # each node makes a move
    def iteration(self):

        infection_map = {}
        swap_index = []

        # check infected list and map infection zone
        for i in self.inf_list:
            if i.can_recover():
                i.recovered()

            if i.get_rec():
                if not i.get_dead():
                    i.step()

                swap_index.append(self.inf_list.index(i))
            else:
                i.step()

                for x in range(i.get_x() - i.get_rad(), i.get_x() + i.get_rad()):
                    for y in range(i.get_y() - i.get_rad(), i.get_y() + i.get_rad()):
                        if is_within_xy(i.get_x(), i.get_y(), x, y, i.get_rad()):
                            # Check logic
                            infection_map["" + str(x) + "," + str(y)] = True

        swap_index.sort()
        swap_index.reverse()
        # Swap
        if self.inf_list:
            for index_to_remove in swap_index:
                node = self.inf_list.pop(index_to_remove)
                self.rec_list.append(node)

        # node in infection map exposed and populate swap indexs
        swap_index = []

        for i in range(len(self.sus_list)):

            self.sus_list[i].step()
            # check logic
            key_test = "" + str(self.sus_list[i].get_x()) + "," + str(self.sus_list[i].get_y())

            if key_test in infection_map:
                self.sus_list[i].exposed()
                if self.sus_list[i].get_inf():
                    swap_index.append(i)

        # Reverses order top avoid integrity lapse
        swap_index.sort()
        swap_index.reverse()
        # Swap
        if self.sus_list:
            for index_to_remove in swap_index:
                node = self.sus_list.pop(index_to_remove)
                self.inf_list.append(node)

            # i.display_postion()
        for i in self.rec_list:
            if not i.get_dead():
                i.step()
        self.current_iteration += 1

    # gets x/y postions for all nodes
    def gen_xy_lists(self):

        s_x_arr = []
        s_y_arr = []
        i_x_arr = []
        i_y_arr = []
        i_r_arr = []
        r_x_arr = []
        r_y_arr = []
        d_x_arr = []
        d_y_arr = []
        xy = []

        for i in self.sus_list:
            s_x_arr.append(i.get_x())
            s_y_arr.append(i.get_y())

        for i in self.inf_list:
            i_x_arr.append(i.get_x())
            i_y_arr.append(i.get_y())
            i_r_arr.append(i.get_rad())

        for i in self.rec_list:
            if i.get_dead():
                d_x_arr.append(i.get_x())
                d_y_arr.append(i.get_y())
            else:
                r_x_arr.append(i.get_x())
                r_y_arr.append(i.get_y())

        return (np.array(s_x_arr), np.array(s_y_arr)), (np.array(i_x_arr), np.array(i_y_arr), np.array(i_r_arr)), (
            np.array(r_x_arr), np.array(r_y_arr)), (np.array(d_x_arr), np.array(d_y_arr))
        # displays current postions of all nodes

    # makes plots
    def map(self):
        co_ords = self.gen_xy_lists()

        # ax = plt.subplot(111)

        plt.clf()
        plt.ylim(0, self.height)
        plt.xlim(0, self.width)
        plt.title("Frame:" + str(self.current_iteration) + " Nodes:" + str(self.numNode) + " Inf_Nodes: " + str(
            len(self.inf_list))
                  + " Inf_prob:" + str(self.prob_inf))
        plt.plot(co_ords[0][0], co_ords[0][1], 'bo',label="Susceptible")
        plt.plot(co_ords[1][0], co_ords[1][1], 'ro',label="Infected")
        plt.plot(co_ords[2][0], co_ords[2][1], 'ko',label="Recovered")
        plt.plot(co_ords[3][0], co_ords[3][1], 'kx',label="Dead")
        plt.axis("off")
        plt.legend(loc="upper right")
        ax = plt.gca()
        for i in range(len(co_ords[1][0])):
            circle = plt.Circle((co_ords[1][0][i], co_ords[1][1][i]), co_ords[1][2][i], color='r', fill=False)
            ax.add_artist(circle)

        # plt.savefig('figure.png')

        # img = imageio.imread('figure.png')

        fig = plt.gcf()

        return fig

    # returns images of plots
    def map_img(self):

        fig = self.map()
        fig.savefig('figure.png')
        img = imageio.imread('figure.png')
        return img

    # return data of current iteration
    def map_data(self):
        size_s = len(self.sus_list)
        size_i = len(self.inf_list)

        size_r = 0
        size_d = 0
        for i in self.rec_list:
            if i.get_dead():
                size_d += 1
            else:
                size_r += 1

        return size_s, size_i, size_r, size_d
