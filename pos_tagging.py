"""
nltk.help.upenn_tagset('JJ')
>>> text = 'Python/NN is/VB awesome/JJ ./.'
>>> [ nltk.tag.str2tuple(word) for word in text.split() ]
[('Python', 'NN'),
 ('is', 'VB'),
 ('awesome', 'JJ'),
 ('.', '.')]


 >>> import nltk
>>> text = 'Python is awesome.'
>>> words = nltk.word_tokenize(text)
>>> defined_tags = {'is':'BEZ', 'over':'IN', 'who': 'WPS'}

baseline_tagger = nltk.UnigramTagger(model=defined_tags)
>>> baseline_tagger.tag(words)
[('Python', None),
 ('is', 'BEZ'),
 ('awesome', None),
 ('.', None)]
"""
import nltk
from nltk.corpus import brown
brown_tagged_words = brown.tagged_words()
#brown_tagged_words[1:30]
brown_tagged_trigrams = nltk.trigrams(brown_tagged_words)
#for (w1,t1),(w2,t2),(w3,t3) in brown_tagged_trigrams:
    #print(t1,t2,t3)
brown_trigram_pos_tags = [(t1,t2,t3) for (w1,t1),(w2,t2),(w3,t3) in brown_tagged_trigrams]
#print(len(brown_trigram_pos_tags))
#nltk.FreqDist(tag for (word,tag) in brown_trigram_pos_tags)
brown_trigram_pos_tags_freq = nltk.FreqDist(brown_trigram_pos_tags)
print(brown_trigram_pos_tags_freq[('JJ','NN','IN')])

brown_tagged_sents = brown.tagged_sents()
total_size = len(brown_tagged_sents)
train_size = int(total_size * 0.8)
train_sents = brown_tagged_sents[:train_size]
test_sents = brown_tagged_sents[train_size:]

unigram_tagger = nltk.UnigramTagger(train_sents)
tag_performance = unigram_tagger.evaluate(test_sents)
print(tag_performance)