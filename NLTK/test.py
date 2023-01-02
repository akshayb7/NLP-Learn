from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello Mr. Bhardwaj! How do you do? What kind of music do you enjoy? I'm in love with Steven Wilson. XOXO"
print(sent_tokenize(text))
print(word_tokenize(text))
for i in word_tokenize(text):
    print(i)

