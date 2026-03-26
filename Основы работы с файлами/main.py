# file = open('i_love_python.txt', 'r')
# text = file.read()
# print(text)
# # print(repr(text)) строка со всеми специальными символами
# file.close()









# def print_file_content(file_name: str) -> None:
#     file = open(file_name, 'r')
#     text = file.read()
#     print(text)
#     file.close()
# print_file_content('breaking_bad.txt')













# Подсчёт строк в файле




# def count_lines_in_file(file_name: str) -> None:
#     with open(file_name, 'r') as f:
#         content = f.read()
#         if not content:  # Если файл абсолютно пустой
#             return 0
#
#         # Считаем все \n
#         count = content.count('\n')
#
#         # Если файл НЕ заканчивается на \n, значит есть "хвост",
#         # который тоже считается строкой (+1)
#         if not content.endswith('\n'):
#             count += 1
#
#         return count
#
# print(count_lines_in_file('office.txt'))



#
# def count_lines_in_file(fname: str) -> int:
#     with open(fname) as f:
#         res = sum(map(bool, f))
#     return res

# def count_lines_in_file(file_name: str) -> None:
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         # lines теперь список: ['Первая строка\n', 'Вторая\n', 'Третья']
#         print(len(lines)) # Выведет общее количество строк
# count_lines_in_file('office.txt')



















# Сравнение содержимого файлов


# def compare_files(file1: str, file2: str) -> None:
#     with open(file1, "r") as f1, open(file2, "r") as f2:
#         return f1.read() == f2.read()
# print(compare_files('office.txt', 'i_love_python.txt'))
#
#
# compare_files = lambda f1, f2: open(f1).read() == open(f2).read()







# Сколько раз ты это сказал?

# def count_word_in_file(filename, phrase):
#     with open(filename, 'r', encoding='utf-8') as file:
#         content = file.read().lower()  # Читаем всё и переводим в нижний регистр
#         return content.count(phrase.lower()) # Считаем вхождения фразы






# Самое длинное палиндромное слово
#
def longest_palindrome(filename):
    file = open(filename, 'r')
    content = file.read().split()
    longest = ""
    file.close()

    for word in content:
        if word.lower() == word.lower()[::-1]:
            if len(word) > len(longest):
                longest = word

    return longest


print(longest_palindrome('secretcode.txt'))
#
#
#
# def longest_palindrome(filename):
#     file = open(filename, 'r')
#     content = file.read().split()
#     file.close()
#
#     palindrome_list = [word for word in content if word.lower() == word.lower()[::-1]]
#     max_len = max(palindrome_list, key=len)
#     return max_len
#
# print(longest_palindrome('secretcode.txt'))


# longest_palindrome = lambda fn: max([w for w in open(fn).read().split() if w.lower() == w[::-1].lower()], key=len)
# print(longest_palindrome('secretcode.txt'))