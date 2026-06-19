#18-06-26
#IPL Team Win Count

import matplotlib.pyplot as plt

teams = ['MI','CSK','RCB','KKR','SRH']
wins = [5,5,0,2,1]
plt.bar(teams, wins, color='gold', edgecolor='black')
plt.title('IPL Championship Wins')
plt.ylabel('Titles')
plt.show()
