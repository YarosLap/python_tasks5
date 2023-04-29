# Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.

import random

numbers = [random.randint(1, 10) for i in range (10)]
print(numbers)

result = [0]

while len(result) < 2:
    index = random.randint(0, 9)  
    result = [numbers[index]]
    for i in numbers[index:]:
        if i > result[len(result)-1]:
            result.append(i)    
        
print(result)    