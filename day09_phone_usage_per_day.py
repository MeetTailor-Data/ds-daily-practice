#16-06-26
#Phone Usage Per Day

import matplotlib.pyplot as plt

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
hours = [3,4,2,5,4,7,6]
plt.bar(days, hours, color='coral')
plt.title('Phone Usage Per Day')
plt.ylabel('Hours')
plt.show()
