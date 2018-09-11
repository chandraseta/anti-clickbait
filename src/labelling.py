# Labelling for kompas-data-titles.txt

import os

titlefile = open('../data/kompas-data-titles.txt', 'r')

titles = []

for line in titlefile:
    titles.append(line)

labelfile = open('../data/kompas-labels.txt', 'r')

labels = []

for line in labelfile:
    labels.append(line.strip())

index = len(labels)

if index >= len(titles):
    print('No more titles to be labelled')
else:
    os.system('clear')
    stop = False
    while index < len(titles) and not stop:
        choice = ''
        while choice not in ['y', 'n', 's']:
            choice = input('{}\n\nType s to stop labelling\nIs it a clickbait? [y/n] '.format(titles[index]))
        if choice == 'y':
            labels.append('clickbait')
        elif choice == 'n':
            labels.append('no')
        else:
            break
        index += 1
        os.system('clear')
    print('End of labelling session')

labelfile = open('../data/kompas-labels.txt', 'w+')

for label in labels:
    labelfile.write(label + '\n')