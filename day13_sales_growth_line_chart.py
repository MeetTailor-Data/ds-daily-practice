#20-06-26
#Sales Growth Line Chart

import matplotlib.pyplot as plt

years = [2019,2020,2021,2022,2023,2024]
sales = [10000,8000,12000,15000,18000,22000]
plt.plot(years, sales, marker='o', color='green')
plt.title('Yearly Sales Growth')
plt.ylabel('Sales (₹)')
plt.show()
