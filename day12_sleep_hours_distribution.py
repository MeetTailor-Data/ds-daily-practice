#19-06-26
#Sleep Hours Distribution

import matplotlib.pyplot as plt
import numpy as np

sleep = np.random.normal(loc=7, scale=1, size=200)
plt.hist(sleep, bins=10, color='slateblue', edgecolor='white')
plt.title('Sleep Hours Distribution')
plt.xlabel('Hours')
plt.show()
