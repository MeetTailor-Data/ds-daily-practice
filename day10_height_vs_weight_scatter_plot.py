#17-06-26
#Height vs Weight Scatter Plot

import matplotlib.pyplot as plt

height = [150,160,170,175,180,165,155]
weight = [50,60,70,75,80,65,55]
plt.scatter(height, weight, color='darkorange')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
