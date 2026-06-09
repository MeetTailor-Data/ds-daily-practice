#09-06-26
#Monthly Expenses Tracker

import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun']
expenses = [5000,4500,6000,5500,7000,6500]
plt.plot(months, expenses, marker='o', color='tomato')
plt.title('Monthly Expenses')
plt.ylabel('Amount (₹)')
plt.show()