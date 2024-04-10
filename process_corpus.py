import os
import jieba
import jieba.analyse
import re
from collections import Counter

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
        seg_list = jieba.cut(text, cut_all=False) 
        return list(seg_list)

def process_folder(folder_path):
    seg_results = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            seg_results.extend(process_file(file_path))
    return seg_results

folder_path = './corpus_utf8/'

seg_results = process_folder(folder_path)

with open('segmented_texts.txt', 'w',encoding='utf-8') as output_file:
    output_file.write(' '.join(seg_results))

word_count = Counter(seg_results)
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

with open('word_frequency.txt', 'w', encoding='utf-8') as freq_file:
    for idx, (word, freq) in enumerate(sorted_word_count, start=1):
        freq_file.write(f'{idx}. {word}: {freq}\n')


jieba.setLogLevel(20) 
jieba.analyse.set_stop_words("cn_stopwords.txt")

with open("word_frequency.txt", 'r', encoding='utf-8') as file:
    seg_results = {line.split()[1][:-1]:line.split()[2] for line in file}

with open("cn_stopwords.txt", 'r', encoding='utf-8') as f:
    stopwords = set([line.strip() for line in f])

filtered_seg_results = [(word,freq) for word,freq in seg_results.items() if word not in stopwords]

with open('filtered_word_frequency.txt', 'w', encoding='utf-8') as output_file:
    for word, freq in filtered_seg_results:
        output_file.write(f"{word}: {freq}\n")
