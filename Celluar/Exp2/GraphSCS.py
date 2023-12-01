import matplotlib.pyplot as plt
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


#-------------------------------------------

#test settings
from_ = 0.0
to = 1
number_of_steps = 30

n_tests = 15
test_length = 50

offset = 0

#-----------------------------------------



svs = []
thngs_alive_conuts = []



for i in range(number_of_steps):
	thing = offset =  from_ + i*((to-from_)/number_of_steps)

	sim = SIM.I(grid_size,d,offset)


	things_alive = 0
	for loop1 in range(n_tests):
		for loop2 in range(test_length):
		
			sim.frame()
		
		things_alive += len(sim.alive) 

	things_alive = things_alive/n_tests
	
	svs.append(thing)
	thngs_alive_conuts.append(things_alive)

	print(i)




plt.scatter(svs, thngs_alive_conuts)
plt.show()