#25-06-26
#Comparing Two Students' Marks

import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math','Science','English','History']
meet = [80,85,70,75]
raj = [70,80,85,65]
x = np.arange(len(subjects))
plt.bar(x-0.2, meet, 0.4, label='Meet', color='steelblue')
plt.bar(x+0.2, raj, 0.4, label='Raj', color='coral')
plt.xticks(x, subjects)
plt.title('Marks Comparison')
plt.legend()
plt.show()
