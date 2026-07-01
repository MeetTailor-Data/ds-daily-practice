#01-07-26
#Dice Roll Simulation

import matplotlib.pyplot as plt
import numpy as np

rolls = np.random.randint(1, 7, size=600)
plt.hist(rolls, bins=6, range=(0.5,6.5), color='tomato', edgecolor='black', rwidth=0.8)
plt.title('Dice Roll - 600 Times')
plt.xlabel('Dice Face')
plt.ylabel('Frequency')
plt.show()
