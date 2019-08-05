import sys
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('words')
nltk.download('stopwords')

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

    if len(rs) == 0:
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
print(corpus.value_counts(normalize=True).head(20))

print('CORPUS2')
corpus2 = pd.Series(corpus2)
print(corpus2.value_counts(normalize=True).head(20))

values = corpus.value_counts(normalize=True).keys().tolist()
counts = corpus.value_counts(normalize=True).tolist()

cl_dic = {}
for v, c in zip(values, counts):
    cl_dic[v] = c

values2 = corpus2.value_counts(normalize=True).keys().tolist()
counts2 = corpus2.value_counts(normalize=True).tolist()

cl_dic2 = {}
for v, c in zip(values2, counts2):
    cl_dic2[v] = c

ds_scores = []
ds_scores2 = []
ds_scores_DS = []
ds_scores2_DS = []

ie = 0
for rs, ds, ed in zip(all_docs['Responsibilities and Achievements'], all_docs['Grouped'], all_docs['Job Title']):
    #if ie == 2000:
    #    break

    if len(rs) == 0:
        continue

    if 'DATA SCIEN' not in ds and len(ds_scores) > 1000:
        continue

    ds_score = 0
    ds_score2 = 0
    ds_score_DS = 0
    ds_score2_DS = 0

    for r in rs:
        r = str(r)
        review = re.sub('[^a-zA-Z]', ' ', r)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review
                  if not word in set(stopwords.words('english'))]
        for rw in review:
            if len(rw) > 1 and rw in list(cl_dic.keys()):
                if 'DATA SCIEN' in ds:
                    ds_score_DS += cl_dic[rw]
                else:
                    ds_score += cl_dic[rw]

    for r in ed:
        r = str(r)
        review = re.sub('[^a-zA-Z]', ' ', r)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review
                  if not word in set(stopwords.words('english'))]
        for rw in review:
            if len(rw) > 1 and rw in list(cl_dic2.keys()):
                if 'DATA SCIEN' in ds:
                    ds_score_DS += cl_dic2[rw]
                else:
                    ds_score += cl_dic2[rw]

    if 'DATA SCIEN' in ds:
        ds_scores_DS.append(ds_score_DS)
        ds_scores2_DS.append(ds_score2_DS)
    else:
        ds_scores.append(ds_score)
        ds_scores2.append(ds_score2)

    if ie % 100 == 0:
        print(ie, ds, ds_score, ds_score2, ds_score_DS, ds_score2_DS)
    ie += 1


#print(ds_scores)

print('lens=', len(ds_scores), len(ds_scores_DS))

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

ax0.hist(ds_scores, 40, density=1, label='DS Score', alpha=0.5, color="blue")
ax1.hist(ds_scores_DS, 40, density=1, label='DS Score_DS', alpha=0.5, color="green")
ax2.hist(ds_scores2, 40, density=1, label='DS Score2', alpha=0.5, color="red")
ax3.hist(ds_scores2_DS, 40, density=1, label='DS Score2_DS', alpha=0.5, color="black")


ax0.legend(loc='best')
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
fig.tight_layout()

plt.show()
