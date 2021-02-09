#how to search for pattern structure
#regular expressions are notoriously hard to memorize syntax
#instead learn how to convert the patterns of syntax
"""
Phone number = (555)-555-5555
Regex Patter = r"(\d\d\d)-\d\d\d-\d\d\d\d"
The regex units are like wildcards waiting for a value
d=digit
parenthesis help shows structure of the patten. this is very simple
This is the same as the above phone number - pattern says (find 3 digits)
r"(\d{3})-\d{3}-\d{4}"
"""

text = "The agent's phone number is 408-555-1234. Call soon!"
'phone' in text 
import re
pattern = 'phone'
re.search(pattern,text)
pattern = 'NOT IN TEXT'
re.search(pattern,text)
pattern = 'phone'
match = re.search(pattern,text)
match
match.span()
match.start()
match.end()
text = 'my phone once, my phone twice'
match = re.search('phone',text)
matches = re.findall('phone',text)
len(matches)
for match in re.finditer('phone',text):
    print(match.span())
for match in re.finditer('phone',text):
    print(match.group())


# Part 2 - how to build pattern codes 
"""
\d = digit
\w = alphanumeric
a\ = whitespace
\D = non digit
\W = non alphanumeric
\S = non whitespace
"""

text = 'My Phone number is 123-989-2281'
phone = re.search('123-989-2281',text)
phone
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
phone.group()

"""
Quantifiers
+ = occurs more than once
{3} = occurs exactly 3 times
{2,4} = occurs 2 to 4 times
{3,} = occurs 3 or more times
* = occurs zero or more times
? = occures once or none
"""

text = 'My Phone number is 123-989-2281'
phone = re.search('123-989-2281',text)
phone
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
results.group()
results.group(1)
results.group(2)
results.group(3)
results.group(4)

# Part 3 - Additional Syntax 
# Starts/Ends with, Wildcards, etc

re.search(r'cat|dog','the cat is here') # <-- Or operator
re.findall(r'...at','The cat in the hat sat there') # <-- Wildcard operator (dot=1 letter/digit)
re.findall(r'^\d','1 is a number') # <-- This is only for STARTS with. It won't find a number after first word
re.findall(r'\d$','A number is 1') # <-- Same as above but ENDS with

# Excluding something
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]' # <-- r (find) + exclude digits 
re.findall(pattern,phrase) #<-- will find a list of every letter WITHOUT any numbers
pattern = r'[^\d]+'
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.?+ ]'.test_phrase)
' '.join(clean)
#Group for inclusion
text = 'Only find-hyphen-words in this sentence. But you do not know how long-ish they are-ish'
pattern = r'[\w]+'
re.findall(pattern,text)
pattern = r'[\w]+[\w]+'
re.findall(pattern,text)

text = 'hello would you like some catfish?'
text2 = 'hello would you like a catnap?'
text3 = 'hello have you seen this catepillar?'
re.search(r'cat(fish|nap|erpillar)',text)
re.search(r'cat(fish|nap|erpillar)',text)
re.search(r'cat(fish|nap|erpillar)',text)
