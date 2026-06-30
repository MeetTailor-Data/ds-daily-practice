#30-06-26
#GDP Growth of India

import matplotlib.pyplot as plt

years = [2018,2019,2020,2021,2022,2023]
gdp = [6.5,6.0,-7.3,8.7,7.2,6.3]
plt.plot(years, gdp, marker='o', color='green')
plt.axhline(0, color='red', linestyle='--')
plt.title('India GDP Growth Rate (%)')
plt.ylabel('Growth %')
plt.show()
