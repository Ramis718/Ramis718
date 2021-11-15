# Варианты использования
list1 = list()
list2 = []
# range - диапазон
for g in  range(1, 5):
    list2.append(g)
print(list2)

list3 = [1, 5, 3.6, 6, 4]

g =[]
d = []


for i in list3:
    if i % 2 == 0:
        g.append(i)
    elif i % 2 != 0:
       d.append(i)
print(g)
print(d)


print(sorted(list3, reverse=False))

# list3.sort()
# print(list3)
#
# list3.reverse()
# print(list3)

# #идексация
# print(list3[-2])
#
# #  от какого до какого, шаги
# print(list3[0:-1:2])
#
# print(list3[-1::-2])
#
# list1.append('Ramis')
# print(list3)
# print(list3[-1][-1][0])
# print(list1+list3)

# # extend - продлевать
# list3.extend(list2)
# print(list3)
#
# list3.append(list2)
# print(list3)

# # добавлени и место
# list3.insert(4, '6')
# print(list3)

# # удаление
# del list3[4]
# print(list3)

# del list3[2:]
# print(list3)

# del list3[2], list3[3]
# list3[1] = 34
#
# print(list3)

# #append -  добавлять

# list1.append('Ramis')
#
# print(list1)
#
# # remove = удалить
# list3.remove(True)
# print(list3)
#
# # изменение
# list1[0]= 'aza'
# print(list1)

