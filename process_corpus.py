import os
import jieba
import jieba.analyse
import re
from collections import Counter

# 定义一个函数，用于读取并分词处理单个txt文件
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
        seg_list = jieba.cut(text, cut_all=False)  # 使用jieba进行分词
        return list(seg_list)  # 返回分词结果，以列表形式返回

# 定义一个函数，用于处理整个文件夹下的所有txt文件
def process_folder(folder_path):
    seg_results = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            seg_results.extend(process_file(file_path))
    return seg_results

# 设置当前文件夹路径
folder_path = './corpus_utf8/'

# 调用函数处理整个文件夹下的txt文件
seg_results = process_folder(folder_path)

# 将分词结果写入新的文件
with open('segmented_texts.txt', 'w',encoding='utf-8') as output_file:
    output_file.write(' '.join(seg_results))

# 统计分词频率并排序
word_count = Counter(seg_results)
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 将分词频率及排名写入文件
with open('word_frequency.txt', 'w', encoding='utf-8') as freq_file:
    for idx, (word, freq) in enumerate(sorted_word_count, start=1):
        freq_file.write(f'{idx}. {word}: {freq}\n')


# 加载jieba的默认停用词列表
jieba.setLogLevel(20)  # 设置日志级别，避免显示加载停用词信息
jieba.analyse.set_stop_words("cn_stopwords.txt")  # 停用词列表文件需要提前准备好，命名为stopwords.txt

# 读取存储了分词结果的文件
with open("word_frequency.txt", 'r', encoding='utf-8') as file:
    seg_results = {line.split()[1][:-1]:line.split()[2] for line in file}  # 假设文件每行为 '词语: 频率'，这里只取词语部分

with open("cn_stopwords.txt", 'r', encoding='utf-8') as f:
    stopwords = set([line.strip() for line in f])

# 根据jieba的停用词列表，过滤掉分词结果中的停用词
filtered_seg_results = [(word,freq) for word,freq in seg_results.items() if word not in stopwords]

# 统计过滤后的分词结果的词频

# 将过滤后的分词频率保存到新的文件
with open('filtered_word_frequency.txt', 'w', encoding='utf-8') as output_file:
    for word, freq in filtered_seg_results:
        output_file.write(f"{word}: {freq}\n")
