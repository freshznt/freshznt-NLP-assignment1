import matplotlib.pyplot as plt

word_frequency = {}
with open("filtered_word_frequency.txt", 'r', encoding='utf-8') as file:
    for line in file:
        word, freq = line.strip().split()[0][:-1],line.strip().split()[1]   
        word_frequency[word] = int(freq)

sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

frequencies = [pair[1] for pair in sorted_word_frequency]
ranks = range(1, len(frequencies) + 1)

plt.figure(figsize=(10, 6))
plt.plot(ranks, frequencies)
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Zipf\'s Law')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
