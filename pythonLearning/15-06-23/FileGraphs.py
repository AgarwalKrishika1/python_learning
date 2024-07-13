import sys
import matplotlib
#matplotlib.use('Agg')  used to save graph and not print it
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 10, mec = 'r', mfc = 'y', ls = ':', c = 'g', lw = 10)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
