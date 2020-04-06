import random
import numpy as np


class Node:
    x = 0
    y = 0
    status = 'S'
    speed = 1
    rad = 7
    max_h = 0
    max_w = 0
    inf_iter = None
    rec_iter = None

    def __init__(self, zone):
        self.zone = zone
        self.max_h = zone.width
        self.max_w = zone.height
        self.rad = zone.node_r
        self.infected_duration = zone.node_inf_dur

        self.x = random.randint(1, self.max_w - 1)
        self.y = random.randint(1, self.max_h - 1)

    def step(self):
        # for each node assigns a direction and checks if direction is possible. if so moves node accordingly
        direction = random.randint(1, 4)
        usage_dict = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

        # print(usage_dict[direction])

        if (self.x == 1 and direction == 1):
            pass
        elif (self.x == self.max_w - 1 and direction == 2):
            pass
        elif (self.y == 1 and direction == 3):
            pass
        elif (self.y == self.max_h - 1 and direction == 4):
            pass
        else:
            self.x += usage_dict[direction][0]
            self.y += usage_dict[direction][1]

    def display_postion(self):
        print("x " + str(self.x) + " y " + str(self.y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.x = new_y

    def get_rad(self):
        return self.rad

    def set_rad(self, new_rad):
        self.rad = new_rad

    def get_inf(self):
        if self.status == 'I':
            return True
        else:
            return False

    def get_rec(self):
        if self.status == 'R' or self.status == 'D':
            return True
        else:
            return False

    def get_dead(self):
        if self.status == 'D':
            return True
        else:
            return False

    def set_inf(self, f_t):
        if f_t:
            self.status = 'I'

    def set_rec(self, f_t):
        if f_t:
            self.status = 'R'
        else:
            self.status = 'D'

    def exposed(self):
        test_int = random.randint(0, 100)
        if test_int < self.zone.prob_inf:
            self.set_inf(True)
            self.inf_iter = self.zone.current_iteration
            self.rec_iter = self.zone.current_iteration + random.randint(14 * 2, 42 * 2)

    def infected(self):
        self.set_inf(True)
        self.inf_iter = self.zone.current_iteration
        self.rec_iter = self.zone.current_iteration + random.randint(self.infected_duration[0],
                                                                     self.infected_duration[1])

    def recovered(self):
        test_int = random.randint(0, 100)
        if test_int < self.zone.prob_safely_recover:
            self.set_rec(True)
        else:
            self.set_rec(False)

    def can_recover(self):
        if self.zone.current_iteration == self.rec_iter:
            return True
        else:
            return False
