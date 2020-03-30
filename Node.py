import random


class Node:
    x = 0
    y = 0
    status = 'Person'
    speed = 1
    radious = 1
    max_h = 0
    max_w = 0

    def __init__(self, w, h):
        self.max_h = h
        self.max_w = w

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
