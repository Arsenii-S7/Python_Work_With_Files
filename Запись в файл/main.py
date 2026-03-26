# ПРАКТИКА
# Задание 1: Список покупок
def save_shopping_list(items: list):
    with open('shopping.txt', 'w') as f:
        f.write('Список покупок:\n')
        for n, v in enumerate(items, 1):
            f.write(f'{n}. {v}\n')

# save_shopping_list(['Хлеб', 'Молоко', 'Яйца'])
# save_shopping_list(["Apples", "Bananas", "Carrots", "Dates", "Eggs"])

# with open('shopping.txt', 'r', encoding='utf-8') as f:
#     print(f.read())


# Задание 2: Файл наоборот

# 1 вариант
def reverse_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
       text = file.readlines()
       text = [line if line.endswith('\n') else line + '\n' for line in text]
       with open('reversed.txt', 'w', encoding='utf-8') as f:
            f.writelines(reversed(text))

# reverse_lines('terminator.txt')
#
#
# with open('reversed.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
#
# reverse_lines('dialog.txt')
#
# with open('reversed.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# 2 вариант
# def reverse_lines(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     with open('reversed.txt', 'w', encoding='utf-8') as f:
#         for line in reversed(lines):
#             if not line.endswith('\n'):
#                 line += '\n'
#             f.write(line)






# Задание 3: Очистка от копипасты
# 1 вариант сохраняет порядок
def remove_duplicate_lines(filename: str, output_filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        seen = set()
        result = []
        for line in lines:
            cleaned = line.strip('\n')
            if cleaned and cleaned not in seen:
                seen.add(cleaned)
                result.append(cleaned)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))




# remove_duplicate_lines('meetings.txt', 'cleaned_meetings.txt')
#
# with open('cleaned_meetings.txt', 'r', encoding='utf-8') as f:
#     print(f.read())


# 2 вариант не сохраняет порядок
def remove_duplicate_lines(filename: str, output_filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        cleaned_lines = [line.strip('\n') for line in file.readlines()]
        result = set(cleaned_lines)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))


# remove_duplicate_lines('meetings.txt', 'cleaned_meetings.txt')
#
# with open('cleaned_meetings.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# 3 вариант сохраняет порядок
def remove_duplicate_lines(filename: str, output_filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = dict.fromkeys(l.strip('\n') for l in f if l.strip('\n'))

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))



# remove_duplicate_lines('meetings.txt', 'cleaned_meetings.txt')
#
# with open('cleaned_meetings.txt', 'r', encoding='utf-8') as f:
#     print(f.read())




