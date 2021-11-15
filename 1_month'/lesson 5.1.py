
# def auto_code(user):
#         if user == '1' or user == '01':
#             print("Бишкек")
#         elif user == '2' or user == '02':
#             print("Ош")
#         elif user == '3' or user == '03':
#             print("Баткенская область")
#         elif user == '4' or user == '04':
#             print("Джалабадская область")
#         elif user == '5' or user == '05':
#             print("Нарынснская область")
#         elif user == '6' or user == '06':
#             print("Ошская область")
#         elif user == '7' or user == '07':
#             print("Таласская область")
#         elif user == '8' or user == '08':
#             print("Чуйская область")
#         elif user == '09' or user == '9':
#             print("Иссык-Кульская область")
#         elif user == '0' or user == 'выйти':
#             print("Выход из программы")
#         else:
#             print("Вы ввели неверно что то не так! ")


# auto_code("01")


members = [
    {'name':'Aza', 'age':18, 'height':185, 'physic':True},
    {'name':'MIka', 'age':17, 'height':170, 'physic':False},
    {'name':'Vin', 'age':20, 'height':185, 'physic':True},
]
# soldiers- солдаты
soldiers = []

# selection_army - отборочная армия, member -  участник
def selection_army(member_lst):
    for member in member_lst:
        if member['age'] >= 18 and member['height'] >= 180 and member['physic'] == True:
            member['soldiers'] = True
            soldiers.append(member)
    print(soldiers)

selection_army(members)

# add  - добавить, height - рост, physic - физика
def add_member(name, age, height, physic):
    return {'name': name, 'age': age, 'height': height, 'physic': physic}

# members.append(add_member('Ulan', 18, 183, True))
# selection_army(members)


# find - найти
def find(name: str, lst: list):
    for member in lst:
        if member['name'] == name.title():
            return member
    print("not")

print(find('aza', members))
print(find('aza', soldiers))