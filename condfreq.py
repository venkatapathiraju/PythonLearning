import nltk
from nltk.corpus import brown,inaugural
brown_cfd = nltk.ConditionalFreqDist(
    (genre,word) 
    for genre in brown.categories() 
    for word in [item.lower() for item in brown.words(categories = genre)] 
    )
modals = ['can', 'could', 'may', 'might', 'must', 'will']
genres = ['news','religion','romance']
#brown_cfd.tabulate(conditions=genres, samples=modals)
ac_cfd = nltk.ConditionalFreqDist(
           (fileid[:4],target)
           for fileid in inaugural.fileids()
           for w in inaugural.words(fileid)
           for target in ['america', 'citizen']
           if w.lower().startswith(target))
#ac_cfd.tabulate(conditions=['america','citizen'],samples=[1841,1993])
"""
ac_cfd = nltk.ConditionalFreqDist(
    (fileid[:4],target)
    for fileid in inaugural.fileids()
    for target in [item.lower() for item in inaugural.words(fileid) if item.lower().startswith('america') or item.lower().startswith('citizen')]
)
"""
ac_cfd.tabulate(conditions=['1841','1993'],samples=['america','citizen'])