from Zone import *

zone = Zone()

file = open("data.txt","w")
file.write("\ninfection probability "+str(zone.prob_inf))
file.write("\ninfected duration min:"+str(zone.node_inf_dur[0]) + " max: "+str(zone.node_inf_dur[0]))
file.write("\nrecovered safely probability "+str(zone.prob_safely_recover))
file.write("\n_______________________________________________________")
file.write("\nTotal,Susceptible,Infected,Recovered,Dead")
for i in range (400):

    zone.iteration()
    sus, inf, rec, dead = zone.map_data()
    file.write("\n"+str(zone.numNode)+","+str(sus)+","+str(inf)+","+str(rec)+","+str(dead))
file.close()