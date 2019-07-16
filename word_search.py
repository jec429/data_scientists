import pandas as pd
'''
docs = pd.read_pickle("./job_full_title.pkl")
all_docs = docs
all_docs['Job'] = docs['Job Position Title Function Subfunction']
selected = all_docs[(all_docs['Job'].str.contains('DATA SCIEN')) |
                    (all_docs['Job'].str.contains('DATA ENGIN')) |
                    (all_docs['Job'].str.contains('ANALYTIC')) |
                    (all_docs['Job'].str.contains('ANALYTICS')) |
                    (all_docs['Job'].str.contains('EPIDEMIO')) |
                    (all_docs['Job'].str.contains('STATI')) |
                    (all_docs['Job'].str.contains('STATS')) |
                    (all_docs['Job'].str.contains('STATISTIC')) |
                    (all_docs['Job'].str.contains('MODEL')) |
                    (all_docs['Job'].str.contains('INSIGHT')) |
                    (all_docs['Job'].str.contains('INTELLI')) |
                    #(all_docs['Job'].str.contains('AUTOMAT')) |
                    (all_docs['Job'].str.contains('PROGRAMMER'))
                    ]
selected.info()
print(selected['Region'].value_counts())
print(selected['Job Function'].value_counts())
print(selected['EC Member'].value_counts())
print(selected['Level'].value_counts())
#print(selected.Name.head(10))
#print(all_docs['DS Flag'].head())

#all_docs[all_docs['DS Flag'] == True].info()

#print(selected[['WWID', 'Job']])
'''

docs = pd.read_csv("./clean_updated_data_W.csv", delimiter=',')
all_docs = docs
all_docs['Job'] = docs['Grouped']
selected = all_docs[(all_docs['Job'].str.contains('DATA SCIEN')) |
                    (all_docs['Job'].str.contains('DATA ENGIN')) |
                    (all_docs['Job'].str.contains('ANALYTIC')) |
                    (all_docs['Job'].str.contains('ANALYTICS')) |
                    (all_docs['Job'].str.contains('EPIDEMIO')) |
                    (all_docs['Job'].str.contains('STATI')) |
                    (all_docs['Job'].str.contains('STATS')) |
                    (all_docs['Job'].str.contains('STATISTIC')) |
                    (all_docs['Job'].str.contains('MODEL')) |
                    (all_docs['Job'].str.contains('INSIGHT')) |
                    (all_docs['Job'].str.contains('INTELLI')) |
                    #(all_docs['Job'].str.contains('AUTOMAT')) |
                    (all_docs['Job'].str.contains('PROGRAMMER'))
                    ]
selected.info()

flag = []
flag0 = []
flag1 = []
flag2 = []
flag3 = []
flag4 = []
flag5 = []
flag6 = []
flag7 = []
flag8 = []
flag9 = []

for j in docs.Grouped:
    fg = False
    j = str(j)
    if 'DATA SCIEN' in j:
        flag0.append(True)
        fg = True
    else:
        flag0.append(False)

    if 'DATA ENGIN' in j:
        flag1.append(True)
        fg = True
    else:
        flag1.append(False)
    if 'ANALYTIC' in j:
        flag2.append(True)
        fg = True
    else:
        flag2.append(False)
    if 'EPIDEMIO' in j:
        flag3.append(True)
        fg = True
    else:
        flag3.append(False)
    if 'STATI' in j:
        flag4.append(True)
        fg = True
    else:
        flag4.append(False)
    if 'STATS' in j:
        flag5.append(True)
        fg = True
    else:
        flag5.append(False)
    if 'MODEL' in j:
        flag6.append(True)
        fg = True
    else:
        flag6.append(False)
    if 'INSIGHT' in j:
        flag7.append(True)
        fg = True
    else:
        flag7.append(False)
    if 'INTELLI' in j:
        flag8.append(True)
        fg = True
    else:
        flag8.append(False)
    if 'PROGRAMMER' in j:
        flag9.append(True)
        fg = True
    else:
        flag9.append(False)

    flag.append(fg)

print('flag=', sum(flag))
docs['DATA SCIEN'] = flag0
docs['DATA ENGIN'] = flag1
docs['ANALYTIC'] = flag2
docs['EPIDEMIO'] = flag3
docs['STATI'] = flag4
docs['STATS'] = flag5
docs['MODEL'] = flag6
docs['INSIGHT'] = flag7
docs['INTELLI'] = flag8
docs['PROGRAMMER'] = flag9

docs['FLAG'] = flag
file_name = 'clean_updated_data_W2.csv'
docs.to_csv(file_name, sep=',', encoding='utf-8')
#docs.to_excel('clean_updated_data2.xlsx', sheet_name='Sheet1')

#print(selected['Region'].value_counts())
#print(selected['Job Function'].value_counts())
#print(selected['EC Member'].value_counts())
#print(selected['Level'].value_counts())
#print(selected.Name.head(10))
#print(all_docs['DS Flag'].head())

#all_docs[all_docs['DS Flag'] == True].info()

#print(selected[['WWID', 'Job']])

