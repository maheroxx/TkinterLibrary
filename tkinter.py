import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()

    if not firstname or not lastname or not email:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if "@" not in email:
         messagebox.showerror("Error", "Invalid email format.")
         return

    messagebox.showinfo("Success", "Registration successful!")
    print(f"First Name: {firstname}, Last Name: {lastname}, Email: {email}")

window = tk.Tk()
window.title("Registration Form")

firstname_label = ttk.Label(window, text="First Name:")
firstname_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
firstname_entry = ttk.Entry(window)
firstname_entry.grid(row=0, column=1, padx=10, pady=10)

lastname_label = ttkues.Label(window, text="Last Name:")
lastname_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
lastname_entry = ttk.Entry(window)
lastname_entry.grid(row=1, column=1, padx=10, pady=10)

email_label = ttk.Label(window, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
email_entry = ttk.Entry(window)
email_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = ttk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

window.mainloop()
