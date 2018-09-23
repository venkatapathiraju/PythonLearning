zenPython = '''

The Zen of Python, by Tim Peters



Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!

'''

#print(zenPython)
#for x in zenPython.split():
#    print(x.strip(',.-*!').lower())
y = [ x.lower().strip(',.-*!') for x in zenPython.split() ]
z = set(y)
print(z)

wordfreq = {}
for i in y:
    if i not in wordfreq:
        wordfreq[i] = 0
    wordfreq[i] += 1

print(wordfreq)
d = { key : value for key, value in wordfreq.items() if value > 5}
print ('filter words having frequency greater than five from word_frequency')
print (d)
    

