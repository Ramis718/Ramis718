a = 10
b = 20
c = a + b
# print(c)

s= 10
e= 54
c= 10-54
# print(c)

# return - возврат, result - результат,
def plus(a,b):
    return a+b
result = plus(5,10)
# print(plus(4,plus(1,4)))
#
# print(result)


def menu(drink, lunch, dessert='медовый торт'):
    return {'сок': drink, 'обед': lunch, 'десерт': dessert}

# items - предметы, dict - диктовать, sow - показать
# def show(dict1: dict):
#     for i, k in dict1.items():
#         print(i, '-', k)

monday = menu("компот", "суп", "брауни")
tuesday = menu(dessert="пироженое", drink="сок", lunch="омлет")
friday = menu('чай', "борщ")

# show(monday)
# show(menu(dessert='манты', drink="людей", lunch='бананы'))

print(monday)
print(tuesday)
print(friday)


# args -  аргументы, sum -  сумма
# def plus(a, *args):
#     return a + sum(args)
#
# print(plus(5,5))
#
# # kwargs -
# def dct(**kwargs):
#     print(kwargs)
# dct(a=1, b=2, с=+3)



