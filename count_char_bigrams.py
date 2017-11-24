import sys
from collections import Counter

first = True

counter = Counter()
capital_counter = Counter()

for line in sys.stdin:
    if first:
        first = False
        continue
    
    data = line.strip().split()
    word = data[0]
    capital_word = data[0].capitalize()
    freq = int(data[4])
    capital_freq = data[5]
    
    #  print(word, freq)

    for i in range(len(word) - 1):
        bigram = tuple([word[i], word[i + 1]])
        capital_bigram = tuple([capital_word[i], capital_word[i + 1]])
        counter[bigram] += int(freq)
        capital_counter[capital_bigram] += freq


with open(sys.argv[1], 'w') as f:
    for pair in counter:
        f.write("\t".join([pair[0], pair[1], str(counter[pair])]) + "\n")
    
with open(sys.argv[2], 'w') as f:
    for pair in capital_counter:
        f.write("\t".join([pair[0], pair[1], str(capital_counter[pair])]) + "\n")

#  print(counter)

#  print(capital_counter)

        
