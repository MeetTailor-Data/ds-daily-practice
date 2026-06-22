#21-06-26
#Subject-wise Average Marks

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Subject':['Math','Science','English','History'],
                   'Avg':[75,82,68,71]})
df.plot(kind='bar', x='Subject', y='Avg', legend=False, color='teal')
plt.title('Subject-wise Average Marks')
plt.ylabel('Marks')
plt.show()
