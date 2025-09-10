import numpy as np
import yanova


control  = np.array([1.33, 1.49, 1.43, 1.33, 1.54, 1.41, 1.49, 1.49, 1.32, 1.47])
glu2     = np.array([1.75, 1.72, 1.67, 1.69, 1.61, 1.67, 1.67, 1.75, 1.69, 1.64])
fru2     = np.array([1.72, 1.64, 1.79, 1.72, 1.75, 1.79, 1.64, 1.67, 1.75, 1.72])
glu1fru1 = np.array([1.72, 1.69, 1.72, 1.64, 1.75, 1.79, 1.72, 1.75, 1.75, 1.69])
su2      = np.array([1.61, 1.52, 1.54, 1.59, 1.56, 1.61, 1.54, 1.54, 1.61, 1.49])


result = yanova.oneway(control, glu2, fru2, glu1fru1, su2)

with np.printoptions(formatter={'float': lambda t: format(t, '8.4g')}):
    print(result)
