# Написать программу, которая:
# - Запрашивает у пользователя строку для поиска.
# - Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.
# - Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их.

podstr = input("Введите строку для поиска: ") #Запрос строки от пользователя

with open('text.txt', 'r', encoding='utf-8') as file: #Открываем файл в режиме чтения 
    strk = file.readlines() #Считывание строк
    
lines = [] #Создание списка

for line in strk: #Цикл
    if podstr in line: #Проверка подстроки 
        lines.append(line) #Добавление строк в список без пробелов 
        
lenLines = len(lines) #Количество найденых строк
print("Количество строк с подстрокой: {}".format(lenLines)) #Вывод на экран

for line in lines: #Цикл
    print(line) #Вывод на экран
    
sorted_lines = sorted(lines, key = len) #Сортируем список по длине строк
print("Сортированные строки: ") #Вывод на экран
for line in sorted_lines: #Цикл отсортированных строк
    print(line) #Вывод на экран
