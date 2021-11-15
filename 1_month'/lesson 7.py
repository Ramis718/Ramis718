import random
from random import choice
from datetime import datetime
import time

# start = datetime.now()
# time.sleep(1)
# end = datetime.now()-start
# print(start)
# print(end)


# def timer(num):
#     while num != 0:
#         num -= 2
#         time.sleep(1)
#         print(num)
#
# timer(6)


students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23]

while len(students) != 0:
   q = input("y/n")
   if q == 'y'.lower():
        # number = random.choice(students)
        # students.remove(number)
        print(students.pop(students.index(random.choice(students))))
        print(students)
   elif q == 'n'.lower():
       print("круг заверщтлся")
       break




# for i in range(1, 24):
#     a.append(i)
#
# print(a)







# # модули
#
# # import random
# from random import randint, choice, randrange, sample
#
# print(randint(1,10))
#
# # choice - выбирать
# tpl = 1, 2, 3, 4, 5
# print(choice(tpl))
# print(sample(tpl, 2))
#
# print(randrange(1, 10, 5))

