import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def collect_user_data(file_path):
    user_data = {
        "full_name": full_name_var.get(),
        "email": email_var.get(),
        "phone": phone_var.get(),
        "address": address_var.get(),
        "documents": {
            "photo": photo_var.get(),
            "tenth_result": tenth_result_var.get(),
            "twelfth_result": twelfth_result_var.get(),
            "income_certificate": income_certificate_var.get()
        }
    }
    with open(file_path, 'w') as file:
        json.dump(user_data, file, indent=4)
    messagebox.showinfo("Success", "User data saved successfully.")

def load_user_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def browse_file(var):
    file_path = filedialog.askopenfilename()
    var.set(file_path)

def load_data():
    user_data = load_user_data('user_data.json')
    if user_data:
        full_name_var.set(user_data['full_name'])
        email_var.set(user_data['email'])
        phone_var.set(user_data['phone'])
        address_var.set(user_data['address'])
        photo_var.set(user_data['documents']['photo'])
        tenth_result_var.set(user_data['documents']['tenth_result'])
        twelfth_result_var.set(user_data['documents']['twelfth_result'])
        income_certificate_var.set(user_data['documents']['income_certificate'])
    else:
        messagebox.showwarning("No Data", "No saved user data found.")

def delete_data():
    if messagebox.askyesno("Delete", "Are you sure you want to delete all user data?"):
        try:
            os.remove('user_data.json')
            clear_form()
            messagebox.showinfo("Success", "User data deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Error", "No user data found to delete.")

def clear_form():
    full_name_var.set("")
    email_var.set("")
    phone_var.set("")
    address_var.set("")
    photo_var.set("")
    tenth_result_var.set("")
    twelfth_result_var.set("")
    income_certificate_var.set("")
    form_url_var.set("")

def fill_form():
    url = form_url_var.get()
    if not url:
        messagebox.showwarning("Error", "Please enter a form URL.")
        return

    user_data = load_user_data('user_data.json')
    if not user_data:
        messagebox.showwarning("Error", "No user data found! Please save details first.")
        return

    try:
        driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
        driver.get(url)

        # Fill in the form using Selenium
        driver.find_element(By.NAME, "full_name").send_keys(user_data["full_name"])
        driver.find_element(By.NAME, "email").send_keys(user_data["email"])
        driver.find_element(By.NAME, "phone").send_keys(user_data["phone"])
        driver.find_element(By.NAME, "address").send_keys(user_data["address"])

        # Upload files
        driver.find_element(By.NAME, "photo").send_keys(user_data["documents"]["photo"])
        driver.find_element(By.NAME, "tenth_result").send_keys(user_data["documents"]["tenth_result"])
        driver.find_element(By.NAME, "twelfth_result").send_keys(user_data["documents"]["twelfth_result"])
        driver.find_element(By.NAME, "income_certificate").send_keys(user_data["documents"]["income_certificate"])

        messagebox.showinfo("Success", "Form filled successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fill form: {e}")

def create_ui():
    global root, full_name_var, email_var, phone_var, address_var, photo_var, tenth_result_var, twelfth_result_var, income_certificate_var, form_url_var
    
    root = tk.Tk()
    root.title("User Details Form")
    root.geometry("800x600")
    
    # Load background image
    bg_img = Image.open("C:/Users/hasec/OneDrive/Documents/Coding/python/auto_form_fill/static/image/pexels-jplenio-1103970.jpg")  
    bg_img = bg_img.resize((800, 600), Image.LANCZOS)

    bg_photo = ImageTk.PhotoImage(bg_img)
    
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    
    full_name_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()
    address_var = tk.StringVar()
    photo_var = tk.StringVar()
    tenth_result_var = tk.StringVar()
    twelfth_result_var = tk.StringVar()
    income_certificate_var = tk.StringVar()
    form_url_var = tk.StringVar()
    
    frame = tk.Frame(root, bg='white', padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    tk.Label(frame, text="User Details Form", font=("Arial", 18, "bold"), bg='white').grid(row=0, column=0, columnspan=2, pady=10)
    
    fields = [
        ("Full Name", full_name_var),
        ("Email", email_var),
        ("Phone Number", phone_var),
        ("Address", address_var)
    ]
    
    for i, (label, var) in enumerate(fields, start=1):
        tk.Label(frame, text=label + ":", font=("Arial", 12), bg='white').grid(row=i, column=0, sticky="w", pady=5)
        tk.Entry(frame, textvariable=var, font=("Arial", 12), width=30).grid(row=i, column=1, pady=5)
    
    doc_fields = [
        ("Photo", photo_var),
        ("10th Result", tenth_result_var),
        ("12th Result", twelfth_result_var),
        ("Income Certificate", income_certificate_var)
    ]
    
    for i, (label, var) in enumerate(doc_fields, start=len(fields)+1):
        tk.Label(frame, text=label + " (Upload):", font=("Arial", 12), bg='white').grid(row=i, column=0, sticky="w", pady=5)
        tk.Entry(frame, textvariable=var, font=("Arial", 12), width=20).grid(row=i, column=1, pady=5)
        ttk.Button(frame, text="Browse", command=lambda v=var: browse_file(v)).grid(row=i, column=2, pady=5)

    # URL Entry
    tk.Label(frame, text="Form URL:", font=("Arial", 12), bg='white').grid(row=len(fields)+len(doc_fields)+1, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=form_url_var, font=("Arial", 12), width=30).grid(row=len(fields)+len(doc_fields)+1, column=1, pady=5)

    button_frame = tk.Frame(frame, bg='white')
    button_frame.grid(row=len(fields) + len(doc_fields) + 2, column=0, columnspan=3, pady=10)
    
    ttk.Button(button_frame, text="Save Details", command=lambda: collect_user_data('user_data.json')).grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Load Data", command=load_data).grid(row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Clear Form", command=clear_form).grid(row=0, column=2, padx=5)
    ttk.Button(button_frame, text="Delete Data", command=delete_data).grid(row=0, column=3, padx=5)
    ttk.Button(button_frame, text="Fill Form", command=fill_form).grid(row=0, column=4, padx=5)  # NEW BUTTON

    root.mainloop()

create_ui()
