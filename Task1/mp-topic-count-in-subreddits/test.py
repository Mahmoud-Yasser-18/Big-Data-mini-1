import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
text = word_tokenize("And now for something completely different")
print(nltk.pos_tag(text)
)