
# Работа с файлами в Python
file = open(r'/Users/senya/ Работа с файлами/111.txt',encoding='utf-8')
# print(file.read())

# 1 - ЧТЕНИЕ ФАЙЛОВ
file = open('111.txt',encoding='utf-8')
# print(file.read(3)) #берем первые три символа
# print(file.read(3)) #программа начинает с того места, где остановилась


file.seek(0)#позволяет откатиться к указанному элементу
# print(file.read(3))


# построчный вывод
# print(file.readline())
# print(file.readline())


#проход по строкам
# for row in file:
#     print(row)

#проход по буквам
# for row in file:
#     for letter in row:
#         print(letter)


# s = file.readlines()
# print(s)




# 2 - ЗАПИСЬ ФАЙЛОВ
# file = open('111.txt','w', encoding='utf-8')
# file.write('Новое стихотворение\n')
# file.write('Новое стихотворение\n')


# file = open('111.txt','a', encoding='utf-8')
# file.write('Дополнение\n')



#Всегда необэодима закрывать файл в конце обработки
file.close()
