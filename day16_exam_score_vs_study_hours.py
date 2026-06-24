#23-06-26
#Exam Score vs Study Hours

import matplotlib.pyplot as plt

study_hours = [1,2,3,4,5,6,7,8]
scores = [40,50,55,65,70,80,85,95]
plt.scatter(study_hours, scores, color='crimson')
plt.title('Study Hours vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.show()
