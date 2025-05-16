import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Password length must be at least 4")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (4 or more).")
        return

    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if not (use_letters or use_numbers or use_symbols):
        messagebox.showerror("Selection Error", "Select at least one character type.")
        return

    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)


# 🖼️ GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# 🔢 Password Length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# ✅ Options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

# ▶️ Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# 📋 Output Field
tk.Label(root, text="Generated Password:").pack(pady=5)
password_output = tk.Entry(root, font=("Courier", 12), width=30)
password_output.pack()

root.mainloop()
