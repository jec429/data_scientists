import sys
import pandas as pd
import re
import nltk

nltk.download('words')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


print('Begin Process')
all_docs = pd.read_pickle("./job_full_title.pkl")
all_docs.info()

all_docs['Education_len'] = [len(x) for x in all_docs['Education']]
all_docs['Responsibilities_len'] = [len(x) for x in all_docs['Responsibilities and Achievements']]

print(all_docs['Responsibilities and Achievements'].head(10))
print(all_docs['Responsibilities_len'].head(10))

corpus = []
corpus2 = []
ps = PorterStemmer()
stem_dic = [ps.stem(s) for s in nltk.corpus.words.words()]
extra_words = ['janssen', 'cvs']

nds = 0

for rs, ds, ed in zip(all_docs['Responsibilities and Achievements'], all_docs['Grouped'], all_docs['Job Title']):
    if 'DATA SCIEN' not in ds:
        continue
    nds += 1

    for r in rs:
        r = str(r)
        review = re.sub('[^a-zA-Z]', ' ', r)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review
                  if not word in set(stopwords.words('english'))]
        for rw in review:
            if len(rw) > 1:
                corpus.append(rw)
    for r in ed:
        r = str(r)
        review = re.sub('[^a-zA-Z]', ' ', r)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review
                  if not word in set(stopwords.words('english'))]
        for rw in review:
            if len(rw) > 1:
                corpus2.append(rw)

print('N DS=', nds)
print('CORPUS')
corpus = pd.Series(corpus)
print(corpus.value_counts().head(20))

print('CORPUS2')
corpus2 = pd.Series(corpus2)
print(corpus2.value_counts().head(20))
