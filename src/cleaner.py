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

linkfile = open('../data/kompas-links.txt', 'w+')
cleanfile = open('../data/kompas-links-clean.txt', 'w+')

for link in links:
    linkfile.write(link)
    cleanfile.write(link)

print('Cleanup done!')