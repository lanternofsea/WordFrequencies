
# Dictionary to store the frequency of words
word_frequency = {}
sentence = input("Enter a sentence: ")

# search for a full stop at the right end of the string and remove if present
sentence = sentence.rstrip(".")

# split the sentence into list of words
sentence_words = sentence.split(" ")

for word in sentence_words:
    if word in word_frequency.keys( ):
        word_frequency[word] = word_frequency[word] + 1
    else:
        word_frequency[word] = 1

print(word_frequency)