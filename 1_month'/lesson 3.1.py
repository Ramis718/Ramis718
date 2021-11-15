
# a = ('qwe', 1, 2.5)
# for i in a:
#     if type(i) == str:
#         print(i)



vowels = ('a', 'e', 'i', 'y', 'o', 'u')
consonats = ('q', 'w', 'r', 't', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'z', 'x', 'c', 'v', 'b', 'n', 'm')

vowels_list =[]
consonats_list =[]
print(len(vowels))

# count = 3
# while len(vowels_list) != 3:
#     count -= 1
word = input('Введите слово').lower()

for letter in word:
    if  letter in vowels:
            vowels_list.append(letter)
    elif letter in consonats:
            consonats_list.append(letter)
print(vowels_list)
print(consonats_list)


# tpl = tuple()
# tpll =()
#
# numbers = (1, 3, 7, 8)
# text = ('ads', 'fda')
# print(id(numbers))
# numbers = numbers + text
# print(numbers)
#
#
# print(id(numbers))
# print(type(numbers))
#
# numbers = list(numbers)
# print(type(numbers))
# #numbers.append(5)
# print(numbers)
