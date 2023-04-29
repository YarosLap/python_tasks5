# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.

import random

numbers = [random.randint(1, 10) for _ in range(6)]
print(numbers)
result = lambda x: x > 5
numbers = list(filter(result, numbers))
print(numbers)