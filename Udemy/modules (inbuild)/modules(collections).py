from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))
sentence = ' blah blah blah archit is motu'
print(Counter(sentence))

dictonary = defaultdict(lambda: 'Dose not exsist', {'a': 1, 'b': 2})
# with defaultdict we are going to get a default value if something dosen't exsist
print(dictonary['n'])

# an ordered dictonary retains the order that you insert into dictonary
# orderedDict check the order of the dictonary
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
print(d2 == d)
