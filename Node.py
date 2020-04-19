import random
import numpy as np
import math
from enum import Enum


class Node:
    class Status(Enum):
        Susceptible = 'S'
        Infected = 'I'
        Recovered = 'R'
        Dead = 'D'

    __x = 0
    __y = 0
    __status = Status.Susceptible
    speed = 2
    __rad = 7
    max_h = 0
    max_w = 0
    inf_iter = None
    rec_iter = None

    def __init__(self, zone):
        self.move = True
        self.theta = random.randint(0, 360)
        self.speed = 1
        self.zone = zone
        self.max_h = self.zone.height
        self.max_w = self.zone.width
        self.__rad = zone.node_r
        self.infected_duration = zone.node_inf_dur

        self.__x = random.randint(1, self.max_w - 1)
        self.__y = random.randint(1, self.max_h - 1)

    def zone_update(self, zone):
        self.zone = zone
        self.__x = zone.width // 2
        self.__y = zone.height // 2

    def step(self):
        # move = True
        if self.move:

            x = round(self.__x + (self.speed * math.cos(math.radians(self.theta))))
            y = round(self.__y + (self.speed * math.sin(math.radians(self.theta))))

            # print(str(x)+","+str(y))
            check = False
            if x > self.zone.width:
                self.__x = self.zone.width - 1
                check = True
            elif x < 1:
                self.__x = 1
                check = True
            else:
                self.__x = x

            if y > self.zone.height:
                self.__y = self.zone.height - 1
                check = True
            elif y < 1:
                self.__y = 1
                check = True
            else:
                self.__y = y

            if not check:
                self.theta += random.randint(-45, 45)
            else:
                self.theta += 180

        else:

            # for each node assigns a direction and checks if direction is possible. if so moves node accordingly
            direction = random.randint(1, 4)
            usage_dict = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

            # print(usage_dict[direction])

            if (self.__x == 1 and direction == 1):
                pass
            elif (self.__x == self.max_w - 1 and direction == 2):
                pass
            elif (self.__y == 1 and direction == 3):
                pass
            elif (self.__y == self.max_h - 1 and direction == 4):
                pass
            else:
                self.__x += usage_dict[direction][0]
                self.__y += usage_dict[direction][1]

    def display_postion(self):
        print("x " + str(self.__x) + " y " + str(self.__y))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def rad(self):
        return self.__rad

    @property
    def status(self):
        return self.__status

    def get_inf(self):
        if self.__status == self.Status.Infected:
            return True
        else:
            return False

    def get_rec(self):
        if self.__status == self.Status.Recovered or self.__status == self.Status.Dead:
            return True
        else:
            return False

    def get_dead(self):
        if self.__status == self.Status.Dead:
            return True
        else:
            return False

    def set_inf(self, f_t):
        if f_t:
            self.__status = self.Status.Infected

    def set_rec(self, f_t):
        if f_t:
            self.__status = self.Status.Recovered
        else:
            self.__status = self.Status.Dead

    def exposed(self, first=False):

        test_int = random.randint(0, 100)
        if test_int < self.zone.prob_inf:
            first = True

        if first:
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
