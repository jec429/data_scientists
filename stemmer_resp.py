import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('words')
nltk.download('stopwords')

df = pd.read_pickle("./job_full_title.pkl")
ps = PorterStemmer()
corpus = []
for i, rs in enumerate(df['Responsibilities and Achievements']):
    rs = [r for r in rs if not pd.isna(r)]
    r = ' '.join(rs)
    review = re.sub('[^a-zA-Z]', ' ', r)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review
              if not word in set(stopwords.words('english'))]

    review = ' '.join(review)
    if i % 10 == 0:
        print(i, rs, review)

    corpus.append(review)
df['Cleaned Responsibilities'] = corpus

print(df['Name'].head(), df['Grouped'].head())

df.to_pickle("./job_full_title_cleaned.pkl")
