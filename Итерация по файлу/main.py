# file = open('todo_list.txt', 'r')
#
# print(next(file))  # Make coffee.\n
# print(next(file))  # Take over the world.\n
#
# file.close()
from string import punctuation
from unittest import result


# Чтение с помощью for

# file = open('todo_list.txt', 'r')
#
# for task in file:
#     print('Task:', task)
#
# file.close()



# Так как при чтении каждая строка сохраняет служебный символ \n на конце, то при выводе появились дополнительные переносы строк.
# Чтобы их убрать можно воспользоваться методом strip() или rstrip():


# file = open('todo_list.txt', 'r')
#
# for task in file:
#     print('Task:', task.rstrip()) # rstrip убирает переносы строк
#
# file.close()



# file = open('todo_list.txt', 'r')
#
# while True:
#     try:
#         task = next(file)
#         print('Task:', task.rstrip())
#     except StopIteration:
#         break
#
# file.close()






# Ограничения по итерации файла
# file = open('todo_list.txt', 'r')
#
# # первым циклом прочитаем все данные
# for task in file:
#     print('Task:', task.strip())
#
#
# # второй цикл выполнится 0 раз
# for task in file:
#     print('Repeat task:', task)
#
# file.close()





# Если вы хотите пройти ещё раз по строкам, вызовите file.seek(0) или откройте файл заново.

# file = open('todo_list.txt', 'r')
#
# # первым циклом прочитаем все данные
# for task in file:
#     print('Task:', task.strip())
#
# file.seek(0)
#
# # второй цикл вновь прочитает все данные
# for task in file:
#     print('Repeat task:', task.strip())
#
# file.close()






# Задание 1: Нумерация строк


# def  print_lines_with_numbers(file_name: str):
#     with open(file_name, 'r') as f:
#         for num, line in enumerate(f, 1):
#             print(f"{num}: {line}", end='')
# print_lines_with_numbers('todo_list.txt')


# Задание 2: Самая болтливая строка

# считает количество букв в каждой строке
def most_talkative_line(file_name: str):
    file = open(file_name, 'r')
    length = []
    for n, i in enumerate(file.readlines(), 1):
        length.append({f"{n}: {len(i)}"})
    file.close()
    return length
# print(most_talkative_line('todo_list.txt'))

# считает количество слов в каждой строке и возвращает самую болтливую(больше всего слов)
def most_talkative_line(file_name: str):
    with open(file_name, 'r') as f:
        max_words = -1
        result_line = ""

        for line in f:
            count_words = len(line.split())
            if count_words >= max_words:
                max_words = count_words
                result_line = line

        return  result_line

print(most_talkative_line('todo_list.txt'))


def most_talkative_line(file_name: str):
    with open(file_name, 'r') as f:
        lines = f.readlines()[::-1]
        return max(lines, key = lambda x: len(x.split()))
print(most_talkative_line('todo_list.txt'))





# def most_talkative_line(fname: str) -> str:
#     with open(fname, "r", encoding="utf-8") as f:
#         ma = float("-inf")
#         res = ""
#         for line in f:
#             if (cur := len(line.strip().split())) >= ma:
#                 ma = cur
#                 res = line
#     return res

#
# Моржовый оператор (:=): Вы одновременно присваиваете значение переменной cur и проверяете его в if. Это делает код компактнее.
#
# float("-inf"): Использование «минус бесконечности» для инициализации максимума — профессиональный подход, гарантирующий корректную работу даже с почти пустыми файлами.
#
# len(line.strip().split()): Вы четко считаете количество слов, предварительно очистив строку от лишних пробелов и переносов.
#
# >= ma: Правильно реализовано условие «выбрать последнюю», если количество слов совпадает.




# Задание 3: numbers.txt
# количество трехзначных чисел;
# сумму двухзначных чисел.


def numbers_task(file_name: str):
    with open(file_name, 'r') as f:
        count = 0
        summa = 0
        # Читаем файл целиком и разбиваем на отдельные «слова» (числа)
        words = f.read().split()

        for word in words:
            # Проверяем длину самого СЛОВА (числа)
            if len(word) == 2:
                summa += int(word)  # Превращаем в число и прибавляем к сумме
            elif len(word) == 3:
                count += 1

        return f"Количество трехзначных чисел: {count}/ сумма двухзначных чисел: {summa}"
print(numbers_task('numbers.txt'))







## Задание 4: Уникальные слова
# Принимает на вход имя текстового файла
#
# Считывает всё содержимое файла;
#
# Делит текст на слова, считая, что они разделяются пробелами;
#
# Удаляет из слов все знаки пунктуации из следующего набора
#
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# Создает из всех слов список всех уникальных слов, записанных в нижнем регистре и расположенных в алфавитном порядке.
# Данный список нужно вернуть в качестве результата работы функции




#
#
# import string
#
#
# def get_unique_words(file_name):
#     # 1. открыть файл и прочитать текст
#     with open(file_name, 'r') as f:
#         text = f.read()
#         unique = set()
#     # 2. разбить на слова через split()
#         words = text.split()
#         for word in words:
#             cleaned = word.lower().strip(string.punctuation)
#             if cleaned:
#                 unique.add(cleaned)
#
#     return sorted(unique)
# print(get_unique_words('Shawshank_hope_txt'))


#
#
# def get_unique_words(file_name):
#     # 1. открыть файл и прочитать текст
#     with open(file_name, 'r') as f:
#         text = f.read().split()
#         unique_words = {word.lower().strip(string.punctuation) for word in text if word.strip(string.punctuation)}
#         return sorted(unique_words)
# print(get_unique_words('Shawshank_hope_txt'))

