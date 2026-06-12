#12-06-26
#Temperature of a Week

import matplotlib.pyplot as plt

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temp = [32,35,33,36,34,30,31]
plt.plot(days, temp, marker='s', linestyle='--', color='orange')
plt.title('Weekly Temperature')
plt.ylabel('Temp (°C)')
plt.show()