#27-06-26
#Normal Distribution Curve

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 200)
y = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
plt.plot(x, y, color='darkblue')
plt.fill_between(x, y, alpha=0.3, color='skyblue')
plt.title('Normal Distribution Curve')
plt.show()
