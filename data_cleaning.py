import pandas as pd
import pickle
import numpy as np
import sys

df = pd.read_excel(open(r'C:\Users\jchaves6\Documents\Updated_File.xlsx', 'rb'), sheet_name='Sheet 1')
#df['Job Position Title Function Subfunction'] = [x.replace(y.upper(), 'XXX')
#                                                 for x, y in zip(df['Job Position Title Function Subfunction'],
#                                                                 df['Name'])]
df['Hierarchy'] = df['Hierarchy'].str.upper()
df['Name'] = df['Name'].str.upper()
df['Grouped'] = df['Grouped'].str.upper()
df['Hierarchy'] = df['Hierarchy'].str.replace(' NA ', '')
df['Grouped'] = df['Grouped'].str.replace('?', '')
df.info()

df2 = pd.read_excel(open(r'C:\Users\jchaves6\Documents\RV1003_Manage_External_Job_History_2019_06_27_20_08_IST.xlsx',
                         'rb'))
df2.info()
df3 = pd.read_excel(open(r'C:\Users\jchaves6\Documents\RG0072_Manage_Education_2019_06_27_20_11_IST.xlsx', 'rb'),
                    sheet_name='Sheet1')
df3.info()

df["Highest Degree Received"] = ""
df["Education"] = ""
df["Field of Study"] = ""

df["Job Title"] = ""
df["Company"] = ""
df["Responsibilities and Achievements"] = ""

dc2 = {}
dc3 = {}

for i, w in enumerate(df.WWID):
    if i % 500 == 0:
        print(i, w)
    dc2[w] = [list(df2[df2['Employee ID'] == w]['Job Title'].values),
              list(df2[df2['Employee ID'] == w]['Company'].values),
              list(df2[df2['Employee ID'] == w]['Responsibilities and Achievements'].values)]

    dc3[w] = [list(df3[df3['WWID'] == w]['Highest Degree Received'].values),
              list(df3[df3['WWID'] == w]['Education'].values),
              list(df3[df3['WWID'] == w]['Field of Study'].values)]

    df.at[i, 'Job Title'] = dc2[w][0]
    df.at[i, 'Company'] = dc2[w][1]
    df.at[i, 'Responsibilities and Achievements'] = dc2[w][2]
    df.at[i, 'Highest Degree Received'] = dc3[w][0]
    df.at[i, 'Education'] = dc3[w][1]
    df.at[i, 'Field of Study'] = dc3[w][2]

print(df['Name'].head(), df['Grouped'].head())

df.to_pickle("./job_full_title.pkl")

'''
df['Job'] = df['Job Position Title Function Subfunction'].str.split('(').str.get(0)
df['Job'] = df['Job'].str.split(' - XXX').str.get(0)
df['Job'] = df['Job'].str.replace('POST-DOC', 'POSTDOC')
df['Job'] = df['Job'].str.replace(',', ' ')
df['Job'] = df['Job'].str.replace('COUNSEL - PATENT', 'COUNSEL PATENT')
df['Job'] = df['Job'].str.replace('COUNSEL-PATENT', 'COUNSEL PATENT')
df['Job'] = df['Job'].str.replace('COUNSEL-TRADE', 'COUNSEL TRADE')
df['Job'] = df['Job'].str.replace('VP', 'VICEPRESIDENT')
df['Job'] = df['Job'].str.replace('VICE PRESIDENT', 'VICEPRESIDENT')
df['Job'] = df['Job'].str.replace('VICE-PRESIDENT', 'VICEPRESIDENT')
df['Job'] = df['Job'].str.replace(' - IT ', ' IT ')

df_search = df['Job'].str.findall(r'-\w\w-').str.get(0)
df['Job'] = pd.Series([x.replace(y, y[1:2]) for x, y in zip(df['Job'], df_search.fillna(''))])

#selected = df[df['DATA SCIEN'] > 0]
#selected.info()


df['Job'] = df['Job'].str.split('-')

#print(df['Job'][df['Job'].str.len() == 1])
print(len(df['Job'][df['Job'].str.len() == 1]))

docs = pd.DataFrame()
docs['WWID'] = [x for x in df['WWID'][df['Job'].str.len() == 1]]
docs['Job'] = [x[0] for x in df['Job'][df['Job'].str.len() == 1]]
docs['Country'] = [x for x in df['Country Working'][df['Job'].str.len() == 1]]
docs['HighestDegree'] = [x for x in df['Highest Degree Received'][df['Job'].str.len() == 1]]
docs['Education'] = [x for x in df['Education'][df['Job'].str.len() == 1]]
docs['FieldOfStudy'] = [x for x in df['Field of Study'][df['Job'].str.len() == 1]]
docs['JobTitle'] = [x for x in df['Job Title'][df['Job'].str.len() == 1]]
docs['Company'] = [x for x in df['Company'][df['Job'].str.len() == 1]]
docs['Responsibilities'] = [x for x in df['Responsibilities and Achievements'][df['Job'].str.len() == 1]]

#print(docs.values[0])

docs.to_pickle("./job_title.pkl")
'''
