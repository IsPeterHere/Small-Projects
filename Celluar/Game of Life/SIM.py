
import numpy as np

class Game:
    Alive = 1
    Dead = 0

    def __init__(self,grid_size,initial_density):
        

        self.grid = np.random.choice([self.Alive, self.Dead], grid_size,p=(initial_density,1-initial_density))
        self.grid[0,0] = self.Alive

        self.alive = set([])

        self.neighbors = np.array([[1,-1],[1,0],[1,1],
                                    [0,-1],[0,1],[0,0],
                                    [-1,-1],[-1,0],[-1,1]])


        self.grid_size = grid_size


       
        for x in range(1,grid_size[0]-1):
            for y in range(1,grid_size[1]-1):
                if self.grid[x,y]:
                    self.alive.add((x,y))

    def frame(self):

        if len(self.alive) ==  0:
            exit()

        ARRAY_alive = np.array(list(self.alive))
        result_array = ARRAY_alive[:,None,:] + self.neighbors
        result_array = result_array.reshape(-1, result_array.shape[-1])

        indices = np.where((result_array[:, 0] >= 0) & (result_array[:, 0] < self.grid_size[0]) & (result_array[:, 1] >= 0) & (result_array[:, 1] < self.grid_size[1]))

        result_array = result_array[indices]

        unique, counts = np.unique(result_array, return_counts=True,axis=0)

        for i in range(len(unique)):
            
            cord = tuple(unique[i])
            value = counts[i]
            

            if cord in self.alive:
                
                if value != 3 and value != 4:
                    self.grid[cord] = self.Dead
                    self.alive.remove(cord)
            else:
                if value == 3:
                    self.grid[cord] = self.Alive
                    self.alive.add(cord)
                