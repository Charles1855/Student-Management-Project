import tkinter as tk
from tkinter import ttk, messagebox
import MANAGE

# --- Admin Credentials ---
ADMIN_USERNAME = "ADMIN"
ADMIN_PASSWORD = "#270707"

# --- ROOT Window ---
root = tk.Tk()
root.title("Student Management System")
root.geometry("750x600")
root.configure(bg="#f0f4f7")

# --- Clear frames function ---
def clear_frames():
    for widget in root.winfo_children():
        widget.pack_forget()

# --- LOGIN FUNCTIONS ---
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome Admin!")
        show_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# --- LOGOUT FUNCTION ---
def logout():
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        clear_frames()
        login_frame.pack(fill="both", expand=True)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# --- DASHBOARD ---
def show_dashboard():
    clear_frames()
    dashboard_frame.pack(fill="both", expand=True)

# --- STUDENT MANAGEMENT ---
def show_student_frame():
    clear_frames()
    student_frame.pack(fill="both", expand=True)
    refresh_students()

def add_student():
    reg_no = reg_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not (reg_no and name and age.isdigit() and gender and email and phone and course):
        messagebox.showerror("Error", "Please fill in all fields correctly.")
        return

    available_courses = [c[0] for c in MANAGE.get_courses()]
    if course not in available_courses:
        messagebox.showerror("Course Unavailable", f"The course '{course}' does not exist.")
        return

    try:
        MANAGE.add_student(reg_no, name, int(age), gender, email, phone, course)
        refresh_students()
        messagebox.showinfo("Success", "Student added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not add student. {e}")

def update_student():
    selected = student_table.focus()
    if not selected:
        messagebox.showerror("Error", "Select a student to update.")
        return

    data = student_table.item(selected, 'values')
    reg_no = data[0]

    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not (name and age.isdigit() and gender and email and phone and course):
        messagebox.showerror("Error", "Fill all fields correctly.")
        return

    try:
        MANAGE.update_student(reg_no, name, int(age), gender, email, phone, course)
        refresh_students()
        messagebox.showinfo("Success", "Student updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not update student. {e}")

def delete_student():
    selected = student_table.focus()
    if not selected:
        messagebox.showerror("Error", "Select a student to delete.")
        return

    data = student_table.item(selected, 'values')
    reg_no = data[0]

    confirm = messagebox.askyesno("Confirm", f"Delete student {reg_no}?")
    if confirm:
        MANAGE.delete_student(reg_no)
        refresh_students()
        messagebox.showinfo("Deleted", "Student deleted.")

def search_student():
    search_term = search_entry.get()
    if not search_term:
        messagebox.showerror("Error", "Enter a search term.")
        return

    results = []
    for row in MANAGE.get_students():
        if search_term.lower() in [str(field).lower() for field in row]:
            results.append(row)

    for row in student_table.get_children():
        student_table.delete(row)
    for row in results:
        student_table.insert('', 'end', values=row)

    if not results:
        messagebox.showinfo("Not Found", "No matching students found.")

def refresh_students():
    for row in student_table.get_children():
        student_table.delete(row)
    for row in MANAGE.get_students():
        student_table.insert('', 'end', values=row)

# --- COURSE MANAGEMENT ---
def show_course_frame():
    clear_frames()
    course_frame.pack(fill="both", expand=True)
    refresh_courses()

def add_course():
    code = course_code_entry.get()
    name = course_name_entry.get()
    count = student_count_entry.get()

    if not (code and name and count.isdigit()):
        messagebox.showerror("Error", "Fill all fields correctly.")
        return

    try:
        MANAGE.add_course(code, name, int(count))
        refresh_courses()
        messagebox.showinfo("Success", "Course added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not add course. {e}")

def delete_course():
    selected = course_table.focus()
    if not selected:
        messagebox.showerror("Error", "Select a course to delete.")
        return

    data = course_table.item(selected, 'values')
    course_code = data[0]

    confirm = messagebox.askyesno("Confirm", f"Delete course {course_code}?")
    if confirm:
        MANAGE.delete_course(course_code)
        refresh_courses()
        messagebox.showinfo("Deleted", "Course deleted.")

def refresh_courses():
    for row in course_table.get_children():
        course_table.delete(row)
    for row in MANAGE.get_courses():
        course_table.insert('', 'end', values=row)

# ====================
# === FRAMES SETUP ===
# ====================

button_style = {"bg": "#4a90e2", "fg": "white", "activebackground": "#357ABD"}

