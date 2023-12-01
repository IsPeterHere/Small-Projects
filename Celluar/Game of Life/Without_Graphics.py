import SIM as SIM
import cProfile

grid_size = (1000,1000)
p = (0.1,0.9)

Game = SIM.Game(grid_size,p)

def main():
	for i in range (10):
		Game.frame()

cProfile.run('main()')

print("done")