import pandas as pd

labelfile = open('../data/kompas-labels.txt', 'r')
labels = []

for line in labelfile:
    labels.append(line.strip())


titlefile = open('../data/kompas-data-titles.txt', 'r')
titles = []

for line in titlefile:
    line = line.strip()
    titles.append(line)

# Slice the number of titles to match the number of labels
titles = titles[:len(labels)]

dataframe = pd.DataFrame({'labels': labels, 'titles': titles})
dataframe.to_csv('../data/kompas-titles.csv', encoding='utf-8', sep='|', index= False, quoting=3, escapechar='\\')