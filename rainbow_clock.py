# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:28:19 2023

@author: echo
"""

import tkinter as tk
import time
import math
import random

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

def change_colors():
    global counter
    hue = (counter / 10) % 1.0

    # 背景色の設定
    bg_color = hsv_to_rgb(hue, 1.0, 1.0)
    bg_hex = rgb_to_hex(bg_color)
    root.configure(bg=bg_hex)

    # 文字色の設定
    text_hue = (hue + 0.5) % 1.0
    text_color = hsv_to_rgb(text_hue, 1.0, 1.0)
    text_hex = rgb_to_hex(text_color)
    label.config(fg=text_hex,bg=bg_hex)

    counter += 0.1
    label.after(10, change_colors)

def move_text():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    label.place(x=150 + x, y=30 + y)
    label["font"] = ('Arial', random.randint(90,110), 'bold')
    b = int.to_bytes(random.randint(0,10**15),10,"little")
    root.title(b.decode(errors="replace"))
    label.after(100, move_text)

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v

    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - (f * s))
    t = v * (1.0 - ((1.0 - f) * s))

    if i % 6 == 0:
        return v, t, p
    elif i % 6 == 1:
        return q, v, p
    elif i % 6 == 2:
        return p, v, t
    elif i % 6 == 3:
        return p, q, v
    elif i % 6 == 4:
        return t, p, v
    else:
        return v, p, q

def rgb_to_hex(rgb):
    r = int(rgb[0] * 255)
    g = int(rgb[1] * 255)
    b = int(rgb[2] * 255)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

root = tk.Tk()
root.geometry("800x200")

label = tk.Label(root, font=('Arial', 100, 'bold'))
label.pack(expand=True)

counter = 0
change_colors()
update_time()
move_text()

root.mainloop()