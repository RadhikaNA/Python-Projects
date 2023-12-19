import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Invalid input. Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

# GUI setup
app = tk.Tk()
app.title("BMI Calculator")

weight_label = tk.Label(app, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(app)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(app, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(app)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2)

app.mainloop()
