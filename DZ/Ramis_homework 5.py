import re

file_path = "mock.data.txt"
result_file_path = 'fullname.txt'
file_read = open(file_path, mode='r', encoding='Latin-1')
full_name = open(result_file_path, mode='w', encoding='Latin-1')
my_text_1 = file_read.read()

searching = r"[A-Z]+[\w+-]+[a-z A-Z]+[\s]+[a-z A-Z)\s+[\'S]+[A-Z]+[A-Z}+[\w+-]\w+|[A-Z]+[\w+-]+[a-z A-Z]+[\s]+[A-Z]\w+"
result_all = re.findall(searching, my_text_1)

for item in result_all:
    print(item)
    full_name.write(item+'\n')

print(f'Total: {str(len(result_all))}')



# file_path = "mock.data.txt"
# result_file_path = 'mail.txt'
# file_reader = open(file_path, mode='r', encoding='Latin-1')
# mail_file = open(result_file_path, mode='w', encoding='Latin-1')
# my_text_1 = file_reader.read()
#
# searching = r'[\w+_-]+@[\w_-]+.[\w.]+'
# result_all = re.findall(searching, my_text_1)
#
# for item in result_all:
#     print(item)
#     mail_file.write(item+'\n')
#
#
# print(f'Total: {str(len(result_all))}')


# file_path = "mock.data.txt"
# result_file_path = 'extension.txt'
# file_reader = open(file_path, mode='r', encoding='Latin-1')
# exten_file = open(result_file_path, mode='w', encoding='Latin-1')
# my_text_1 = file_reader.read()
#
# searching = r'[A-Z]\w+[.]+[a-z 0-9 a-z]\w+|[A-Z]+[.]+[a-z]'
#
# result_all = re.findall(searching, my_text_1)
#
# for item in result_all:
#     print(item)
#     exten_file.write(item+'\n')
# #
# #
# print(f'Total: {str(len(result_all))}')


# file_path = "mock.data.txt"
# result_file_path = 'number.txt'
# file_read = open(file_path, mode='r', encoding='Latin-1')
# number_file = open(result_file_path, mode='w', encoding='Latin-1')
# my_text_1 = file_read.read()
#
# searching = r"#[0-9 a-z]+"
# result_all = re.findall(searching, my_text_1)
#
# for item in result_all:
#     print(item)
#     number_file.write(item+'\n')
#
# print(f'Total: {str(len(result_all))}')