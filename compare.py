import pandas as pd

df1 = pd.read_csv("./clean_updated_data2.csv", delimiter=',', low_memory=False)
df2 = pd.read_csv("./clean_updated_data_W2.csv", delimiter=',', low_memory=False)

df1 = df1.sort_values('WWID')
df2 = df2.sort_values('WWID')

print(df1.shape[0])
print(df2.shape[0])

for x1, x2, w1, w2 in zip(df1.Span, df2.Span, df1.WWID, df2.WWID):
    if x1 - x2 != 0:
        print(w1, w2, x1, x2)


df = pd.read_csv("./clean_filtered_data_W2.csv", delimiter=',')

df.info()

ws = df['WWID'].unique()
print(len(ws))
