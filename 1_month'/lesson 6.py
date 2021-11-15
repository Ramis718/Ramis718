#
# #  как создается
# a = lambda a, b: a + b
# print(a(5, 6))
#
# print(10 + (lambda x: x ** 2)(2))
#
# # lambda  по умолчанию
# r =((lambda x, y=2: x + y)(2, 6))
#
#
# print(r)
#
#
# print(type(a))
# print(type(r))
words = ['kg', 'kz', 'ru', 'ua']
names = ['aza', 'samat', 'erkin', 'max', 'roma', 'azamat']

# def up_l(word):
#     return word.upper()
# def  edit_l(lst, fund):
#     for word in lst:
#         print(fund(word))
#
# # edit(words, up_l)
# edit_l(names, up_l)


edit_l = list(map(lambda word: word.upper(), words))

print(edit_l)
print(list(map(lambda word: word.upper(), names)))


filter_names = list(filter(lambda word: not word.startswith('a'), names))
print(filter_names)