import pandas as pd


df = pd.read_csv("./clean_updated_data_W2.csv", delimiter=',')

df.info()

df2 = df[df['FLAG']==1]

print(df2.shape[0])

seens = []
for g in df2.Hierarchy:
    seen = False
    for w in df2.WWID:
        if '('+str(w)+')' in g:
            #print(w, g)
            seen = True

    seens.append(seen)

#for i, s in enumerate(seens):
#    df2.loc[i, 'SEEN'] = s
df2['SEEN'] = seens

print(df2.head(20))

file_name = 'clean_filtered_data_W2.csv'
df2.to_csv(file_name, sep=',', encoding='utf-8')