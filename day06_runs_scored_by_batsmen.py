#13-06-26
#Runs Scored by Batsmen

import matplotlib.pyplot as plt

players = ['Rohit','Virat','Gill','Pant','Hardik']
runs = [75,90,55,40,65]
plt.barh(players, runs, color='royalblue')
plt.title('Runs Scored by Batsmen')
plt.xlabel('Runs')
plt.show()
