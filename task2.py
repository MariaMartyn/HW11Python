# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список 
# подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import matplotlib.pyplot as plt
import numpy as np

price_houses = np.random.randint(3000000, 20000001, 15)
area_house = np.random.randint(100, 301, 15)

price_onemetr = []
for i in range(len(price_houses)):
    price_onemetr.append(round((price_houses[i] / area_house[i]), 2))

print(price_onemetr)
count_houses = []
for i in range(len(price_houses)):
    count_houses.append(i+1)

plt.title('Данные о стоимости 1 кв.м. квартир')
plt.ylabel('Цена за 1 кв.м.')
plt.xlabel('Порядковый номер дома')
plt.bar(count_houses, price_onemetr)
print()

sorted_price_houses = []
sorted_number_houses = []
for i in range(len(price_onemetr)):
    if price_onemetr[i] < 50000:
        sorted_price_houses.append(price_onemetr[i])
        sorted_number_houses.append(i+1)
    
print(f'Дома со стоимостью ниже 50т.р. за 1 кв.м.: ')
for i in range(len(sorted_price_houses)-1):
    print(f'У дома номер {sorted_number_houses[i+1]} цена за 1 кв.м. составляет {sorted_price_houses[i+1]}')

plt.show()