from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look',
    'into', 'my', 'eyes', "you're", 'under'
]

words_counter = Counter(words)
common = words_counter.most_common(4)
print(common)

more_words = ['why','are','you','not','looking','in','my','eyes','seven']

words_counter.update(more_words)
print(words_counter)

counter1 = Counter(words)
counter2 = Counter(more_words)

print(counter1 + counter2)
print(counter1 - counter2)