import re
Text = "My phone number is 408-555-5555"
phone = re.search('\d{3}-\d{3}-\d{4}',Text)
print(phone)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,Text)
print(results.group())
print(results.group(3))
print(re.search(r'cat|dog', 'The dog is here'))
print(re.findall(r'.at','The cat in the hat sat here'))
print(re.findall(r'^\d','2 is the number'))
print(re.findall(r'\d$','The number is 2'))
phrase = 'there are 3 numbers 34 inside 5 this pattern'
pattern = r'[^\d]+'
print(re.findall(pattern,phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
abc = re.findall(r'[^!.?]+',test_phrase)
print(' '.join(abc))