# def get_unique_words(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         return sorted({w.lower().strip(string.punctuation) for w in f.read().split() if w.strip(string.punctuation)})
# print(get_unique_words('Shawshank_hope_txt'))












# Решение задачи с удалением символов не только по краям слова, но и внутри, translate() — это встроенный метод строки - заменяет или удаляет символы в строке по таблице замен.

# Таблицу создаёт str.maketrans():
# python три аргумента: что заменить, на что заменить, что удалить
# translator = str.maketrans('', '', '!?,.')

# def get_unique_words(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         unique_words = set()
#         for word in f.read().split():
#             cleaned  = "".join(x for x  in word.lower() if word.isalpha())
#             if cleaned:
#                 unique_words.add(cleaned)
#         return sorted(unique_words)
# print(get_unique_words('Shawshank_hope_txt'))


# import string
#
# def get_unique_words(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         translator = str.maketrans('', '', string.punctuation)
#         words = f.read().split()
#         unique_words = {w.lower().translate(translator) for w in words if w.translate(translator)}
#         return sorted(unique_words)


# метод строк  str.maketrans
# # 1. Удаление символов
# translator = str.maketrans('', '', '!?.,')
# "Hello, World!".translate(translator)
# # → "Hello World"
#
# # 2. Замена символов
# translator = str.maketrans('aeiou', '12345')
# "hello world".translate(translator)
# # → "h2ll4 w4rld"
#
# # 3. Замена и удаление одновременно
# translator = str.maketrans('aeiou', '12345', '!?.')
# "hello, world!".translate(translator)
# # → "h2ll4, w4rld"
#
# # 4. Замена букв — транслитерация
# translator = str.maketrans('abcdefghij', 'абсдефгхий')
# "hello".translate(translator)
# # → "хелло"  (частичная транслитерация)
#
# # 5. Шифр Цезаря — сдвиг букв
# import string
# abc = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
# shifted = abc[3:] + abc[:3]   # сдвиг на 3: 'defghijklmnopqrstuvwxyzabc'
# translator = str.maketrans(abc, shifted)
# "hello".translate(translator)
# # → "khoor"


#
# def get_unique_words(file_name):
#     del_symbols = r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#     with open(file_name, 'r', encoding='utf-8') as f:
#         return sorted(set(map(lambda word: word.lower().strip(del_symbols).replace("'", ""), f.read().split())))
# print(get_unique_words('Shawshank_hope_txt'))










# Задача 5:Сумма по каждому отделу

# def sum_columns(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         for n, i in enumerate(f,1):
#             print(f'{n}: {i}')
#
#
#
# sum_columns('квартальный отчет.txt')

def sum_columns(filename):
    with open(filename,  'r', encoding='utf-8') as f:
        # 1. первую строку берём как начальный список сумм

        lines = [list(map(int, line.split())) for line in f]
        # 2. для каждой следующей строки — складываем через zip
        sums = lines[0]
        for row in lines[1:]:
            sums = [a + b for a, b in zip(sums, row)]

        return sums


# print(sum_columns('квартальный отчет.txt'))




def sum_columns(filename):
    with open(filename) as file:
        return [sum(map(int, x)) for x in zip(*map(str.split, file))]

# print(sum_columns('квартальный отчет.txt'))


def sum_columns(filename):
    with open(filename,  'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(list(map(int, line.split())))
        sums = lines[0]
        for row in lines[1:]:
            sums = [a + b for a, b in zip(sums, row)]
        return sums
# print(sum_columns('квартальный отчет.txt'))




# Задание 6: самое длинное слово




from string import punctuation

def longest_word_in_file(file: str):
    with open(file, "r", encoding="utf-8") as f:
        translator = str.maketrans("", "", punctuation)
        return max((word.lower().translate(translator) for word in f.read().split()), key=len)
# print(longest_word_in_file('Shawshank_hope_txt'))
from string import punctuation


def longest_word_in_file(file: str):
    with open(file, "r", encoding="utf-8") as f:
        clean_words = []
        for word in f.read().split():
            cleaned = word.strip(punctuation)
            if cleaned:
                clean_words.append(word)
        return max(reversed(clean_words), key=len)
# print(longest_word_in_file('Shawshank_hope_txt'))

from string import punctuation


def longest_word_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        # Очищаем слова от знаков и фильтруем пустые строки
        words = [w.strip(punctuation) for w in f.read().split()]

        # Переворачиваем список и находим максимум по длине
        return max(reversed(words), key=len)
# print(longest_word_in_file('Shawshank_hope_txt'))

from string import punctuation


def longest_word_in_file(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        # Создаем таблицу перевода, которая заменяет все знаки пунктуации на None
        translator = str.maketrans('', '', punctuation)

        longest_word = ""

        for line in file:
            words = line.split()
            for word in words:
                # Удаляем пунктуацию из любой части слова
                clean_word = word.translate(translator)

                # Если длина текущего слова больше или равна максимальной,
                # обновляем переменную (равенство обеспечит выбор последнего слова)
                if len(clean_word) >= len(longest_word):
                    longest_word = clean_word

    return longest_word
# print(longest_word_in_file('Shawshank_hope_txt'))






# Задание 7: лучший студент

def get_best_student(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        best_name = None
        best_score = -1

        for line in file:
            parts = line.strip().split(':')
            name = parts[0].strip()  # "Иванов Иван"
            first, last = name.split()  # first="Иванов", last="Иван"  # "Иван Иванов"
            score = int(parts[1].strip())

            if score >= best_score:  # >= берёт последнего при равных
                best_score = score
                best_name = f"{last} {first}"

        return best_name



print(get_best_student('баллы'))

#
# def get_best_student(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
