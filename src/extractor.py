import requests

from bs4 import BeautifulSoup

# Extractor for kompas.com

crawledfile = open('../data/kompas-links-crawled.txt', 'r')

crawled_links = []

for line in crawledfile:
    crawled_links.append(line)


linkfile = open('../data/kompas-links-clean.txt', 'r')

links = []

for line in linkfile:
    if line not in crawled_links:
        links.append(line)


titlefile = open('../data/kompas-titles.txt', 'a+')
datafile = open('../data/kompas-data.txt', 'a+')
crawledfile = open('../data/kompas-links-crawled.txt', 'a+')

rawfile = open('../data/kompas-raw.txt', 'a+')

for link in links:
    print('Start: {}'.format(link))
    request = requests.get(link)
    
    data = request.text
    soup = BeautifulSoup(data, 'html.parser')

    titles = soup.find_all('title')
    paragraphs = soup.find_all('p')

    rawfile.write(link)
    rawfile.write(' | ')

    for title in titles:
        # titlefile.write(title.text)
        rawfile.write(title.text)

    rawfile.write(' | ')

    for par in paragraphs:
        # datafile.write(par.text)
        rawfile.write(par.text)

    # titlefile.write('\n')
    # datafile.write('\n')

    rawfile.write('\n')

    crawledfile.write(link)

    print('Done: {}'.format(link))