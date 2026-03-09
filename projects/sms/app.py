import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from projects.sms.functions import *

root = tk.Tk()
root.title("Student Management System")
root.geometry("500x400")

#function calling
def check_login():
    username =username_entry.get()
    password =password_entry.get()

    if login(username ,password):
        messagebox.showinfo("success","login successful")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error","Invalid login")


#gui
def open_dashboard():
    dashboard=tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("500x400")

    tk.Label(dashboard,text="Welcome to Student Management System").pack(pady=20)

    tk.Button(dashboard,text="Add Student",command=open_add_student).pack()
    tk.Button(dashboard,text="Delete Student",command=open_delete_student).pack()
    tk.Button(dashboard,text="Update Student",command=open_update_student).pack()
    tk.Button(dashboard,text="View Student",command=open_view_student).pack()
    tk.Button(dashboard,text="Search Student",command=open_search_student).pack()


def open_add_student():
    window = tk.Toplevel()
    window.title("Add student")
    window.geometry("400x400")

    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="DOB").pack()
    dob_entry = tk.Entry(window)
    dob_entry.pack()

    tk.Label(window, text="Email").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    tk.Label(window, text="Phone").pack()
    phone_entry = tk.Entry(window)
    phone_entry.pack()

    tk.Label(window, text="Gender").pack()
    gender_entry = tk.Entry(window)
    gender_entry.pack()

    def submit_student():
        name = name_entry.get()
        dob = dob_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        gender = gender_entry.get()

        result = add_student(name, dob, email, phone, gender)

        if result:
            messagebox.showinfo("Success", "Student added successfully")
            window.destroy()

    tk.Button(window, text="Add Student", command=submit_student).pack(pady=10)

def open_delete_student():
    window = tk.Toplevel()
    window.title("Delete student")
    window.geometry("400x400")

    tk.Label(window, text="student id").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()
        
    def submit_delete():
        student_id = id_entry.get()
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to proceed?")
        if confirmation:
            result= delete_student(student_id)
        if result:
            messagebox.showinfo("Success", "Student deleted successfully")
            window.destroy()
    tk.Button(window,text="Delete student",command=submit_delete).pack(pady=10)

def open_update_student():
    window = tk.Toplevel()
    window.title("Update student")
    window.geometry("400x400")

    tk.Label(window, text="student id").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()
    
    def submit_fetch():
        student_id = id_entry.get()
        result = fetch_student(student_id)
        if result:
            messagebox.showinfo("Success","Students fetched successfully")
            name_entry.delete(0, tk.END)
            name_entry.insert(0, result[1])

            dob_entry.delete(0, tk.END)
            dob_entry.insert(0, result[2])

            email_entry.delete(0, tk.END)
            email_entry.insert(0, result[3])

            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, result[4])

            gender_entry.delete(0, tk.END)
            gender_entry.insert(0, result[5])
        else:
            messagebox.showerror("Error","Student with the id not found ")
    
    tk.Button(window,text="fetch student",command=submit_fetch).pack(pady=10)

    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="DOB").pack()
    dob_entry = tk.Entry(window)
    dob_entry.pack()

    tk.Label(window, text="Email").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    tk.Label(window, text="Phone").pack()
    phone_entry = tk.Entry(window)
    phone_entry.pack()

    tk.Label(window, text="Gender").pack()
    gender_entry = tk.Entry(window)
    gender_entry.pack()

    def submit_update():
        student_id =id_entry.get()
        name = name_entry.get()
        dob = dob_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        gender = gender_entry.get()

        result = update_student(student_id,name, dob, email, phone, gender)

        if result:
            messagebox.showinfo("Success", "Student Updated successfully")
            window.destroy()

    tk.Button(window, text="updated Student", command=submit_update).pack(pady=10)

def open_view_student():
    window = tk.Toplevel()
    window.title("View Students")
    window.geometry("750x400")

    tk.Button(window, text="Export to CSV", command=export_students).pack(pady=10,padx=10)

    columns = ("ID", "Name", "DOB", "Email", "Phone", "Gender")

    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)

    tree.column("ID", width=50, anchor="center")
    tree.column("Name", width=150)
    tree.column("DOB", width=100)
    tree.column("Email", width=200)
    tree.column("Phone", width=120)
    tree.column("Gender", width=80)

    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)

    students = view_students()

    for student in students:
        tree.insert("", tk.END, values=student)


def open_search_student():
    window = tk.Toplevel()
    window.title("Search student")
    window.geometry("750x400")

    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    columns = ("ID", "Name", "DOB", "Email", "Phone", "Gender")

    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)

    tree.column("ID", width=50, anchor="center")
    tree.column("Name", width=150)
    tree.column("DOB", width=100)
    tree.column("Email", width=200)
    tree.column("Phone", width=120)
    tree.column("Gender", width=80)

    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)

    def submit_name():
        name = name_entry.get()

        students = search_student(name)

        # clear old rows
        tree.delete(*tree.get_children())

        if students:
            for student in students:
                tree.insert("", tk.END, values=student)
        else:
            messagebox.showinfo("Info", "No students found")

    tk.Button(window, text="Search Student", command=submit_name).pack(pady=10)



#login screen
tk.Label(root,text="username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root,text="password").pack()
password_entry = tk.Entry(root)
password_entry.pack()

tk.Button(root,text="login",command=check_login).pack()

root.mainloop()

