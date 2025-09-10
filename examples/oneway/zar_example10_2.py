
import numpy as np
import yanova


t1 = [34, 36, 34, 35, 34]
t2 = [37, 36, 35, 37, 37]
t3 = [34, 37, 35, 37, 36]
t4 = [36, 34, 37, 34, 35]


result = yanova.oneway(t1, t2, t3, t4)

with np.printoptions(formatter={'float': lambda t: format(t, '8.4g')}):
    print(result)
