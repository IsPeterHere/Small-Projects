import math
import numpy as np




class I:

    def __init__(self,grid_size,p,offset):
        
        self.grid_size = (grid_size,grid_size)
        self.grid = np.random.choice([0,0.2,0.4,0.6,0.8,1], self.grid_size,p=p)
        #self.grid = np.zeros(self.grid_size)

        self.grid[2,2] = 1
        self.grid[2,3] = 1
        self.grid[2,4] = 1


        def suffer(v):
            return 1 if v>1 and v < 4 else 0

            #return min(0,-(0.8*v)**2)

        def birth(v):
            return v/3 if v>2 and v<4 else 0
            #return max(0,-v**2 + offset)


        self.birth = birth
        self.suffer = suffer







        




        self.grid[0,:] = 0
        self.grid[-1,:] = 0
        self.grid[:,0] = 0
        self.grid[:, -1]= 0

        self.alive = set([])

        self.neighbors = np.array([[1,-1],[1,0],[1,1],
                                    [0,-1],[0,1],
                                    [-1,-1],[-1,0],[-1,1]])


       
        for x in range(0,self.grid_size[0]):
            for y in range(0,self.grid_size[1]):
                if self.grid[x,y] > 0:
                    self.alive.add((x,y))


    def frame(self):

        if len(self.alive) ==  0:
            return None

        ARRAY_alive = np.array(list(self.alive))

        ARRAY_considered = ARRAY_alive[:,None,:] + self.neighbors
        ARRAY_considered = ARRAY_considered.reshape(-1, ARRAY_considered.shape[-1])

        i = np.where((ARRAY_considered[:, 0] >= 1) & (ARRAY_considered[:, 0] < self.grid_size[0]-1) & (ARRAY_considered[:, 1] >= 1) & (ARRAY_considered[:, 1] < self.grid_size[1]-1))
        ARRAY_considered = ARRAY_considered[i]

        ARRAY_considered = np.clip(ARRAY_considered,1,self.grid_size[0]-1)

        result_array = ARRAY_considered[:,None,:] + self.neighbors

        vls = np.sum(self.grid[result_array[:,:,0],result_array[:,:,1]],axis =1)

        for i in range(len(ARRAY_considered)):
            
            cord = tuple(ARRAY_considered[i])
            value = vls[i]

            if cord in self.alive:

                self.grid[cord] = self.suffer(value)
                
                if self.grid[cord] <= 0:
                    self.grid[cord] = 0
                    self.alive.remove(cord)

            else:

                 self.grid[cord] = self.birth(value)
                
                 if self.grid[cord] > 0:
                     self.alive.add(cord)
                