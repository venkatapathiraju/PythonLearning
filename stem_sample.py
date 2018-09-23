"""
>>> from nltk import PorterStemmer
>>> porter = nltk.PorterStemmer()
>>> porter.stem('builders')
builder

from nltk import LancasterStemmer
>>> lancaster = LancasterStemmer()
>>> lancaster.stem('builders')
build

>>> from nltk.book import *
>>> len(set(text1))
19317
>>> lc_words = [ word.lower() for word in text1] 
>>> len(set(lc_words))
17231

>>> from nltk import PorterStemmer
>>> porter = PorterStemmer()
>>> p_stem_words = [porter.stem(word) for word in set(lc_words) ]
>>> len(set(p_stem_words))
10927

>>> from nltk import LancasterStemmer
>>> lancaster = LancasterStemmer()
>>> l_stem_words = [lancaster.stem(word) for word in set(lc_words) ]
>>> len(set(l_stem_words))
9036

nltk comes with WordNetLemmatizer. This lemmatizer removes affixes only if the resulting word is found in lexical resource, Wordnet.
>>> wnl = nltk.WordNetLemmatizer()
>>> wnl_stem_words = [wnl.lemmatize(word) for word in set(lc_words) ]
>>> len(set(wnl_stem_words))
15168 
"""
import nltk
from nltk.corpus import brown,words
from nltk import PorterStemmer,LancasterStemmer
humor_words = brown.words(categories='humor')
#print(humor_words[1:20])
lc_humor_words = [word.lower() for word in humor_words]
lc_humor_uniq_words = set(lc_humor_words)

wordlist_words = nltk.corpus.words.words()
wordlist_uniq_words = set(wordlist_words)
print(len(lc_humor_uniq_words))
print(len(wordlist_uniq_words))

porter = PorterStemmer()
lancaster = LancasterStemmer()

p_stemmed = [porter.stem(word) for word in lc_humor_uniq_words]
l_stemmed = [lancaster.stem(word) for word in lc_humor_uniq_words]

p_stemmed_in_wordlist = [word for word in p_stemmed if word in wordlist_uniq_words]
l_stemmed_in_wordlist = [word for word in l_stemmed if word in wordlist_uniq_words]
print(len(p_stemmed_in_wordlist))

print(len(l_stemmed_in_wordlist))

p_stemmed_diff = [word for word in lc_humor_uniq_words if word!=porter.stem(word) and len(porter.stem(word))==len(word)]
l_stemmed_diff = [word for word in lc_humor_uniq_words if word!=lancaster.stem(word) and len(lancaster.stem(word))==len(word)]

print(len(p_stemmed_diff))
print(len(l_stemmed_diff))