
import cupy as np

class I:

    MAX = 2
    Alive = 1
    Dead = 0


    def __init__(self,grid_size,p,starve,gain):

        self.STARVE = starve
        self.GAIN  = gain
        
        self.grid_size = (grid_size,grid_size)
        self.grid = np.random.choice([0,0.2,0.4,0.6,0.8,1], self.grid_size,p=p)
        self.grid[0,:] = self.Dead
        self.grid[-1,:] = self.Dead
        self.grid[:,0] = self.Dead
        self.grid[:, -1]= self.Dead

        self.alive = set([])

        self.neighbors = np.array([[1,-1],[1,0],[1,1],
                                    [0,-1],[0,1],[0,0],
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
                
                if value >4:
                    self.grid[cord] = self.Dead
                    self.alive.remove(cord)

                elif value < 3:
                    if self.grid[cord]-self.STARVE  <= 0:
                        self.grid[cord] = self.Dead
                        self.alive.remove(cord)
                    else:
                        self.grid[cord]  = self.grid[cord]-self.STARVE
            else:
                if value > 2 and value < 3 :
                    self.grid[cord] = min(self.MAX,self.grid[cord]+self.GAIN)
                    self.alive.add(cord)
                