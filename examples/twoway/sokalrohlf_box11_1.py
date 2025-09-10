# ANOVA example from Sokal & Rohlf (fourth ed.), Box 11.1

import numpy as np
import yanova


consumption = np.array(
    [[[709, 679, 699],
      [592, 538, 476]],
     [[657, 594, 677],
      [508, 505, 539]]])

result = yanova.twoway_from_data_grid(consumption)
with np.printoptions(formatter={'float': lambda t: format(t, '9.5g')}):
    print(result)
