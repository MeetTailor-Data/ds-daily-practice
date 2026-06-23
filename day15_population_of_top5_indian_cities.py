#22-06-26
#Population of Top 5 Indian Cities

import matplotlib.pyplot as plt

cities = ['Mumbai','Delhi','Bangalore','Hyderabad','Surat']
pop = [20.7,32.9,13.2,10.5,7.8]
plt.bar(cities, pop, color='steelblue')
plt.title('Population of Top 5 Cities (Millions)')
plt.ylabel('Population')
plt.show()
