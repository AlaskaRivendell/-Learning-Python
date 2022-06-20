from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("AliceText") as f:
    text = f.read()

wordcloud = WordCloud(width=1920, height=1200)
STOPWORDS.add('said')
STOPWORDS.add('s')

wordcloud.generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()