#07-06-26
#Age Distribution of Students
import pandas as pd
import matplotlib.pyplot as plt

ages = [18,19,20,21,22,19,20,21,18,22,20,19,21,20,18]
plt.hist(ages, bins=5, color='steelblue', edgecolor='black')
plt.title('Age Distribution of Students')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()