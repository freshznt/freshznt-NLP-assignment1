import os
import jieba
from collections import Counter
import re
import math

def group_n_adjacent(generator, n):
    words = [next(generator) for _ in range(n)]  # 获取前 n 个词
    while True:
        yield tuple(words)  # 返回前 n 个词组成的元组
        words.pop(0)  # 弹出第一个词
        try:
            words.append(next(generator))  # 添加下一个词
        except StopIteration:
            break


# 读取所有的 txt 文件作为语料库
corpus_dir = './corpus_utf8/'  # 假设所有的 txt 文件都存放在 corpus 文件夹中
corpus_files = os.listdir(corpus_dir)

# 分词并统计汉字频次
chinese_counter = Counter()
n = 3

for file_name in corpus_files:
    if file_name.endswith('.txt'):
        with open(os.path.join(corpus_dir, file_name), 'r', encoding='utf-8') as file:
            text = file.read()
            # 使用正则表达式去除非汉字字符和标点符号
            text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
            # 使用jieba分词
            # words = list(jieba.cut(text))
            words = list(text)
            grouped_words = group_n_adjacent(iter(words), n)
            # 统计汉字频次
            chinese_counter.update(grouped_words)

# 计算汉字的频率分布
total_count = sum(chinese_counter.values())
probabilities = {char: count / total_count for char, count in chinese_counter.items()}

# 计算汉字的熵值
entropy = -sum(p * math.log2(p) for p in probabilities.values())/n

print("汉字熵值:", entropy)
