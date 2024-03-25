import numpy as np
import matplotlib.pyplot as plt

sales_data = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])

mean_sales = np.mean(sales_data)  
weighted_mean_sales = np.average(sales_data, weights=range(1, 11))  
max_sales = np.max(sales_data)  
min_sales = np.min(sales_data)  

print(f"Среднее значение продаж: {mean_sales}")
print(f"Средневзвешенное значение продаж: {weighted_mean_sales}")
print(f"Максимальное значение продаж: {max_sales}")
print(f"Минимальное значение продаж: {min_sales}")

plt.figure(figsize=(8, 6))
plt.plot(sales_data, marker='o', linestyle='-', color='b')
plt.title('Продажа товаров')
plt.xlabel('Дни')
plt.ylabel('Продажи')
plt.grid(True)
plt.show()
