import tkinter as tk
from tkinter import messagebox
from datetime import date
def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        birth_date = date(year, month, day)
        today = date.today()
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future.")
            return
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        label_result.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for day, month, and year.")
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
tk.Label(root, text="Enter your date of birth", font=("Helvetica", 14)).pack(pady=10)
tk.Label(root, text="Day:").pack()
entry_day = tk.Entry(root)
entry_day.pack()
tk.Label(root, text="Month:").pack()
entry_month = tk.Entry(root)
entry_month.pack()
tk.Label(root, text="Year:").pack()
entry_year = tk.Entry(root)
entry_year.pack()
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=15)
label_result = tk.Label(root, text="", font=("Helvetica", 12))
label_result.pack()
root.mainloop()