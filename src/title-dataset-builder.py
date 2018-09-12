import pandas as pd

labelfile = open('../data/kompas-labels.txt', 'r')
labels = []

for line in labelfile:
    labels.append(line.strip())


titlefile = open('../data/kompas-data-titles.txt', 'r')
titles = []

for line in titlefile:
    titles.append(line.strip())

# Slice the number of titles to match the number of labels
titles = titles[:len(labels)]


dataframe = pd.DataFrame({'labels': labels, 'titles': titles})
dataframe.to_csv('../data/kompas-titles.csv', sep=',', index=False)