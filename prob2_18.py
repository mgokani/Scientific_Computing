import math
import numpy as np


# function to compute v as a function of t
def velocity(t):
    if 0 <= t <= 10:
        return 11*t**2 - 5*t
    elif 10 <= t <= 20:
        return 1100 - 5*t
    elif 20 <= t <= 30:
        return 50*t + 2*(t-20)**2
    elif t > 30:
        return 1520*math.exp(-0.2*(t-30))
    else:
        return 0

# print a table showing different values of velocity at different time values
for time in np.arange(-5, 50.5, 0.5):
    print("time, velocity = {}, {}".format(time, velocity(time)))
