import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import numpy as np
from nltk.tokenize import RegexpTokenizer

nltk.download('words')
nltk.download('stopwords')

df = pd.read_excel(open('DataAnalyticsEEs-Updated.3.xlsx', 'rb'), sheet_name='Email')
df = df.replace(np.nan, '')

words_ns = []
ps = PorterStemmer()

words = []
print('Read quals')
tokenizer = RegexpTokenizer(r'\w+')
for q in df['Int Qual']:
    # print(q)
    # for w in q.split(' '):
    #    words.append(w)
    words += tokenizer.tokenize(q.lower())

print('Done reading')
print(len(words))
# words_ns = [ps.stem(word) for word in words if not word in set(stopwords.words('english'))]
ignore_words = set(stopwords.words('english'))
ignore_words.add('required')
ignore_words.add('preferred')
ignore_words.add('johnson')
ignore_words.add('must')
ignore_words.add('demonstrated')
ignore_words.add('experience')
words_ns = [word for word in words if word not in ignore_words]

sns.set(rc={'figure.figsize': (11.7, 8.27)})
sns.set_style('darkgrid')
nlp_words = nltk.FreqDist(words_ns)
nlp_words.plot(20)
