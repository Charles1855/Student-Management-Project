import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('hostel_management.db')
cur = conn.cursor()

# Create Students table
cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    reg_no TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    course TEXT NOT NULL
)
''')

# Create Courses table
cur.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_code TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    student_count INTEGER NOT NULL
)
''')

conn.commit()

def coon():
    pass  # Not needed now, but your main code is calling it, so we keep it

# ----------- STUDENT FUNCTIONS -----------
def add_student(reg_no, name, age, gender, email, phone, course):
    cur.execute('''
    INSERT INTO students (reg_no, name, age, gender, email, phone, course)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (reg_no, name, age, gender, email, phone, course))
    conn.commit()

def update_student(reg_no, name, age, gender, email, phone, course):
    cur.execute('''
    UPDATE students
    SET name=?, age=?, gender=?, email=?, phone=?, course=?
    WHERE reg_no=?
    ''', (name, age, gender, email, phone, course, reg_no))
    conn.commit()

def delete_student(reg_no):
    cur.execute('DELETE FROM students WHERE reg_no=?', (reg_no,))
    conn.commit()

def get_students():
    cur.execute('SELECT * FROM students')
    return cur.fetchall()

# ----------- COURSE FUNCTIONS -----------
def add_course(course_code, course_name, student_count):
    cur.execute('''
    INSERT INTO courses (course_code, course_name, student_count)
    VALUES (?, ?, ?)
    ''', (course_code, course_name, student_count))
    conn.commit()

def update_course(course_code, course_name, student_count):
    cur.execute('''
    UPDATE courses
    SET course_name=?, student_count=?
    WHERE course_code=?
    ''', (course_name, student_count, course_code))
    conn.commit()

def delete_course(course_code):
    cur.execute('DELETE FROM courses WHERE course_code=?', (course_code,))
    conn.commit()

def get_courses():
    cur.execute('SELECT * FROM courses')
    return cur.fetchall()