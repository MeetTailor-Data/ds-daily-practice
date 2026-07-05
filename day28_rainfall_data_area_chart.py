#05-07-26
#Rainfall Data - Area Chart

import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun']
rain = [10,5,20,80,150,200]
plt.fill_between(months, rain, color='deepskyblue', alpha=0.6)
plt.plot(months, rain, color='navy')
plt.title('Monthly Rainfall (mm)')
plt.ylabel('Rainfall')
plt.show()
