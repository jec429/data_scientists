import pandas as pd
import re

#pd.set_option('display.expand_frame_repr', False)

df = pd.read_excel(open(r'C:\Users\jchaves6\Documents\Updated_File.xlsx', 'rb'))
df.info()
df = df.sort_values('PG', ascending=False)

all_docs = df

selected = all_docs[(all_docs['Grouped'].str.upper().str.contains('DATA SCIEN')) |
                    (all_docs['Grouped'].str.upper().str.contains('DATA ENGIN')) |
                    (all_docs['Grouped'].str.upper().str.contains('ANALYTIC')) |
                    (all_docs['Grouped'].str.upper().str.contains('ANALYTICS')) |
                    (all_docs['Grouped'].str.upper().str.contains('EPIDEMIO')) |
                    (all_docs['Grouped'].str.upper().str.contains('STATI')) |
                    (all_docs['Grouped'].str.upper().str.contains('STATS')) |
                    (all_docs['Grouped'].str.upper().str.contains('STATISTIC')) |
                    (all_docs['Grouped'].str.upper().str.contains('MODEL')) |
                    (all_docs['Grouped'].str.upper().str.contains('INSIGHT')) |
                    (all_docs['Grouped'].str.upper().str.contains('INTELLI')) |
                    #(all_docs['Grouped'].str.upper().str.contains('AUTOMAT')) |
                    (all_docs['Grouped'].str.upper().str.contains('PROGRAMMER'))
                    ]
selected.info()

counts = []

df['Hierarchy'] = df['Hierarchy'].str.upper()
df['Name'] = df['Name'].str.upper()
df['Grouped'] = df['Grouped'].str.upper()
df['Hierarchy'] = df['Hierarchy'].str.replace(' NA ', '')
df['Grouped'] = df['Grouped'].str.replace('?', '')
#df['Grouped'] = df['Grouped'].str.replace('- ?', '')

#df['Name'] = df['Name'].str.replace('SUZAN PATRICIA RIVETTI BARRETTI', 'SUZAN RIVETTI BARRETTI')
#df['Hierarchy'] = df['Hierarchy'].str.replace('STEF HEYLEN', 'STEFAAN HEYLEN')
#df['Name'] = df['Name'].str.replace('OLADAPO AJAYI', 'DAPO AJAYI')
#df['Name'] = df['Name'].str.replace('MARIA DE LOURDES CASTELLANOS DE SAMPER', 'LULY CASTELLANOS DE SAMPER')
#df['Hierarchy'] = df['Hierarchy'].str.replace('FILIP VERHOEVEN', 'PHILIPPE VERHOEVEN')
#df['Name'] = df['Name'].str.replace('ANA MARIA GARCIA BELLO', 'ANA GARCIA BELLO')
#df['Name'] = df['Name'].str.replace('VAISHALI SHRIKANT BHAT', 'VAISHALI BHAT')
#df['Name'] = df['Name'].str.replace('NICOLA FRANCO', 'NICHOLAS FRANCO')
#df['Name'] = df['Name'].str.replace('MARGARIDA C.A. SEICA NEVES .', 'MARGARIDA NEVES')
#df['Name'] = df['Name'].str.replace('CHRISTOPHER VONWILLER', 'CHRISTOPH VONWILLER')

i = 0
for w, g in zip(df.WWID, df.Grouped):
    count = 0
    w = '('+str(w)+')'
    for h in df.Hierarchy[i:]:
        if w in h:
            count += 1
            #print(h)

    if i % 500 == 0:
    #if not bool(re.match('^[a-zA-Z0-9\s]+$', str(n))):
    #if count == 0:
        print(i+2, w, count)

    counts.append(count)
    i += 1

df['Span'] = counts

print(df.head(15))

file_name = 'clean_updated_data_W.csv'
df.to_csv(file_name, sep=',', encoding='utf-8')
