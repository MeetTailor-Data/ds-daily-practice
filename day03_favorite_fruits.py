#10-06-26
# Favorite Fruits Survey

import matplotlib.pyplot as plt

fruits = ['Mango','Apple','Banana','Grapes','Orange']
votes = [35,25,20,10,10]
plt.pie(votes, labels=fruits, autopct='%1.1f%%')
plt.title('Favorite Fruits Survey')
plt.show()