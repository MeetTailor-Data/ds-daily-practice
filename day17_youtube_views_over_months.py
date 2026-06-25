#24-06-26
#YouTube Views Over Months

import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun']
views = [1200,1800,1500,2200,2800,3500]
plt.fill_between(months, views, color='skyblue', alpha=0.5)
plt.plot(months, views, color='blue')
plt.title('YouTube Views Over Months')
plt.show()
