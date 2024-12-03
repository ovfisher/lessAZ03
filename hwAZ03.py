import matplotlib.pyplot as plt
import numpy as np

# Генерация случайных чисел, распределенных по нормальному распределению
# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 10000  # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)
plt.title("Гистограмма нормального распределения")
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.hist(data, bins=100)
plt.show()

