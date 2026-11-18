import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Program Curve Fitting")
st.subheader("Regresi Linear Jam Belajar dan Nilai Ujian")

# Data jam belajar dan nilai ujian
x = np.array([1, 2, 2, 3, 4, 4, 5, 6])
y = np.array([55, 60, 62, 65, 70, 72, 75, 82])

# Menghitung regresi linear
koefisien = np.polyfit(x, y, 1)

a = koefisien[0]
b = koefisien[1]

# Persamaan regresi
st.write("### Persamaan Regresi")
st.write(f"y = {a:.2f}x + {b:.2f}")

# Prediksi nilai baru
jam_baru = 7
prediksi = a * jam_baru + b

st.write("### Prediksi Nilai")
st.write("Prediksi nilai untuk 7 jam belajar:", round(prediksi, 2))

# Membuat grafik
fig, ax = plt.subplots()

ax.scatter(x, y, label="Data asli")
ax.plot(x, a*x+b, color="red", label="Garis regresi")

ax.set_xlabel("Jam Belajar")
ax.set_ylabel("Nilai Ujian")
ax.set_title("Regresi Linear Jam Belajar dan Nilai Ujian")
ax.legend()
ax.grid()

st.pyplot(fig)

# Menghitung nilai prediksi seluruh data
y_prediksi = a * x + b

# Menghitung residual
residual = y - y_prediksi

# Menghitung jumlah residual
jumlah_galat = np.sum(residual)

# Menghitung jumlah kuadrat galat
jumlah_kuadrat_galat = np.sum(residual**2)

st.write("### Hasil Perhitungan Galat")
st.write("Residual:", residual)
st.write("Jumlah galat:", jumlah_galat)
st.write("Jumlah kuadrat galat:", jumlah_kuadrat_galat)
