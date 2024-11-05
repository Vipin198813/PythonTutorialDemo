#Change the first and 4th letter to upper case
def old_macdonald(name):
    first_letter = name[0].upper()
    in_between = name[1:3]
    fourth_letter = name[3].upper()
    rest = name[4:]
    return first_letter + in_between + fourth_letter + rest

Name = old_macdonald("macdonald")
print(Name)


#Take a sentence and return the words in reverse order
def master_sentence(text):
    list = text.split()
    reversed_list = list[::-1]
    return ' '.join(reversed_list)

result = master_sentence("How are you")
print(result)
result = master_sentence("I am working in Damco solutions limited Noida")
print(result)

mylist = ['a','b','c','d']
print(''.join(mylist))
