from nltk.book import text6
n = len(text6)
print(n)
u = len(set(text6))
print(u)
wc = n/u
print(wc)

ise_ending_words = [word for word in text6 if word.endswith('ing')]
print(len(ise_ending_words))

#contains_z = [word for word in set(text6) if word.find('z') >=0 ]