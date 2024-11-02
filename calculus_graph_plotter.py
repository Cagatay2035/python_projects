import tkinter as tk
from tkinter import messagebox
from sympy import symbols, sympify, diff, integrate, lambdify
import matplotlib.pyplot as plt
import numpy as np


def grafik(expr, title="Fonksiyonun Grafiği"):
    x = symbols('x')
    expr = sympify(expr)
    f = lambdify(x, expr, 'numpy')

    x_degeri = np.linspace(-10, 10, 400)
    try:
        y_degeri = f(x_degeri)
    except Exception as e:
        messagebox.showerror("Hata", f"Grafik çizilemedi: {e}")
        return

    plt.figure()  
    plt.plot(x_degeri, y_degeri, label=str(expr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title(title)
    plt.show()


def turev_al(deger):
    x = symbols('x')
    deger = sympify(deger)
    derivative = diff(deger, x)
    return derivative


def integral_al(deger):
    x = symbols('x')
    deger = sympify(deger)
    integral = integrate(deger, x)
    return integral


def grafigi_ciz():
    deger = entry.get()
    try:
        grafik(deger)
    except Exception as e:
        messagebox.showerror("Hata", f"Geçersiz ifade: {e}")

def turevin_grafigini_ciz():
    deger = entry.get()
    try:
        derivative = turev_al(deger)
        grafik(derivative, title="Türevin Grafiği")
    except Exception as e:
        messagebox.showerror("Hata", f"Geçersiz ifade: {e}")

def integralin_grafigini_ciz():
    deger = entry.get()
    try:
        integral = integral_al(deger)
        grafik(integral, title="İntegralin Grafiği")
    except Exception as e:
        messagebox.showerror("Hata", f"Geçersiz ifade: {e}")

def turevi_goster():
    deger = entry.get()
    try:
        derivative = turev_al(deger)
        messagebox.showinfo("Türev", f"Türev: {derivative}")
    except Exception as e:
        messagebox.showerror("Hata", f"Geçersiz ifade: {e}")

def integrali_goster():
    deger = entry.get()
    try:
        integral = integral_al(deger)
        messagebox.showinfo("İntegral", f"İntegral: {integral}")
    except Exception as e:
        messagebox.showerror("Hata", f"Geçersiz ifade: {e}")


root = tk.Tk()
root.title("Fonksiyon Çizici")

tk.Label(root, text="Matematiksel İfade:").grid(row=0, column=0)

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1)

tk.Button(root, text="Grafik Çiz", command=grafigi_ciz).grid(row=1, column=0)
tk.Button(root, text="Türevini Al", command=turevi_goster).grid(row=1, column=1)
tk.Button(root, text="İntegralini Al", command=integrali_goster).grid(row=1, column=2)

tk.Button(root, text="Türevin Grafiğini Çiz", command=turevin_grafigini_ciz).grid(row=2, column=0)
tk.Button(root, text="İntegralin Grafiğini Çiz", command=integralin_grafigini_ciz).grid(row=2, column=1)

root.mainloop()
