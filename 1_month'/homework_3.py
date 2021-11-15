data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
   if type(i) == str:
       letters.append(i.lower())
   elif type(i) == int or bool:
        numbers.append(i)

del numbers[0]
#
for i in numbers:
    if type(i) == bool:
       numbers.pop(0)
       letters.append(i)

numbers.insert(1, 2)
numbers.sort()
letters.reverse()

letters[1]= 'G'
letters[5]= 'T'

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)


