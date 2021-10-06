import random
import functools

class IteratorLL:
    def __init__(self, size, function = functools.partial(random.randint, 0, 10)):
        self.__curr_index = 0
        self.__size = size
        self.__function = function
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.__curr_index >= self.__size:
            raise StopIteration
        value = self.__function()
        self.__curr_index += 1
        return value



