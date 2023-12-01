
from Utils import *
import numpy as np
from collections import defaultdict

class Game():

    def __init__(self,grid_size):
        self.grid_size = grid_size

        self.map = Map()

        self.grid = np.full(grid_size,0)
        self.grid[0,0] = 1

        ran = np.random.choice([True, False], grid_size)
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                if ran[x,y]:
                    self.set_map_element_alive((x,y))
        

    def set_map_element_alive(self,cord):
        if cord[0] > 0 and cord[0] < self.grid_size[0] and cord[1] > 0 and cord[1] < self.grid_size[0]:
            self.map.set(cord,1)

    def set_map_element_dead(self,cord):
        if cord[0] > 0 and cord[0] < self.grid_size[0] and cord[1] > 0 and cord[1] < self.grid_size[0]:
            self.map.remove(cord)
    
    def __update_grid(self):
        for cord,value in self.map.get_update("all items"):
            print(cord,value)
            if value == 0:
                self.grid[cord] = 1

            elif value == 1:
                self.grid[cord] = 0

            else:
                raise NameError("please only have 1s & zeros on the map")

        self.map.clear_updates()

    def __do_proccess(self):
        count_relevant_squares = defaultdict(lambda:0)
        
        for cord in self.map.get("all keys"):
            count_relevant_squares[cord] += -10
            for x in [-1,0,1]:
                for y in [-1,0,1]:

                    count_relevant_squares[(cord[0]+x,cord[1]+y)] += 1
    
        for cord,value in count_relevant_squares.items():

            if value == 2:
                    self.set_map_element_alive(cord)

            else:
                if value < 0:
                
                    if value == -9 or value == -7:
                        pass
                    else:
                        self.set_map_element_dead(cord)

    def frame(self):
        self.__update_grid()

        self.__do_proccess()











