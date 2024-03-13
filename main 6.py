import tkinter as tk
from tkinter import ttk
from time import *

root = tk.Tk()
root.title("Simple GUI")
root.geometry("400x400")

text_label = tk.Label(root, text="Bla bla")
text_label.pack()

def btn_callback(button_text):
    if button_text == "btn1":
        print("BTN 1")
        indicator_1.config(bg="blue")
    else:
        print("BTN 2")
        indicator_1.config(bg="red")

def update_indicator():
    root.after(1000, update_indicator)

def update_text():
    text_label.config(text="New text")
    root.after(1000, update_text)

indicator_size = 5
indicator_1 = tk.Label(root, text="", bg="red", width=indicator_size, height=indicator_size)
indicator_2 = tk.Label(root, text="", bg="green", width=indicator_size, height=indicator_size)

indicator_1.config(relief=tk.RAISED, bd=4)
indicator_2.config(relief=tk.RAISED, bd=4)

indicator_1.pack()
indicator_2.pack()

button_1 = tk.Button(root, text="Čudl 1", command=lambda: btn_callback("btn1"))
button_1.config(font=("Arial", 14, "bold"), background="lightblue")
button_2 = tk.Button(root, text="Čudl 2", command=lambda: btn_callback("bnt2"))
button_2.config(font=("Arial", 16, "italic"), background="lightgreen",
                       foreground="darkblue", activebackground="lightblue", padx=15, pady=5, relief=tk.RAISED)
button_1.pack()
button_2.pack()

update_indicator()
update_text()
root.mainloop()
