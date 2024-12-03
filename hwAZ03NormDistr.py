import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Настройки для визуализации
sns.set(style="whitegrid")

# Параметры для первого набора данных
mean1 = 0  # Среднее
std_dev1 = 1  # Стандартное отклонение
size1 = 1000  # Размер выборки

# Генерация первого набора данных
data1 = np.random.normal(mean1, std_dev1, size1)

# Параметры для второго набора данных
mean2 = 5  # Среднее
std_dev2 = 2  # Стандартное отклонение
size2 = 1000  # Размер выборки

# Генерация второго набора данных
data2 = np.random.normal(mean2, std_dev2, size2)

# Построение гистограммы для первого набора данных
plt.hist(data1, bins=30, density=True, alpha=0.6, color='blue', label='Набор данных 1 (μ=0, σ=1)')

# Построение гистограммы для второго набора данных
plt.hist(data2, bins=30, density=True, alpha=0.6, color='red', label='Набор данных 2 (μ=5, σ=2)')

# Создание диапазона значений для построения функции плотности
x = np.linspace(-5, 10, 1000)

# Вычисление функции плотности вероятности (PDF) для первого набора данных
pdf1 = (1 / (std_dev1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean1) / std_dev1) ** 2)

# Вычисление функции плотности вероятности (PDF) для второго набора данных
pdf2 = (1 / (std_dev2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean2) / std_dev2) ** 2)

# Построение линий плотности для обоих наборов данных
plt.plot(x, pdf1, color='blue', linewidth=2)
plt.plot(x, pdf2, color='red', linewidth=2)

# Добавление заголовка и меток
plt.title('Нормальное распределение двух наборов данных')
plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')

# Добавление легенды
plt.legend()

# Показ графика
plt.grid()
plt.show()
