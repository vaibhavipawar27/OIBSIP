from tkinter import *
from tkinter import ttk

def calculate_bmi():
    try:
        weight = float(e1.get())
        height = float(e2.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        result_category.config(text=get_bmi_category(bmi))
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")
    except ZeroDivisionError:
        result_label.config(text="Height cannot be zero.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Category: Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Category: Normal weight"
    elif 25 <= bmi < 29.9:
        return "Category: Overweight"
    elif 30 <= bmi < 34.9:
        return "Category: Obesity (Class I)"
    elif 35 <= bmi < 39.9:
        return "Category: Obesity (Class II)"
    else:
        return "Category: Obesity (Class III)"

master = Tk()
master.title("BMI Calculator")
master.configure(bg='#e6f2ff')  # light blue background

frame = Frame(master, padx=20, pady=20, bg='white', relief=RIDGE, borderwidth=2)
frame.pack(padx=10, pady=10)

Label(frame, text='Weight (kg):', font=('Arial', 12), bg='white').grid(row=0, column=0, pady=5, sticky='e')
Label(frame, text='Height (m):', font=('Arial', 12), bg='white').grid(row=1, column=0, pady=5, sticky='e')

e1 = ttk.Entry(frame, width=20)
e2 = ttk.Entry(frame, width=20)
e1.grid(row=0, column=1, pady=5)
e2.grid(row=1, column=1, pady=5)

calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, pady=10)

result_label = Label(frame, text="", font=('Arial', 12, 'bold'), fg='green', bg='white')
result_label.grid(row=3, columnspan=2, pady=5)

result_category = Label(frame, text="", font=('Arial', 11), bg='white')
result_category.grid(row=4, columnspan=2, pady=5)

mainloop()
