#29-06-26
#Word Count in a Sentence

import matplotlib.pyplot as plt

sentence = "data science is fun and data is the new oil"
words = {}
for word in sentence.split():
    words[word] = words.get(word, 0) + 1
plt.bar(words.keys(), words.values(), color='mediumorchid')
plt.title('Word Frequency')
plt.xticks(rotation=45)
plt.show()
