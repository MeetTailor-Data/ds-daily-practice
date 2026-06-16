#15-06-26
#Random Walk Simulation

import matplotlib.pyplot as plt
import numpy as np

steps = np.random.choice([-1,1], size=100)
position = np.cumsum(steps)
plt.plot(position, color='purple')
plt.title('Random Walk Simulation')
plt.xlabel('Steps')
plt.ylabel('Position')
plt.show()
