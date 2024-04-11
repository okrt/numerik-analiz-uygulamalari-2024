import numpy as np
import matplotlib.pyplot as plt

import scipy

# Noktaların x ve y koordinatlarını veriyoruz.
x_values = np.array([1, 2, 3, 4])
y_values = np.array([1, 4, 9, 16])

# Scipy içerisindeki lagrance interpolasyon metodunu çağırıyoruz.
polynomial = scipy.interpolate.lagrange(x_values, y_values)

# x = 2.5 için interpolasyonu yapıyoruz.
x_interpolated = 2.5
y_interpolated = polynomial(x_interpolated)

# Orijinal noktalar için kırmızı olarak grafiği oluşturuyoruz.
plt.scatter(x_values, y_values, color='red', label='Veri Noktaları')

# İnterpolasyon yapılmış noktayı gösteriyoruzç
plt.scatter(x_interpolated, y_interpolated, color='blue', label='Yeni Nokta')

# İnterpolasyon ile oluşturulmuş polinomu çiziyoruz.
x_range = np.linspace(min(x_values), max(x_values), 100)  # Düzgün bir eğri için yeni noktalar oluşturuyoruz.
plt.plot(x_range, polynomial(x_range), color='green', label='İnterpolasyonlu eğri')

# Grafik başlık ve açıklamalarını ekliyoruz.
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Lagrange Interpolasyonu')
plt.legend()

# Grafiği gösteriyoruz.
plt.grid(True)
plt.show()

# İnterpolasyon sonucunu yazdırıyoruz.
print(f" x = {x_interpolated} icin interpolasyon sonucu olusan y = {y_interpolated}")
