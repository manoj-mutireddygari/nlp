import sqlite3
import csv
import hashlib
from tkinter import messagebox

connection = sqlite3.connect("database/students.db")
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dob TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    gender TEXT NOT NULL
)""")
connection.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)""")
connection.commit()

def login(username ,password):
    hashed_password = hash_password(password)
    cursor.execute("SELECT * FROM teachers WHERE username=? AND password=?",(username,hashed_password))
    teachers = cursor.fetchone()
    if teachers:
        return True
    else:
        return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
def add_student(name,dob ,email,phone,gender):
    if not check_email(email):
        return False

    if not check_phone(phone):
        return False

    cursor.execute("INSERT INTO students(name,dob,email,phone,gender) VALUES(?,?,?,?,?)",(name,dob,email,phone,gender))
    connection.commit()

    return True

def check_email(email):
    cursor.execute("SELECT * FROM students WHERE email=?",(email,))
    existing =cursor.fetchone()
    if existing:
        messagebox.showerror("Error","Email id already exists try another")
        return False
    return True


def check_phone(phone):
    cursor.execute("SELECT * FROM students WHERE phone=?",(phone,))
    existing =cursor.fetchone()
    if existing:
        messagebox.showerror("Error","Phone number already exists")
        return False
    return True

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id =? ",(student_id,))
    connection.commit()
    return True
    
def fetch_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?",(student_id,))
    student = cursor.fetchone()
    return student

def update_student(student_id,name,dob,email,phone,gender):
    cursor.execute("UPDATE students SET name=? ,dob=?, email=?, phone=?,gender=? WHERE id=?",(name,dob,email,phone,gender,student_id))
    connection.commit()
    return True

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return students

def search_student(name):
    cursor.execute("SELECT * FROM students WHERE name LIKE?",("%"+name+"%",))
    student = cursor.fetchall()
    return student


def export_students():
    cursor.execute("SELECT * FROM students")
    students =cursor.fetchall()
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID","Name","DOB","Email","Phone","Gender"])

        for student in students:
            writer.writerow(student)

    messagebox.showinfo("Success", "Students exported to students.csv")
  


    


                  