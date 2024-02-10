import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text for NLP processing
text = "Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(token) for token in tokens]
print("Stemmed words:", stemmed_words)

# Part-of-speech tagging
pos_tags = pos_tag(tokens)
print("Part-of-speech tags:", pos_tags)
