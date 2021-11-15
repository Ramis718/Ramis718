import re
#
# my_text = 'Vasya, 1999, vasfkjdf@gmail.com'\
#           'nikita, 1995, nikitadf@mail.ru'\
#           'victor, 1994,  victor@yedex.ru'\
#           'Voloda, 1966, voloda@git.com'\
#           'misha, 1955, misha@gmail.com'
# #
#
# """
# \d
# \D
# []{}
#
# \w
# \W
# [A-Z, a-z]+
#
# \s
# \S
# @(?!gmail)\w+.\w+'
#
#
# """
#
# seanching = r'@(?!gmail\.com)\w+.\w'
# results = re.findall(seanching, my_text)
# print(results)

file_path = "mock.data.txt"
result_file_path = 'results.txt'
file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_1 = file_reader.read()

searching = r'[\w+_-]+@[\w_-]+.[\w.]+'
result_all = re.findall(searching, my_text_1)

for item in result_all:
    print(item)
    result_file.write(item+'\n')


print(f'Total: {str(len(result_all))}')
