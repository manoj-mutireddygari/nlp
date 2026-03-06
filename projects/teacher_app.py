import sqlite3

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
)
""")
connection.commit()

def add_student():
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    email = input("Enter student email: ")
    phone = input("Enter student phone: ")
    gender = input("Enter student gender: ")
    cursor.execute("INSERT INTO students(name,dob,email,phone,gender) VALUES(?,?,?,?,?)",(name,dob,email,phone,gender))
    connection.commit()
    print("Student added successfully!")

def delete_student():
    student_id = int(input("Enter the student id to delete: "))
    cursor.execute("DELETE FROM students WHERE id =? ",(student_id,))
    connection.commit()
    print("Student deleted successfully!")

def update_student():
    student_id = int(input("Enter the student id"))
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
    cursor.execute("SELECT * FROM students WHERE name=?",(name,))
    student = cursor.fetchone()
    if student:
        print("student found",student)
    else:
        print("student not found")
                   
while True:
    print("-------------")
    print("1.Add student")
    print("2.Delete student")
    print("3.update student")
    print("4.View students")
    print("5.search student")
    print("6.Exit")
    
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
        break

    


                  