import sys
import matplotlib
# matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["20.07", "21.07", "24.07", "24.07", "29.07", "29.07", "29.07", "02.08", "04.08", "10.08", "13.08", "13.08", "17.08"])
y = np.array([2630, 9936, 2140, 2995, 4892, 2467, 2344, 5109, 10057, 6296, 3207, 5411, 1982])

plt.bar(x, y, color = "#4CAF50")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
