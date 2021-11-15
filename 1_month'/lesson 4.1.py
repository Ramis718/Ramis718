#
# lsr = (1, 2, 3, 1, 1, 3, 4, 4, 5)
#
#
# set_1 = set()
# set_2 = set(lsr)
#
# set_2.add(1)
#
# print(set_2)

# print(type(set(lsr)))
# print(len(set_2))



menu = {
    'plow':{"рис", "мясо", "морковь"},
    'beshbarmak':{"мясо", "лапша", "лук"},
    'kasha':{'крупа', "молоко", "масло"}
}

quest = input('Choose:\n')

for designation, ingredients in menu.items():
    if quest == designation:
        print(designation, ingredients)
    elif quest in ingredients:
        print(designation)
    

    else:
        print('goobuy')


plow = {"рис", "мясо", "морковь"},
beshbarmak = {"мясо", "лапша", "лук"}

# print(plow & beshbarmak)
# print(plow.intersection(beshbarmak))
#
print(plow | beshbarmak)
print(plow.union(beshbarmak))
#
# print(plow . beshbarmak)
# print(plow.difference(beshbarmak))
#
# print(plow ^ beshbarmak)
# print(plow.symmetric_difference(beshbarmak))
