
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import List

app = FastAPI()

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="promisenonhlanhla",
    database="student_portal"
)
cursor = conn.cursor(dictionary=True)

# Models
class Student(BaseModel):
    name: str
    email: str

class Course(BaseModel):
    name: str
    code: str

class Enrollment(BaseModel):
    student_id: int
    course_id: int

# STUDENTS CRUD
@app.post("/students/")
def create_student(student: Student):
    try:
        cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (student.name, student.email))
        conn.commit()
        return {"message": "Student created successfully"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=str(err))

@app.get("/students/")
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    cursor.execute("UPDATE students SET name=%s, email=%s WHERE id=%s", (student.name, student.email, student_id))
    conn.commit()
    return {"message": "Student updated"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    return {"message": "Student deleted"}

# COURSES CRUD
@app.post("/courses/")
def create_course(course: Course):
    cursor.execute("INSERT INTO courses (name, code) VALUES (%s, %s)", (course.name, course.code))
    conn.commit()
    return {"message": "Course created"}

@app.get("/courses/")
def get_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

# ENROLLMENTS
@app.post("/enrollments/")
def enroll(enrollment: Enrollment):
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
                   (enrollment.student_id, enrollment.course_id))
    conn.commit()
    return {"message": "Enrollment successful"}

@app.get("/enrollments/")
def get_enrollments():
    cursor.execute("""
        SELECT e.id, s.name AS student, c.name AS course
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
    """)
    return cursor.fetchall()
