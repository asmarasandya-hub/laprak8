import numpy as np
import matplotlib.pyplot as plt

# Data jam belajar dan nilai ujian
x = np.array([1, 2, 2, 3, 4, 4, 5, 6])
y = np.array([55, 60, 62, 65, 70, 72, 75, 82])

# Menghitung regresi linear
koefisien = np.polyfit(x, y, 1)

a = koefisien[0]
b = koefisien[1]

# Persamaan regresi
print("Persamaan regresi:")
print(f"y = {a:.2f}x + {b:.2f}")

# Prediksi nilai baru
jam_baru = 7
prediksi = a * jam_baru + b

print("Prediksi nilai untuk 7 jam belajar:", round(prediksi, 2))

# Membuat grafik
plt.scatter(x, y, label="Data asli")
plt.plot(x, a*x+b, color="red", label="Garis regresi")

plt.xlabel("Jam Belajar")
plt.ylabel("Nilai Ujian")
plt.title("Regresi Linear Jam Belajar dan Nilai Ujian")
plt.legend()
plt.grid()

plt.show()

# Menghitung nilai prediksi seluruh data
y_prediksi = a * x + b

# Menghitung residual
residual = y - y_prediksi

# Menghitung jumlah residual
jumlah_galat = np.sum(residual)

# Menghitung jumlah kuadrat galat
jumlah_kuadrat_galat = np.sum(residual**2)

print("Residual:", residual)
print("Jumlah galat:", jumlah_galat)
print("Jumlah kuadrat galat:", jumlah_kuadrat_galat)