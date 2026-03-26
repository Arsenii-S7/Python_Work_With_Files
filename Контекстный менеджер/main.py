# Страховка по-старому: try … finally
# Если вы выбираете использовать блок try-finally для гарантии закрытия файла,
# то шаблон «открыл файл → поработал → обязательно закрыл» реализуется через него следующим образом:
# import string


# file = open("data.txt", "r", encoding="utf-8")
# try:
#     text = file.read()
#     print("Длина файла:", len(text))
# finally:
#     file.close()  # выполнится всегда, даже если выше была ошибка

#
# Вот как будет выглядеть программа, которая ищет слово «Python» внутри файла

# file = open("data.txt", "r", encoding="utf-8")
# try:
#     text = file.read()
#     pos = text.index("Python")  # может кинуть ValueError
#     print("Нашли 'Python' на позиции:", pos)
# finally:
#     file.close()


# программа, которая суммирует все числа в файле.

# file = open("logs.txt", "r", encoding="utf-8")
# try:
#     total = 0
#     for line in file:
#         total += int(line.strip())  # может кинуть ValueError на «плохой» строке
#     print("Сумма:", total)
# finally:
#     file.close()



# ✅ Современное решение: контекстный менеджер

# Шаблон использования with

# with выражение as переменная:
    # блок кода, в котором используется ресурс
    # здесь можно читать или записывать в файл
# после выхода из блока файл автоматически закрывается

# with open("data.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     print("Файл прочитан:", text)

# Здесь файл уже закрыт автоматически, даже если выше случилась ошибка





# Убедиться в том, что файл действительно закрылся, можно,
# проверив состояние файла до и после выхода из блока.
# В атрибуте .closed хранится ответ на вопрос, закрыт ли файл на текущий момент или нет.


# try:
#     with open("top_score_4.txt", "r", encoding="utf-8") as file:
#         print('Файл закрыт?', file.closed)  # False
#         pos = file.read().index("Python")  # вызовет ValueError
#         print("Слово найдено на позиции:", pos)
# except ValueError:
#     print("Слово 'Python' не найдено")
#
# # Проверим, закрыт ли файл
# print('Файл закрыт?', file.closed)  # True




# Задача 1: Строки длиннее шести символов
#
# def find_lines_len_more_6(file: str):
#     with open(file, 'r', encoding = 'utf-8') as file:
#         count = 0
#         for line in file:
#             word = line.strip()
#             if len(word) > 6:
#                 count += 1
#         return count
#
#
#
# print(find_lines_len_more_6('test1.txt'))



# def find_lines_len_more_6(file: str):
#     with open(file, 'r', encoding = 'utf-8') as file:
#
#         words = [w for w in file.read().split() if len(w) > 6]
#         return len(words)

# print(find_lines_len_more_6('test1.txt'))




# Вариант 1 — твой (генератор списка)
# def find_lines_len_more_6(file: str):
#     with open(file, 'r', encoding = 'utf-8') as file:
#         return len([w.strip() for w in file.read().split() if len(w) > 6])
# print(find_lines_len_more_6('test1.txt'))




# Вариант 2 — обычный цикл
# def find_lines_len_more_6(file: str):
#     with open(file, 'r', encoding='utf-8') as f:
#         count = 0
#         for line in f:
#             if len(line.strip()) > 6:
#                 count += 1
#         return count


# Вариант 3 — filter
# def find_lines_len_more_6(file: str):
#     with open(file, 'r', encoding='utf-8') as f:
#         return len(list(filter(lambda w: len(w) > 6, f.read().split())))
# print(find_lines_len_more_6('test1.txt'))


# Вариант 4 — sum с генератором (питоновский)
# def find_lines_len_more_6(file: str):
#     with open(file, 'r', encoding='utf-8') as f:
#         return sum(1 for w in f.read().split() if len(w) > 6)
# print(find_lines_len_more_6('test1.txt'))




# Задача 2: Уникальные слова в тексте

# import string
# def count_unique_words(filename):
#     with open(filename, 'r', encoding = 'utf-8') as file:
#         return len(set([w.lower().strip(string.punctuation) for w in file.read().split() if w.strip(string.punctuation)]))
# print(count_unique_words('test2.txt'))
#
# # знаков пунктуациии нет, поэтому можно не убирать знаки препинания
# def count_unique_words(fn):
#     with open(fn, encoding='utf-8') as f:
#         return len(set(f.read().lower().split()))


# Задача 3: Частота слов в файле
# def word_frequencies(filename):
#     with open(filename, 'r', encoding = 'utf-8') as file:
#         d = {}
#         for line in file:
#             words = line.split()
#             for word in words:
#                 key = word.upper()
#                 d[key] = d.get(key, 0) + 1
#
#         return d
# print(word_frequencies('test3.txt'))


# def word_frequencies(filename):
#     with open(filename, 'r', encoding = 'utf-8') as file:
#
#         res = list(map(str.upper, file.read().split()))
#         return {el: res.count(el) for el in res}
# print(word_frequencies('test3.txt'))


# def word_frequencies(file_name):
#     with open(file_name, encoding='utf-8') as file:
#         result_dict = {}
#
#         for line in file:
#             for word in line.upper().split():
#                 result_dict[word] = result_dict.get(word, 0) + 1
#
#         return result_dict
# print(word_frequencies('test3.txt'))

# Задача 4: Шея, фея, затея ...

def find_words_ending_with_eya(file: str):
    with open(file, 'r', encoding = 'utf-8') as file:
        words = set()
        for i in file.read().split():
            word = i.upper()
            if word.endswith('ЕЯ'):
                words.add(word)
        for word in sorted(words, key=lambda w: (len(w), w)):
                print(word)
# print(find_words_ending_with_eya('test4.txt'))


def find_words_ending_with_eya(file: str):
    with open(file, 'r', encoding = 'utf-8') as file:
        words = []
        for i in file:
            word = i.upper().strip()
            if word.endswith('ЕЯ'):
                words.append(word)
        for word in sorted(set(words), key=lambda w: (len(w), w)):
            print(word)
# find_words_ending_with_eya('test4.txt')

#
# def find_words_ending_with_eya(file: str):
#     with open(file, 'r', encoding = 'utf-8') as file:
#         print(*sorted({w.upper() for w in file.read().split() if w.upper().endswith('ЕЯ')},
# key=lambda w: (len(w), w)), sep='\n')
# find_words_ending_with_eya('test4.txt')






# Задача 5: ⚓ Морской бой: проверка попаданий

def check_hits(shots_file, ships_file):
    with open(shots_file, 'r', encoding = 'utf-8') as file1, open(ships_file, 'r', encoding = 'utf-8') as file2:

        shot = set(map(str.strip, file1.readlines()))
        ships = set(map(str.strip, file2.readlines()))
        result = len(shot & ships)
        return result
#
# print(check_hits('shots_alpha.txt', 'ships_alpha.txt'))


def check_hits(shots_file, ships_file):
    with open(shots_file) as f1, open(ships_file) as f2:
        return len({s.strip() for s in f1} & {s.strip() for s in f2})












# Задача 5: ⚓ Морской бой: подсчёт потопленных кораблей
def count_destroyed_ships(ships_file, shots_file):
    with  open(shots_file) as f1:
        shots = {s.strip() for s in f1}





    count = 0
    with open(ships_file) as f2:
        for line in f2:
            if line.strip():
                ship = set(line.split())
                if ship.issubset(shots):
                    count += 1
    return count








print(count_destroyed_ships('ships_1.txt', 'shots_1.txt',))




