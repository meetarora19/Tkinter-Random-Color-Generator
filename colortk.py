import tkinter as tk
import random

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = f"#{r:02x}{g:02x}{b:02x}"
    color_label.config(bg=color_code)
    color_code_label.config(text=f"Color Code: {color_code}")

root = tk.Tk()
root.title("Random Color Generator")

color_label = tk.Label(root, width=30, height=10)
color_label.pack()

generate_button = tk.Button(root, text="Generate Color", font=("Arial", 14), command=generate_random_color)
generate_button.pack()

color_code_label = tk.Label(root, text="Color Code:", font=("Arial", 12))
color_code_label.pack()

root.mainloop()
