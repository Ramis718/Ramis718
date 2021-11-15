def add(a, b):
    return float(a * b)
S = add(10,12)
print('S =', S)



def plus(*args):
    return int((sum(args))/len(args))

print(plus(5,7,8,9,3,7))



def menu(bite,lunch,dinner):
    return {'завтрак': bite, 'обед': lunch, 'ужин': dinner}

dinner = menu("soup", "rice", "manti")
bite = menu("egg", "kasha","coffe")
lunch = menu("plof", "lagman", "oromo")

print(dinner)
print(bite)
print(lunch)






