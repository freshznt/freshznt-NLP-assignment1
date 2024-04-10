import os
import jieba
from collections import Counter
import re
import math

def group_n_adjacent(generator, n):
    words = [next(generator) for _ in range(n)]
    while True:
        yield tuple(words) 
        words.pop(0)
        try:
            words.append(next(generator))
        except StopIteration:
            break

corpus_dir = './corpus_utf8/'
corpus_files = os.listdir(corpus_dir)

chinese_counter = Counter()
n = 3

for file_name in corpus_files:
    if file_name.endswith('.txt'):
        with open(os.path.join(corpus_dir, file_name), 'r', encoding='utf-8') as file:
            text = file.read()
            text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
            # chinese word entropy
            # words = list(jieba.cut(text))
            # chinese character entropy
            words = list(text)
            grouped_words = group_n_adjacent(iter(words), n)
            chinese_counter.update(grouped_words)

total_count = sum(chinese_counter.values())
probabilities = {char: count / total_count for char, count in chinese_counter.items()}

entropy = -sum(p * math.log2(p) for p in probabilities.values())/n

print("entropy:", entropy)
