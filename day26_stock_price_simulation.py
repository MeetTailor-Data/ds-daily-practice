#03-07-26
#Stock Price Simulation

import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
price = 100 + np.cumsum(np.random.randn(30))
plt.plot(days, price, color='darkgreen')
plt.title('Simulated Stock Price - 30 Days')
plt.xlabel('Day')
plt.ylabel('Price (₹)')
plt.show()
