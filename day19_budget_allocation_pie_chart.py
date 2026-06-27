#26-06-26
#Budget Allocation Pie Chart

import matplotlib.pyplot as plt

categories = ['Food','Rent','Transport','Entertainment','Savings']
amounts = [3000,8000,1500,1000,2500]
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Budget Allocation')
plt.show()
