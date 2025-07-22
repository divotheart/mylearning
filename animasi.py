import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0.5, 8, 100) #angka 0.5(star) itu tata letak dari garis nya, 8(stop) untuk kecepatan dan 100(num itu titik akhir dari garisnya) untuk tinggi rendahnya
y1 = np.sin(x)
y2 = np.cos(x)

line1, = ax.plot([], [], color='yellow', label='Sinus')
line2, = ax.plot([], [], color='green', label='Cosinus')

# Set batas area plot
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Tambahkan legenda dengan gaya
legend = ax.legend(
    loc='upper right',
    fontsize='medium',
    frameon=True,
    shadow=True,
    facecolor='white',
    edgecolor='black'
)

# Fungsi update frame
def update(frame):
    line1.set_data(x[:frame], y1[:frame])
    line2.set_data(x[:frame], y2[:frame])
    return line1, line2

# Buat animasi
ani = animation.FuncAnimation(fig, update, frames=len(x), interval=50, blit=True)

plt.title('Animasi Sinus & Cosinus')
plt.grid(True)
plt.show()