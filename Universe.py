from Zone import *
from Node import *
import csv


class Universe:
    zones = []

    def __init__(self):
        num_zones = 4
        self.num_nodes_move = 3
        for i in range(num_zones):
            self.zones.append(Zone(num_nodes=150))

    def node_move(self):
        node_list = []

        for i in self.zones:
            node_list += i.node_export(self.num_nodes_move)

        for i in node_list:
            check = True
            while check:
                zone = random.choice(self.zones)
                if not zone == i.zone:
                    zone.node_import(i)
                    check = False

    def export_csv(self):
        print("hi")
        num_iterations = 500
        write_data = []
        for j in range(num_iterations):
            print(str(j))
            self.node_move()
            for i in range(len(self.zones)):
                self.zones[i].iteration()
                i_data = self.zones[i].map_data()
                i_data += [i]
                write_data.append(i_data)
        print(write_data)

        csvO = open('data1.csv', 'w')
        with csvO:
            writer = csv.writer(csvO)
            writer.writerow(["Susceptible", "Infected", "Recover", "Dead", "Iter", "Zone"])
            writer.writerows(write_data)




        #
        # writer.writerow(["Susceptible", "Infected", "Recover", "Dead", "iter", "zone"])
        # num_iterations = 1000
        #
        # for j in range(num_iterations):
        #     self.node_move()
        #     for i in range(len(self.zones)):
        #         self.zones[i].iteration()
        #         i_data = self.zones[i].map_data()
        #         i_data += i
        #
        #         writer.writerow(i_data)



uni = Universe()

uni.export_csv()

