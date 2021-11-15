import time
with open('results.txt', 'r') as gma:
    print(gma.read())
    time.sleep(2)
with open('file.txt', 'r') as gam:
    for line in gam:
        for i in line:
          print(i, end='')
          time.sleep(1)


    # for line in gam.read():
    #     # for i in line:
    #         # print(i, end='')
    #         print(line)
    #         time.sleep(1)



# from pprint import  pprint
#
#
# with open('file.txt', 'w') as file:
#     file.write('My name is Roma\n')
#
# with open('txt.txt', 'a') as file:
#     file.write('I am from USA\n')
#
# with open('file.txt', 'r') as file:
#     pprint(file.read())

