# ANOVA: Example 12.1 from Zar (fifth ed.), pages 251-255

import numpy as np
import yanova


conc = np.array(
    [[[16.3, 20.4, 12.4, 15.8, 9.5],
      [15.3, 17.4, 10.9, 10.3, 6.7]],
     [[38.1, 26.2, 32.3, 35.8, 30.2],
      [34.0, 22.8, 27.8, 25.0, 29.3]]])

result = yanova.twoway_from_data_grid(conc)
with np.printoptions(formatter={'float': lambda t: format(t, '9.5g')}):
    print(result)
