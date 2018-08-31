linkfile = open('../data/kompas-links.txt', 'r')

links = []

for line in linkfile:
    links.append(line)

# Remove duplicates
links = list(set(links))

# Remove pictures (foto.kompas.com)
for idx, link in enumerate(links):
    if 'foto.kompas.com' in link:
        del links[idx]

cleanfile = open('../data/kompas-links-clean.txt', 'r')
n_link = 0

for line in cleanfile:
    n_link += 1

linkfile = open('../data/kompas-links.txt', 'w+')
cleanfile = open('../data/kompas-links-clean.txt', 'w+')

for link in links:
    linkfile.write(link)
    cleanfile.write(link)

n_new_link = len(links) - n_link

print('Cleanup done! Added {} new links'.format(n_new_link))