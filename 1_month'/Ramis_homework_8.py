# импоритирую random и datetime
from random import randint
from datetime import datetime

# спрашиваю количество попыток и имя
attempts = int(input("ВВЕДИТЕ КОЛИЧЕСТВО ПОПЫТОК:"))
name = input("Введите имя:")
a1 = attempts
start = datetime.now()

# здесь создаю цикал
while attempts != 0:
    # здесь создаю исключение
    try:
        a = randint(1, 9)
        b = randint(1, 9)
        user = f"{a} * {b}  = "
        print(user, "?", end=' ')
        i = int(input())
        attempts -=1
        rightAnswer = a * b
        print(rightAnswer)
        # здесь добавлюем примеры и указыеваем праильно или нет
        with open('results.txt', 'a') as file:
            if rightAnswer == i:
                file.write(user+" "+ str(i)+ " ("+ str(rightAnswer)+")правильно\n" )
            if rightAnswer != i:
                file.write(user+" "+ str(i)+ " ("+ str(rightAnswer)+")неправильно\n")
# здесь проверяем пользователя на коректный ввод
    except ValueError:
        print("Введите только числа")
        break
# здесь добавляем время, имя, количество попыток
with open('results.txt', 'a')  as fil:
    fil.write(f'было {a1} попыток, потрачино время: {datetime.now() - start}, Имя: {name} ')





