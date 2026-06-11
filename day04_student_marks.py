#11-06-26
#Student Marks Bar Chart

import matplotlib.pyplot as plt

students = ['Meet','Raj','Priya','Ankit','Sara']
marks = [85,72,90,65,88]
plt.bar(students, marks, color='mediumseagreen')
plt.title('Student Marks')
plt.ylabel('Marks')
plt.ylim(0,100)
plt.show()
