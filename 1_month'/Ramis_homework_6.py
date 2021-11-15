
#  созздал список five
five = [1, 2, 3, 4, 5]


# с помощью lambda функции прибавил каждой обьекту 5   и сохранил в ten
ten = list(map(lambda x: x + 5, five))
print(ten)

# Конкатена́ция списка ten  с списком five
#  сортировка списка
ten.extend(five)
ten.sort()
print(ten)

# c помощбю фстроеной функции  filter  фильтруем числа четные или нечетные
even = list(filter(lambda y: y % 2 == 0, ten))
odd = list(filter(lambda y: y % 2 != 0, ten))
print(ten)


# Создать функцию для вывода объекта списка по указанному индексу.
def index(tee=ten):
#  делаем безконечный цикал
    while 1:
#  создаем исключение
        try:
            user = input("Введите индекс ( для выйхода  введите = 'a' ): " )
#  сообщаем пользователь что он может ввести и при обходимости выйти с программы
            if user == 'a'.lower():
                break
            print(tee[int(user)])
# обрабатываем ошибку
        except IndexError:
            print(f"индекс неверный!\nПопробуйте ввести  от 0 до  {len(tee) - 1}")
        except:
            print(f"вводите только числа! от 0 до  {len(tee) - 1}")




index()


