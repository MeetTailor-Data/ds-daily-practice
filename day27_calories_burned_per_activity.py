#04-07-26
#Calories Burned Per Activity

import matplotlib.pyplot as plt

activities = ['Running','Cycling','Swimming','Walking','Yoga']
calories = [500,400,450,250,200]
plt.bar(activities, calories, color='salmon')
plt.title('Calories Burned Per Activity')
plt.ylabel('Calories')
plt.show()
