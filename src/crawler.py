import requests

from bs4 import BeautifulSoup

# Crawler for kompas.com

KOMPAS_CATEGORIES = ['news', 'ekonomi', 'bola', 'tekno', 'sains', 'entertainment', 'otomotif', 'lifestyle', 'travel', 'edukasi']
# KOMPAS_CATEGORIES = ['news']

for cat in KOMPAS_CATEGORIES:
    url = 'https://' + cat + '.kompas.com'
    request = requests.get(url)

    data = request.text
    soup = BeautifulSoup(data)

    # links = soup.find_all('a')
    links = soup.find_all('a', class_=['headline__big__link', 'headline__thumb__link', 'article__link', 'most__link'])

    linkfile = open('../data/kompas-links.txt', 'a+')

    for link in links:
        linkfile.write(link.get('href') + '\n')

    print("Crawling done for {}".format(cat))