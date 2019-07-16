import pickle
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from random import shuffle


print('Begin Process')
all_docs = pd.read_pickle("./job_full_title.pkl")
all_docs.info()

all_docs['Education_len'] = [len(x) for x in all_docs['Education']]
all_docs['Responsibilities_len'] = [len(x) for x in all_docs['Responsibilities and Achievements']]
#all_docs = all_docs.sample(frac=1)

print(all_docs['Responsibilities and Achievements'].head(10))
print(all_docs['Responsibilities_len'].head(10))

for rs in all_docs['Responsibilities and Achievements'][:10]:
    print('RS')
    for r in rs:
        print(r.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ").replace('nan', ''))


sys.exit()

documents = pd.DataFrame()
documents = all_docs['Grouped'].str.upper()
names = all_docs['Name'].str.upper()

print(documents.head())

dc_clean = []
for x, n in zip(documents, names):
    string = x.split('(')[0].strip()
    str_rep = string.replace(n, '').strip()
    #print(n, string)
    #print(str_rep[:-2])
    dc_clean.append(str_rep[:-2])

filtered_document = [x.replace('SENIOR', '').replace('SR', '').replace('JR', '').replace(' II', ' ').replace(' IV', ' ')
                     for x in dc_clean[:10000]]

#s = ' '
#wordcloud = WordCloud().generate(s.join(filtered_document))

# Display the generated image:
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")
#plt.show()

#print(filtered_document)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(filtered_document)

true_k = 1000
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
#for i in range(true_k):
    #print("Cluster %d:" % i),
    #for ind in order_centroids[i, :10]:
    #    print(' %s' % terms[ind]),

print("\n")
print("Prediction")
Y = vectorizer.transform(["DATA SCIENTIST"])
ds_prediction = model.predict(Y)
print(ds_prediction)

ds_jobs = []
docs = pd.Series(dc_clean[10000:])
for d in docs.unique():
    Y = vectorizer.transform([d])
    prediction = model.predict(Y)
    if prediction == ds_prediction:
        ds_jobs.append(d)

ds_jobs = pd.Series(ds_jobs)
print(ds_jobs.value_counts())