# Задание 4: Уборка архива
# 1 вариант
def clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        result = []
        for line in lines:
            if not line.strip():
                continue
            result.append(line)
    with open('cleaned.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(result))

# clean_file('star_wars.txt')
#
# with open('cleaned.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# 2 вариант

def clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line for line in file.readlines() if line.strip()]
    with open('cleaned.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)
# clean_file('star_wars.txt')
#
# with open('cleaned.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# 3 вариант
def clean_file(filename:str):
    with open(filename) as f1, open('cleaned.txt', 'w') as f2:
        f2.writelines(s for s in f1 if s.strip())



# Задание 5: Статистика по песне


def export_song_stats(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = [a.strip() for a in  file.readlines() if a.strip()]
        with open('stats.txt', 'w', encoding='utf-8') as f:
            for num, val in enumerate(text, 1):
                f.write(f'Строка {num}: {len(val)} символов\n')

export_song_stats('lyrics.txt')
with open('stats.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# "  привет  ".strip()    # → "привет"   — убрал с обеих сторон
# "  привет  ".rstrip()   # → "  привет" — убрал только справа
# "  привет  ".lstrip()   # → "привет  " — убрал только слева
# Условие изменилось — теперь пустые строки не пропускаем, а считаем их длину как 0. И формат вывода
def export_song_stats(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = [a.rstrip('\n') for a in file.readlines()]

    with open('stats.txt', 'w', encoding='utf-8') as f:
        for num, val in enumerate(text, 1):
            f.write(f'Строка {num}: {len(val.rstrip())} символов\n')

# export_song_stats('lyrics.txt')
# with open('stats.txt', 'r', encoding='utf-8') as f:
#     print(f.read())



def export_song_stats(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as f_read, \
            open('stats.txt', 'w', encoding='utf-8') as f_write:
        for i, line in enumerate(f_read, 1):
            f_write.write(f'Строка {i}: {len(line.strip())} символов\n')
#
# export_song_stats('lyrics.txt')
# with open('stats.txt', 'r', encoding='utf-8') as f:
#     print(f.read())



#Задание 6: Сохранение шахматной доски в файл


def save_board(n):
    with open("chess_board.txt", "w") as f:
        for i in range(n):
            row = ""
            for j in range(n):
                row += "#" if (i + j) % 2 == 0 else "."
            f.write(row + "\n")
# save_board(5)




#Задание 7: Генерация файла с числами
def create_file_with_numbers(n):
    with open(f"range_{n}.txt", "w") as f:
        for i in range(1, n + 1):
            f.write(str(i) + "\n")
# create_file_with_numbers(4)
#
# with open('range_4.txt', 'r', encoding='utf-8') as f:
#     print(f.read())


# Задание 8: Битва языков программирования
results = {
    "Python": 38,
    "JavaScript": 25,
    "C++": 12,
    "Java": 17
}


def export_poll_results(results):
    with open('results.txt', 'w', encoding='utf-8') as f:
        f.write('Результаты опроса:' + '\n')
        filtered_results = sorted(results, key=lambda x: results[x], reverse=True)
        for num, language in enumerate(filtered_results, 1):
            f.write(f'{num}. {language} — {results[language]} голосов\n')

export_poll_results(results)

# with open('results.txt', 'r', encoding='utf-8') as f:
#     print(f.read())



# Задание 9: Финал Большого голосования

def export_poll_results(*args):

        total_votes = {}

        for poll in args:
            for lang, count in poll.items():
                total_votes[lang] = total_votes.get(lang, 0) + count

        grouped = {}
        for lang, count in total_votes.items():
            grouped.setdefault(count,[]).append(lang)

        sorted_votes = sorted(grouped.keys(), reverse=True)

        with open('results.txt', 'w', encoding='utf-8') as file:
            file.write('Итоги общего голосования:\n')
            for i, count in enumerate(sorted_votes, 1):
                langs_str = ', '.join(sorted(grouped[count]))
                file.write(f"{i}. {langs_str} — {count} голосов\n")


export_poll_results(
    {"Python": 12, "C++": 8, "Go": 9, "Swift": 6},
    {"Rust": 12, "Kotlin": 8, "Ruby": 6},
    {"Python": 3, "Go": 6, "Swift": 4, "Rust": 1},
    {"Kotlin": 2, "Ruby": 4, "JavaScript": 7}
)


with open('results2.txt', 'r', encoding='utf-8') as f:
    print(f.read())





# Задание 10: Генератор чеков


def generate_receipt(purchases):
    with open('receipt.txt', 'w', encoding='utf-8') as file:
        file.write('==== Чек покупок ====\n')
        total_sum = 0
        for i, item in enumerate(purchases, 1):
            # Достаем данные (просто по ключу, без pop)
            name = item['название']
            price = round(item['цена'], 2)
            qty = round(item['количество'], 2)

            # Считаем сумму позиции
            subtotal = price * qty
            total_sum += subtotal

            # Формируем строку по шаблону
            line = f"{i}. {name} ({qty:.2f} × {price:.2f}) = {subtotal:.2f}\n"

            file.write(line)


        file.write('---------------------\n')
        file.write(f'ИТОГО: {total_sum:.2f} руб\n')
        file.write('======================')




purchases = [
    {"название": "Шоколад", "цена": 99.99, "количество": 2},
    {"название": "Сок", "цена": 50.5, "количество": 1.2}
]
generate_receipt(purchases)

with open('receipt.txt', 'r', encoding='utf-8') as f:
    print(f.read())


# Задание 11: Морской бой: обновление карты

import json

def mark_hits(field_file, shots_file):
    # 1. ЗАГРУЗКА ПОЛЯ (превращаем текстовый файл в список списков)
    with open(field_file, 'r', encoding='utf-8') as f:
        # line.split() разрезает строку по пробелам: ['~', '■', '~', ...]
        field = [line.split() for line in f]

    # 2. ЧТЕНИЕ ВЫСТРЕЛОВ
    with open(shots_file, 'r', encoding='utf-8') as f:
        # strip() убирает невидимые символы переноса строки \n
        shots = [line.strip() for line in f if line.strip()]

    # Алфавит для перевода букв в индексы (A=0, B=1...)
    alphabet = "ABCDEFGHIJ"

    # 3. ОБРАБОТКА ВЫСТРЕЛОВ
    for shot in shots:
        # Разбираем координату, например "B2" или "J10"
        letter = shot[0]          # Берем первую букву ('B')
        number = int(shot[1:])    # Берем всё остальное и делаем числом (2 или 10)

        # Переводим в понятные Python индексы (от 0 до 9)
        col = alphabet.find(letter) # Находим позицию буквы в алфавите
        row = number - 1            # Вычитаем 1, так как в списках всё с нуля

        # 4. ЛОГИКА ПОПАДАНИЯ (меняем символ прямо в нашей матрице field)
        if field[row][col] == '■':
            field[row][col] = 'X'
        elif field[row][col] == '~':
            field[row][col] = '•'

    # 5. СОХРАНЕНИЕ ОБНОВЛЕННОГО ПОЛЯ
    with open('updated_field.txt', 'w', encoding='utf-8') as f:
        for row_list in field:
            # Склеиваем символы списка обратно в строку через пробел
            f.write(" ".join(row_list) + "\n")



mark_hits('field_1.txt', 'shots_1.txt')

with open('updated_field.txt', 'r', encoding='utf-8') as f:
    print(f.read())











