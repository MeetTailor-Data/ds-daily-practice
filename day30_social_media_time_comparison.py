#07-07-26
#Social Media Time Comparison

import matplotlib.pyplot as plt
import numpy as np

platforms = ['Instagram','YouTube','Twitter','Snapchat']
weekday = [1.5,2.0,0.5,0.8]
weekend = [3.0,4.5,1.0,1.5]
x = np.arange(len(platforms))
plt.bar(x-0.2, weekday, 0.4, label='Weekday', color='steelblue')
plt.bar(x+0.2, weekend, 0.4, label='Weekend', color='coral')
plt.xticks(x, platforms)
plt.title('Social Media Time (Hours/Day)')
plt.legend()
plt.show()
