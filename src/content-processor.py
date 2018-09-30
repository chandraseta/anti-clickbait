# Processor for kompas-data-contents.txt

contentfile = open('../data/kompas-data-contents.txt', 'r')

content_data = []

for line in contentfile:
    content_data.append(line)

processed_contentfile = open('../data/kompas-data-contents-processed.txt', 'w+')

for id, content in enumerate(content_data):
    idxs = [0, 0, 0, 0]
    idxs[0] = content.find('-')
    idxs[1] = content.find('–')
    idxs[2] = content.find('—')
    idxs[3] = content.find('--')

    # If string is not found, add 100 to make the idx big
    for i, idx in enumerate(idxs):
        if idx < 0:
            idxs[i] += 100

    separator_idx = min(idxs)
    d_dash = separator_idx == idxs[3]
    
    start_index = separator_idx + 1
    if d_dash:
        start_index += 1

    if start_index <= 100:
        content = content[start_index:]
        content = content.strip()

    processed_contentfile.write(content + '\n')