import tkinter as tk
import math
import matplotlib.pyplot as plt

win = tk.Tk()
win.geometry('710x543+1100+10')
win.title('ХН')


def plot_XH():
    global val_1, val_2, val_3
    f = float(val_1.get())
    n = int(val_2.get())
    x = float(val_3.get())
    print(f, n, x)
    XH = []
    Ang = []
    temp_val = n * math.pi * x * 1500 / f
    for phi in range(-90, 90, 1):
        Ang.append(phi)
        y = temp_val * math.cos(phi / 180.0 * math.pi)
        XH.append(math.sin(y) / y)
    plt.plot(Ang, XH)
    plt.show()


tk.Label(win, text="Частота, ГЦ     :").grid(row=0, column=0)
tk.Label(win, text="Кол-во эл-тов   :").grid(row=1, column=0)
tk.Label(win, text="Размер эл-тов   :").grid(row=2, column=0)

val_1 = tk.Entry(win)
val_1.insert(0, '20000')
val_1.grid(row=0, column=1)
val_2 = tk.Entry(win)
val_2.insert(0, '15')
val_2.grid(row=1, column=1)
val_3 = tk.Entry(win)
val_3.insert(0, '0.03')
val_3.grid(row=2, column=1)

tk.Button(win, text="Расчитать", command=plot_XH).grid(column=0, row=3, columnspan=2)

win.mainloop()
