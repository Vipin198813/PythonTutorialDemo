# Split incoming string words and compare the first letter of both the strings
# Return true if first letter of both words are same else return false
import split
def string_checker(text):
    list = text.split()
    return list[0][0] == list[1][0]

result = string_checker('Vipin Vathore')
print(result)