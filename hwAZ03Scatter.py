import matplotlib.pyplot as plt
import numpy as np
# Генерация случайных данных для первого набора
x1 = np.random.rand(50)
y1 = np.random.rand(50)

# Генерация случайных данных для второго набора
x2 = np.random.rand(50)
y2 = np.random.rand(50)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x1, y1, color='blue', label='Набор данных 1', alpha=0.6)
plt.scatter(x2, y2, color='red', label='Набор данных 2', alpha=0.6)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния двух наборов данных')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Добавление легенды
plt.legend()

# Показ графика
plt.grid()
plt.show()