# --- Login Frame ---
login_frame = tk.Frame(root, bg="#f0f4f7")
tk.Label(login_frame, text="Username:", bg="#f0f4f7").pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password:", bg="#f0f4f7").pack(pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

tk.Button(login_frame, text="Login", command=login, **button_style).pack(pady=20)
login_frame.pack(fill="both", expand=True)

# --- Dashboard Frame ---
dashboard_frame = tk.Frame(root, bg="#f0f4f7")

tk.Button(dashboard_frame, text="Manage Students", width=25, height=2, command=show_student_frame, **button_style).pack(pady=10)
tk.Button(dashboard_frame, text="Manage Courses", width=25, height=2, command=show_course_frame, **button_style).pack(pady=10)
tk.Button(dashboard_frame, text="Logout", width=25, height=2, command=logout, **button_style).pack(pady=10)

# --- Student Frame ---
student_frame = tk.Frame(root, bg="#f0f4f7")

labels = ["Reg No", "Name", "Age", "Gender", "Email", "Phone", "Course"]
entries = []

for i, label in enumerate(labels):
    tk.Label(student_frame, text=label, bg="#f0f4f7").grid(row=i, column=0)
    if label == "Gender":
        gender_var = tk.StringVar()
        tk.Radiobutton(student_frame, text="Male", variable=gender_var, value="Male", bg="#f0f4f7").grid(row=i, column=1, sticky="w")
        tk.Radiobutton(student_frame, text="Female", variable=gender_var, value="Female", bg="#f0f4f7").grid(row=i, column=2, sticky="w")
    else:
        entry = tk.Entry(student_frame)
        entry.grid(row=i, column=1)
        entries.append(entry)

reg_entry, name_entry, age_entry, email_entry, phone_entry, course_entry = entries

tk.Button(student_frame, text="Add Student", command=add_student, **button_style).grid(row=7, column=0, pady=5)
tk.Button(student_frame, text="Update Student", command=update_student, **button_style).grid(row=7, column=1, pady=5)
tk.Button(student_frame, text="Delete Student", command=delete_student, **button_style).grid(row=7, column=2, pady=5)

tk.Label(student_frame, text="Search", bg="#f0f4f7").grid(row=8, column=0)
search_entry = tk.Entry(student_frame)
search_entry.grid(row=8, column=1)
tk.Button(student_frame, text="Search", command=search_student, **button_style).grid(row=8, column=2)

columns = ("Reg No", "Name", "Age", "Gender", "Email", "Phone", "Course")
student_table = ttk.Treeview(student_frame, columns=columns, show="headings")
for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)

student_table.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

student_scroll = ttk.Scrollbar(student_frame, orient="vertical", command=student_table.yview)
student_table.configure(yscrollcommand=student_scroll.set)
student_scroll.grid(row=9, column=3, sticky='ns')

tk.Button(student_frame, text="Back", command=show_dashboard, bg="lightgrey").grid(row=10, column=1, pady=20)

# --- Course Frame ---
course_frame = tk.Frame(root, bg="#f0f4f7")

tk.Label(course_frame, text="Course Code", bg="#f0f4f7").grid(row=0, column=0)
course_code_entry = tk.Entry(course_frame)
course_code_entry.grid(row=0, column=1)

tk.Label(course_frame, text="Course Name", bg="#f0f4f7").grid(row=1, column=0)
course_name_entry = tk.Entry(course_frame)
course_name_entry.grid(row=1, column=1)

tk.Label(course_frame, text="Student Count", bg="#f0f4f7").grid(row=2, column=0)
student_count_entry = tk.Entry(course_frame)
student_count_entry.grid(row=2, column=1)

tk.Button(course_frame, text="Add Course", command=add_course, **button_style).grid(row=3, column=0, pady=5)
tk.Button(course_frame, text="Delete Course", command=delete_course, **button_style).grid(row=3, column=1, pady=5)

course_columns = ("Course Code", "Course Name", "Student Count")
course_table = ttk.Treeview(course_frame, columns=course_columns, show="headings")
for col in course_columns:
    course_table.heading(col, text=col)
    course_table.column(col, width=150)

course_table.grid(row=4, column=0, columnspan=2, pady=10)

course_scroll = ttk.Scrollbar(course_frame, orient="vertical", command=course_table.yview)
course_table.configure(yscrollcommand=course_scroll.set)
course_scroll.grid(row=4, column=2, sticky='ns')

tk.Button(course_frame, text="Back", command=show_dashboard, bg="lightgrey").grid(row=5, column=0, columnspan=2, pady=20)

# --- MAINLOOP ---
root.mainloop()