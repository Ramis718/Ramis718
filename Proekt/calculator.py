while True:

    user = int(input("Введите цифру:\n"))
    user1 = input("Ведите опирацию:\n")
    user2 = int(input("Введите цифру:\n"))

    if user1 == '+':
        print(user+user2)
    elif user1 == "-":
        print(user-user2)
    elif user1 == '*':
        print(user*user2)
    elif user1 == '/' and user2 != 0:
        print(user/user2)
    elif user1 == '/' and user2 == 0:
        print('ERROR')
        break
    elif user2 == '0':
        print("Выход")
        break
    else:
     print("Вот ваш ответ")



















