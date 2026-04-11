# Hash Map Implementation: Word frequency checker

# A random sentence
sentence = (
    "The quick brown fox jumps over the lazy dog while the quick fox "
    "watches another quick brown dog and the lazy dog slowly watches "
    "the fox as the brown fox jumps again and the quick dog follows "
    "the fox and the fox keeps jumping over the lazy dog again and again"
)

# Dictionary for keeping track of each word count
word_frequency = {}

for word in sentence.split(" "):
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Display all words and their counts
for word, count in word_frequency.items():
    print(f"The word {word} appears {count} times in the sentence.")