
import numpy as np

class Game:
    Alive = 1
    Dead = 0

    def __init__(self,grid_size,initial_density):
        

        self.grid = np.random.choice([self.Alive, self.Dead], grid_size,p=(initial_density,1-initial_density))
        self.grid[0,0] = self.Alive

        self.alive = set([])


        self.grid_size = grid_size


        points = set([])
        for x in range(0,grid_size[0]):
            for y in range(0,grid_size[1]):
                if self.grid[x,y]:
                    self.alive.add((x,y))
                points.add((x,y))



        self.dict_of_points = {k:set([(k[0]+1,k[1]-1),(k[0]+1,k[1]  ),(k[0]+1,k[1]+1),
                                  (k[0]  ,k[1]-1),(k[0]  ,k[1]+1),(k[0]  ,k[1]  ),
                                  (k[0]-1,k[1]-1),(k[0]-1,k[1]),(k[0]-1,k[1]+1)]) for k in points}

    def frame(self):

        if len(self.alive) ==  0:
            exit()


        de = []
        al = []

        for a in self.alive:
            n = self.dict_of_points[a]
            count = len(self.alive.intersection(a))

            
            for i in n:
                 if i[0] > 0 and i[0] < self.grid_size[0] and i[1] > 0 and i[1] < self.grid_size[0]:
                    if len(self.alive.intersection(self.dict_of_points[i])) == 4:
                        self.grid[i] = self.Alive
                        al.append(i)
            
            
            if count != 3 and count != 4:
                self.grid[a] = self.Dead
                de.append(a)

        for i in de:
            self.alive.remove(i)

        for i in al:
            self.alive.add(i)

                