import random
import functools

def generator(size, function = functools.partial(random.randint, 0, 10)): 
    for i in range(size):
        yield function()