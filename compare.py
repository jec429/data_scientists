import pandas as pd
import fasttext
from nltk.corpus import stopwords
import numpy as np
from nltk.tokenize import RegexpTokenizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_excel('DataAnalyticsEEs-Updated.3.xlsx', sheet_name='Email')
df = df.drop_duplicates(subset='Email', keep="first")
df = df.fillna('')

df.info()

#for iq in df['Internal Qualifications'][:10]:
#    print(iq.split('.'))

import sys
#sys.exit()

a0 = df[df['Email'].str.contains('amyer2')]['Internal Qualifications']
a0 = np.array(a0)
a1 = df[df['Email'].str.contains('narbabzd')]['Internal Qualifications']
a1 = np.array(a1)
a2 = df[df['Email'].str.contains('nbaro')]['External Qualifications']
a2 = np.array(a2)
a3 = df[df['Email'].str.contains('dmengis2')]['External Qualifications']
a3 = np.array(a3)
a4 = df[df['Email'].str.contains('kbettenc')]['Internal Qualifications']
a4 = np.array(a4)
a5 = df[df['Email'].str.contains('jdoering')]['External Qualifications']
a5 = np.array(a5)
a6 = df[df['Email'].str.contains('dkaplan6')]['External Qualifications']
a6 = np.array(a6)
a7 = df[df['Email'].str.contains('jheadd')]['Internal Qualifications']
a7 = np.array(a7)
a8 = df[df['Email'].str.contains('msoltani')]['External Qualifications']
a8 = np.array(a8)
a9 = df[df['Email'].str.contains('cchehoud')]['External Qualifications']
a9 = np.array(a9)

model = fasttext.load_model("fastText/wiki.en.bin")

sims0 = []
sims1 = []
sims2 = []
sims3 = []
sims4 = []
sims5 = []
sims6 = []
sims7 = []
sims8 = []
sims9 = []

avs = []
tokenizer = RegexpTokenizer(r'\w+')
for a in [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]:
    print(a)
    tok = tokenizer.tokenize(a[0].lower())
    a2 = ' '.join([word for word in tok if word not in set(stopwords.words('english'))])
    print(a2)
    a_v = model.get_sentence_vector(a2).reshape(1, -1)
    avs.append(a_v)

#sys.exit()

ie = 0
for iq, eq in zip(df['Internal Qualifications'], df['External Qualifications']):
    if ie > 100:
        break
    sim = []

    if len(iq) < 5:
        if len(eq) < 5:
            sims0.append(0)
            sims1.append(0)
            sims2.append(0)
            sims3.append(0)
            sims4.append(0)
            sims5.append(0)
            sims6.append(0)
            sims7.append(0)
            sims8.append(0)
            sims9.append(0)
            continue
        else:
            tok = tokenizer.tokenize(eq.lower())
            a2 = ' '.join([word for word in tok if word not in set(stopwords.words('english'))])
            q = model.get_sentence_vector(a2).reshape(1, -1)
    else:
        tok = tokenizer.tokenize(iq.lower())
        a2 = ' '.join([word for word in tok if word not in set(stopwords.words('english'))])
        q = model.get_sentence_vector(a2).reshape(1, -1)

    cos = cosine_similarity(avs[0], q)
    sims0.append(cos[0][0])
    cos = cosine_similarity(avs[1], q)
    sims1.append(cos[0][0])
    cos = cosine_similarity(avs[2], q)
    sims2.append(cos[0][0])
    cos = cosine_similarity(avs[3], q)
    sims3.append(cos[0][0])
    cos = cosine_similarity(avs[4], q)
    sims4.append(cos[0][0])
    cos = cosine_similarity(avs[5], q)
    sims5.append(cos[0][0])
    cos = cosine_similarity(avs[6], q)
    sims6.append(cos[0][0])
    cos = cosine_similarity(avs[7], q)
    sims7.append(cos[0][0])
    cos = cosine_similarity(avs[8], q)
    sims8.append(cos[0][0])
    cos = cosine_similarity(avs[9], q)
    sims9.append(cos[0][0])

    # ie += 1

print(sims1[:5])

df['Sims0'] = sims0
df['Sims1'] = sims1
df['Sims2'] = sims2
df['Sims3'] = sims3
df['Sims4'] = sims4
df['Sims5'] = sims5
df['Sims6'] = sims6
df['Sims7'] = sims7
df['Sims8'] = sims8
df['Sims9'] = sims9

df.to_csv('test.csv', sep=',')
#print(cos)
