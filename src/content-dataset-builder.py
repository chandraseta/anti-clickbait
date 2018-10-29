import pandas as pd

contentfile = open('../data/kompas-data-contents-processed.txt', 'r')
contents = []

for line in contentfile:
    line = line.strip()
    if line == '':
        line = 'None'
    if '|' in line:
        line = line.replace('|', '')
    contents.append(line)

dataframe = pd.DataFrame({'contents': contents})
dataframe.to_csv('../data/kompas-contents.csv', encoding='utf-8', sep='|', index= False, quoting=3, escapechar='\\')