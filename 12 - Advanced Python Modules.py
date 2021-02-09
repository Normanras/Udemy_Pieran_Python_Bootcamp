"""
The following are all modules part of base Python
"""

# Collections Module
from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]
Counter(mylist)

mylist = ['a','a',10,10,10,10]
Counter(mylist)

sentence = "How many times does each word show up in this sentence with a word sentence?"
Counter(sentence.split())
Counter(sentence.lower().split())

letters = 'aaaaabbbbbbbccccccccccccccdddddddddddd'
c = Counter(letters)
c

c.most_common()
c.most_common(3)

list(c) # This shows a list of all the individual elements 

from collections import defaultdict

d = {'a':10}
d
d['a']
d['WRONG']

d = defaultdict(lamba:0)
d['correct']=100
d['correct']
d['WRONG KEY']
d

mytuple = (10,20,30)
mytuple[0]

from collections import namedtuple
Dog = namedtuple('Dog',['age'],'name')
Dog
sammy = Dog(age=5,breed='Husky',name='Sam')
sammy
sammy.age 
sammy.breed
sammy.name

