#14-06-26
#Correlation Heatmap (Mini)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({'Math':[80,90,70],'Science':[85,88,75],'English':[60,70,65]})
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Subject Correlation')
plt.show()
