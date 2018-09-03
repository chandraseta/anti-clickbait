# Processor for kompas-raw.txt

rawfile = open('../data/kompas-raw.txt', 'r')

raw_data = []

for idx, line in enumerate(rawfile):
    if idx % 2 == 1:
        line = line[3:]
        raw_data.append(line)

titlefile = open('../data/kompas-data-titles.txt', 'w+')
contentfile = open('../data/kompas-data-contents.txt', 'w+')

for data in raw_data:
    title = data.split('|')[0]
    data = data.replace(title, '')

    data = data[2:]

    if '- Kompas.com' in title:
        title = title.replace('- Kompas.com', '')
        title = title.strip(' ')

    # Remove duplicate titles in front of the articles
    data = data.replace(title, '')
    data = data.strip(' ')

    titlefile.write(title + '\n')
    contentfile.write(data)