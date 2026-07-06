#06-07-26
#Grade Distribution - Pie

import matplotlib.pyplot as plt

grades = ['A','B','C','D','F']
students = [10,25,30,20,5]
plt.pie(students, labels=grades, autopct='%1.0f%%', colors=['green','blue','yellow','orange','red'])
plt.title('Class Grade Distribution')
plt.show()
