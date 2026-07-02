#02-07-26
#Top Programming Languages

import matplotlib.pyplot as plt

languages = ['Python','JavaScript','Java','C++','Rust']
popularity = [30,25,20,15,10]
plt.barh(languages, popularity, color='cornflowerblue')
plt.title('Top Programming Languages 2024')
plt.xlabel('Popularity %')
plt.show()
