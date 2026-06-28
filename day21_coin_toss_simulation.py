#28-06-26
#Coin Toss Simulation

import matplotlib.pyplot as plt
import numpy as np

results = np.random.choice(['Heads','Tails'], size=1000)
counts = [np.sum(results=='Heads'), np.sum(results=='Tails')]
plt.bar(['Heads','Tails'], counts, color=['gold','silver'])
plt.title('Coin Toss - 1000 Times')
plt.ylabel('Count')
plt.show()
