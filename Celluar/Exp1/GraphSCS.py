import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SIM

#----------------------------------------

#world settings
grid_size = 200

D0 = 0.6
D1_5 = 0.1
D2_5 = 0
D3_5 = 0
D4_5 = 0.1
D1 = 0.2
d = (D1,D4_5,D3_5,D2_5,D1_5,D0)

#s = 0.03
g = 0.8


#-------------------------------------------

#test settings
from_ = 0.0
to = 0.2
number_of_steps = 30
#-----------------------------------------



svs = []
thngs_alive_conuts = []



for i in range(number_of_steps):
	thing = s =  from_ + i*((to-from_)/number_of_steps)

	sim = SIM.I(grid_size,d,s,g)

	for loop in range(10):
		
		sim.frame()
		
	things_alive = len(sim.alive) 
	
	svs.append(thing)
	thngs_alive_conuts.append(things_alive)

	print(i)




plt.scatter(svs, thngs_alive_conuts)
plt.show()