import sqlite3
import csv
import hashlib

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

def main():
    print("===== Teacher Login =====")

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username,password):
            print("Login Successful")
            break
        else:
            print("username or password is incorrect")
    
    while True:
        print("-------------")
        print("1.Add student")
        print("2.Delete student")
        print("3.update student")
        print("4.View students")
        print("5.search student")
        print("6.count students")
        print("7.Export students")
        print("8.Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            view_students()
        elif choice == 5:
            search_student()
        elif choice == 6:
            count_students()
        elif choice == 7:
            export_students()
        elif choice == 8:
            break

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
    
def add_student():
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    email = input("Enter student email: ")
    validate_email =check_email(email)
    print(f"Accepted email: {validate_email}")
    phone = input("Enter student phone: ")
    validate_phone = check_phone(phone)
    print(f"Accepted phone: {validate_phone}")
    gender = input("Enter student gender: ")
    cursor.execute("INSERT INTO students(name,dob,email,phone,gender) VALUES(?,?,?,?,?)",(name,dob,validate_email,validate_phone,gender))
    connection.commit()
    print("Student added successfully!")

def check_email(email):
    cursor.execute("SELECT * FROM students WHERE email=?",(email,))
    existing =cursor.fetchone()
    if existing:
        print("Email id already exists try another")
        new_email = input("Enter student email: ")
        return check_email(new_email)
    return email

def check_phone(phone):
    cursor.execute("SELECT * FROM students WHERE phone=?",(phone,))
    existing =cursor.fetchone()
    if existing:
        print("Phone number already exists")
        new_phone = input("Enter student phone: ")
        return check_phone(new_phone)
    return phone

def delete_student():
    student_id = int(input("Enter the student id to delete: "))
    confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
    if confirm == "y":
        cursor.execute("DELETE FROM students WHERE id =? ",(student_id,))
        connection.commit()
        print("Student deleted successfully!")
    else:
        print("Student not deleted")

def update_student():
    student_id = int(input("Enter the student id: "))
    cursor.execute("SELECT * FROM students WHERE id=?",(student_id,))
    student = cursor.fetchone()
    if not student:
        print("Student not found")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    email = input("Enter student email: ")
    phone = input("Enter student phone: ")
    gender = input("Enter student gender: ")
    cursor.execute("UPDATE students SET name=? ,dob=?, email=?, phone=?,gender=? WHERE id=?",(name,dob,email,phone,gender,student_id))
    connection.commit()
    print("Student details updated successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

def search_student():
    name = input("Enter the name of the student: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE?",("%"+name+"%",))
    student = cursor.fetchone()
    if student:
        print("student found",student)
    else:
        print("student not found")

def count_students():
    cursor.execute("SELECT COUNT(*) FROM students")
    result = cursor.fetchone()
    print("Total students:", result[0])

def export_students():
    cursor.execute("SELECT * FROM students")
    students =cursor.fetchall()
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID","Name","DOB","Email","Phone","Gender"])

        for student in students:
            writer.writerow(student)

    print("Students exported successfully to students.csv")

if __name__ == "__main__":
    main()         


    


                  