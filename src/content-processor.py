# Processor for kompas-data-contents.txt
MIN_IDX = 100

contentfile = open('../data/kompas-data-contents.txt', 'r')

content_data = []

for line in contentfile:
    content_data.append(line)

processed_contentfile = open('../data/kompas-data-contents-processed.txt', 'w+')

for id, content in enumerate(content_data):
    # idxs = [0, 0, 0, 0]
    idx = content.find('KOMPAS.com')
    # idxs[1] = content.find('–')
    # idxs[2] = content.find('—')
    # idxs[3] = content.find('--')

    # If string is not found, add 100 to make the idx big
    # for i, idx in enumerate(idxs):
    #     if idx < 0:
    #         idxs[i] += MIN_IDX

    # separator_idx = min(idxs)
    # d_dash = separator_idx == idxs[3]
    
    # start_index = separator_idx + 1
    # if d_dash:
        # start_index += 1

    # if start_index <= MIN_IDX:
        # content = content[start_index:]
    content = content[idx + 12:]
    content = content.strip('-')
    content = content.strip()
        
    processed_contentfile.write(content + '\n')