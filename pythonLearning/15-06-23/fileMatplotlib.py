import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
import numpy as np

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
print('\n')
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()