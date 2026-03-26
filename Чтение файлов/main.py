# file = open('quotes.txt')
# print(type(file))
# file.close()


# 1. Метод read()
# Метод .read() считывает весь текст, хранящийся в файле, сразу и возвращает одну длинную строку.

# file = open('quotes.txt')
# text = file.read()
# print(text)
# file.close()

#
# 2. Метод read(n)
# Метод .read() умеет считывать информацию из файла не только «целиком», но и порциями.
# Для этого в него можно передать число n — сколько символов нужно прочитать. Формат вызова следующий:

# file = open('quotes.txt')
# text = file.read(10)
# print(text)
# file.close()


# Как узнать, где находится курсор?
# У курсора есть «номер позиции» — сколько символов мы уже прошли от начала файла.
# Его можно узнать при помощи метода .tell().


# Что такое курсор?

# file = open('quotes.txt', 'r')
# print(file.tell())  # 0 — курсор в начале
# file.read(5)        # читаем 5 символов
# print(file.tell())  # 5 — курсор сдвинулся вперёд на 5 символов
# file.close()




# Как переместить курсор?

# file = open('quotes.txt', 'r')
#
# part1 = file.read(12)
# print('Первый кусочек:', part1)
#
# file.seek(0)  # возвращаем курсор в начало
# part2 = file.read(12)
# print('Снова сначала:', part2)
# file.close()






# в примере ниже мы считываем все содержимое файла, начиная с 65-й позиции

# file = open('quotes.txt', 'r')
#
# file.seek(65)       # перемещаемся на 65-й символ
# content = file.read()
# print(content)
#
# file.close()






# 3. Метод readline()— чтение по строкам

# file = open('quotes.txt', 'r')
# line = file.readline()
# print(line)
# file.close()


# если курсор стоит в середине строки,
# .readline() начинает читать с текущей позиции курсора и берёт символы до конца строки.
#
# file = open('quotes.txt', 'r')
# file.seek(8)             # курсор внутри первой строки
# line = file.readline()
# print(line)
# file.close()





# Несколько вызовов подряд
# file = open('quotes.txt', 'r')
#
# print(file.readline())  # первая строка
# print(file.readline())  # вторая строка
#
# file.close()


# Теперь код без пробелов - метод strip
# file = open('quotes.txt', 'r')
#
# print(file.readline().strip())  # первая строка
# print(file.readline().strip())  # вторая строка
#
# file.close()









# 4. Метод readlines() — список строк

# Метод .readlines() читает весь файл целиком, но возвращает его не одной длинной строкой, а списком строк.
# file = open('quotes.txt', 'r')
# lines = file.readlines()
# file.close()
#
# print(lines)




# Влияние курсора

# file = open('quotes.txt', 'r')
# file.seek(250)           # смещаемся на 250-й символ
# lines = file.readlines()
# print(lines)
# file.close()


# Если курсор стоит в конце файла, повторные попытки чтения вернут «пустые» значения:
# f = open('quotes.txt', 'r')
#
# f.read()         # читаем весь файл
#
# #  пробуем читать ещё
# print(repr(f.read()))      # ''  — больше нечего читать
# print(repr(f.readline()))  # ''  — нет следующей строки
# print(f.readlines())       # []  — пустой список
#
# f.close()


# Задание 1
# def print_first_two_lines(file_name:str):
#     with open(file_name,'r') as f:
#         print(f.readline().strip())
#         print(f.readline().strip())
# print_first_two_lines('chat.txt')

#
# def print_first_two_lines(file_name:str):
#     with open(file_name,'r') as f:
#         for _ in range(2):
#             print(f.readline().strip())
# print_first_two_lines('chat.txt')



# Задание 2

# def print_first_and_last_line(file_name):
#     with open(file_name) as f:
#         lines = f.readlines()
#         if lines:
#             print(lines[0].strip())
#             print(lines[-1].strip())
# print_first_and_last_line('chat.txt')


#
# def print_first_and_last_line(file_name):
#     f = open(file_name).readlines()
#     print(f[0].strip(), f[-1].strip(),sep='\n')





# Задание 3
# def file_n_lines(file_name, n):
#     with open(file_name) as f:
#         for line in range(n):
#             print(f.readline().strip())
#
# file_n_lines('words.txt', 4)




