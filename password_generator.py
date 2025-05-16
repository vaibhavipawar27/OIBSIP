import random
import string
import tkinter as tk
from tkinter import messagebox

def password_generator():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Password length must be at least 4")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (4 or more).")
        return

    letter = letters_var.get()
    numbers = numbers_var.get()
    symbols = symbols_var.get()

    if not(letter or numbers or symbols):
        messagebox.showerror("Selection Error", "Select at least one character type.")
        return
    
    characters=''
    if letter:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
        
    password= ''.join(random.choice(characters) for _ in range(length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)
   
root=tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg='#e6f2ff')

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=password_generator).pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)
password_output = tk.Entry(root, font=("Courier", 12), width=30)
password_output.pack()

root.mainloop()
