from collections import defaultdict
from typing import KeysView

class Map:

    def __init__(self):

        self.__map = defaultdict(lambda:0)
        
        self.__updates_made = {}

    def set(self,cord,value):

        self.__updates_made[cord] = self.__map[cord]
        self.__map[cord] = value

    def remove(self,cord):
        self.__updates_made[cord] = self.__map[cord]
        del self.__map[cord]

    def get(self,cord):

        if cord == "all keys":
            return self.__map.keys()
        return self.__map[cord]

    def clear(self):
        for k,v in self.__map.items:
           if v != " " :
               self.__updates_made[k] = v
        
        self.__map = defaultdict(" ")


    def get_update(self, cord):
        if cord == "all items":
            return self.__updates_made.items()
        return self.__updates_made[cord]

    def clear_updates(self):
        self.__updates_made = {}
