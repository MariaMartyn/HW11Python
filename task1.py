# Задача 1. Постройте график функции
# 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = 5 * x * x + 10 * x - 30
plt.figure(1)
plt.title('График функции f(x)=5x^2+10x-30')
plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.grid(axis='y', c='b')
plt.grid(axis='x', c='g')

plt.plot(x, y, 'r')
plt.show()


