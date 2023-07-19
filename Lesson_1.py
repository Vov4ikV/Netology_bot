# Списки и операции над ними
strings = ['Hello', 'world']
numbers = [1, 2, 3, 4, 5]
data = ['hello', 1]

print(strings)
print(numbers)
print(data)

# Консоль выведет:
# ['Hello', 'world']
# [1, 2, 3, 4, 5]
# ['hello', 1]

summa = numbers + data
print(summa)
# Консоль выведет:
# [1, 2, 3, 4, 5, 'hello', 1] Это означает, что списки можно складывать, а так же различные типы данных в них

numbers.append(6)
print(numbers)

# Консоль выведет:
# [1, 2, 3, 4, 5, 6], свойство .append позволяет добавлять элемент в конец списка

first = strings[0]
second = strings[1]
print(first)
print(second)

# Консоль выведет:
# Hello
# world
# Таким образом моно выводить каждый элемент списка отдельно

strings_lenght = len(strings)
print(strings_lenght)
# Консоль выведет: 2
# Функция len() позволяет вывести количество элементов в списке

s = sum(numbers)
print(s)

# Консоль выведет: 21
# Функция sum() позволяет сложить все элементы в списке


numbers_2 = [1, 2, 3, 4, 5, 'Hello']
s_2 = sum(numbers_2)
print(s_2)

# Консоль выведет:
# Traceback (most recent call last):
#   File "/home/vladimir/PycharmProjects/Netology_bot/List.py", line 49, in <module>
#     s_2 = sum(numbers_2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Операция sum() не позволяет складывать разные типы данных

