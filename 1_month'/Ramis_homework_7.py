# из random импортируем randint  и time
from random import randint
import  time
# загадываем числа от 1 до 100
guess = randint(1, 100)
count = 1
# ввыводи на экран guess
print(guess)
#  делаем бесконечный цикал
start = time.time()
while 1:
  # создаем исключение
  try:
    user = int(input("Угадайте целое число от 1 до 100:\nПовторите ещё раз:"))
    # предупреждаем пользователя, чтобы он ввел от 1 до 100 числа
    if user > 100 or user < 0:
        print("Введите число от 1 до 100")
     # здесь создаем диопозон от 5 и от 10   для угадывания числа
    elif user -5 <= guess and user +5 >= guess:
      print('горячо')
    elif user -10 <= guess and user +10 >= guess:
      print('тепло')
     # пользователь ввел число меньше  загаданого его придуприждаем здесь
    if user < guess:
        print("Ваше число Меньше, чем задумал компьютер")
        count += 1
     #  здесь сообщаем пользователю что он ввел число больше загаданого
    elif user > guess:
      print("Ваше число Больше , чем задумал компьютер")
      count += 1
    # если пользователь угодал, показываем пользователю количество попыток и секунд и  выходим из программы
    elif user == guess:
        print(f"Вы угадали за {time.time()-start} сегунд\nИ на  {count} попыток")
        break
   # здесь обрабатываем что вввел пользователь, при не корректном вводе придуприждаем
  except ValueError:
    print("Вводите только чила,а не буквы или что-либо другое")
