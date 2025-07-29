# gui_calculator.py
import tkinter as tk
from tkinter import messagebox

history = []

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        result = str(eval(expr))
        history.append(f"{expr} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Expression")

def show_history():
    hist_win = tk.Toplevel(root)
    hist_win.title("History")
    hist_text = tk.Text(hist_win, height=10, width=30)
    hist_text.pack()
    for item in history:
        hist_text.insert(tk.END, item + "\n")

def clear_history():
    history.clear()
    messagebox.showinfo("History", "History cleared!")

root = tk.Tk()
root.title("Simple Calculator 🧮")

entry = tk.Entry(root, width=25, font=('Arial', 16), borderwidth=3, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for btn in buttons:
    action = (lambda x=btn: calculate() if x == '=' else click(x))
    tk.Button(root, text=btn, width=5, height=2, font=('Arial', 14), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=5, height=2, font=('Arial', 14), command=clear_entry).grid(row=5, column=0)
tk.Button(root, text='History', width=11, height=2, font=('Arial', 14), command=show_history).grid(row=5, column=1, columnspan=2)
tk.Button(root, text='Clear History', width=11, height=2, font=('Arial', 14), command=clear_history).grid(row=5, column=3)

root.mainloop()
