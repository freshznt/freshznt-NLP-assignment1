import matplotlib.pyplot as plt

# 读取 word_frequency.txt 文件
word_frequency = {}
with open("filtered_word_frequency.txt", 'r', encoding='utf-8') as file:
    for line in file:
        word, freq = line.strip().split()[0][:-1],line.strip().split()[1]   # 假设文件每行为 '词： 频率'，使用 ':' 分割
        word_frequency[word] = int(freq)

# 按照词频从高到低排序
sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

# 提取词频和排名
frequencies = [pair[1] for pair in sorted_word_frequency]
ranks = range(1, len(frequencies) + 1)

# 绘制词频与排名之间的曲线
plt.figure(figsize=(10, 6))
plt.plot(ranks, frequencies)
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Zipf\'s Law')
plt.xscale('log')  # 使用对数坐标轴
plt.yscale('log')
plt.grid(True)
plt.show()
