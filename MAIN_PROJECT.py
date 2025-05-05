import tkinter as tk
from tkinter import ttk, messagebox
import MANAGE

# --- Admin Credentials ---
ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "password"

# --- ROOT Window ---
window = tk.Tk()

window.title("Student Management System")
window.geometry("1890x1080")
window.configure(bg="#e0f7fa")  # Light teal background

# --- Styling ---
button_style = {"bg": "#00796b", "fg": "white", "activebackground": "#004d40", "activeforeground": "white", "padx": 10, "pady": 5}
label_style = {"bg": "#e0f7fa", "font": ("Arial", 11)}
entry_style = {"font": ("Arial", 11)}

# --- Clear frames function ---
def clear_frames():
    for widget in window.winfo_children():
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

    if results:
        for row in student_table.get_children():
            student_table.delete(row)
        for row in results:
            student_table.insert('', 'end', values=row)
    else:
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

# === FRAMES SETUP ===

# --- Login Frame ---

login_frame = tk.Frame(window, bg="#e0f7fa")

tk.Label(login_frame, text="Student Management System", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

tk.Label(login_frame, text="Username:", **label_style).pack(pady=5)
username_entry = tk.Entry(login_frame, **entry_style)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password:", **label_style).pack(pady=5)
password_entry = tk.Entry(login_frame, show="*", **entry_style)
password_entry.pack(pady=5)

tk.Button(login_frame, text="Login", command=login, **button_style).pack(pady=20)
login_frame.pack(fill="both", expand=True)

# --- Dashboard Frame ---
dashboard_frame = tk.Frame(window, bg="#e0f7fa")
dashboard_inner = tk.Frame(dashboard_frame, bg="#e0f7fa")
dashboard_inner.place(relx=0.5, rely=0.5, anchor="center")

tk.Button(dashboard_inner, text="Manage Students", width=25, height=2, command=show_student_frame, **button_style).pack(pady=10)
tk.Button(dashboard_inner, text="Manage Courses", width=25, height=2, command=show_course_frame, **button_style).pack(pady=10)
tk.Button(dashboard_inner, text="Logout", width=25, height=2, command=logout, **button_style).pack(pady=10)

# --- Student Frame ---
student_frame = tk.Frame(window, bg="#e0f7fa")

student_inner = tk.Frame(student_frame, bg="#e0f7fa")
student_inner.place(relx=0.5, rely=0.05, anchor="n")

tk.Label(student_inner, text="Reg No", **label_style).grid(row=0, column=0, sticky="e", padx=5, pady=5)
reg_entry = tk.Entry(student_inner, **entry_style)
reg_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(student_inner, text="Name", **label_style).grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(student_inner, **entry_style)
name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(student_inner, text="Age", **label_style).grid(row=2, column=0, sticky="e", padx=5, pady=5)
age_entry = tk.Entry(student_inner, **entry_style)
age_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(student_inner, text="Gender", **label_style).grid(row=3, column=0, sticky="e", padx=5, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(student_inner, text="Male", variable=gender_var, value="Male", bg="#e0f7fa").grid(row=3, column=1, sticky="w", padx=5)
tk.Radiobutton(student_inner, text="Female", variable=gender_var, value="Female", bg="#e0f7fa").grid(row=3, column=2, sticky="w", padx=5)

tk.Label(student_inner, text="Email", **label_style).grid(row=4, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(student_inner, **entry_style)
email_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(student_inner, text="Phone", **label_style).grid(row=5, column=0, sticky="e", padx=5, pady=5)
phone_entry = tk.Entry(student_inner, **entry_style)
phone_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(student_inner, text="Course", **label_style).grid(row=6, column=0, sticky="e", padx=5, pady=5)
course_entry = tk.Entry(student_inner, **entry_style)
course_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Button(student_inner, text="Add Student", command=add_student, **button_style).grid(row=7, column=0, pady=10)
tk.Button(student_inner, text="Update Student", command=update_student, **button_style).grid(row=7, column=1, pady=10)
tk.Button(student_inner, text="Delete Student", command=delete_student, **button_style).grid(row=7, column=2, pady=10)

tk.Label(student_inner, text="Search", **label_style).grid(row=8, column=0, sticky="e", padx=5, pady=5)
search_entry = tk.Entry(student_inner, **entry_style)
search_entry.grid(row=8, column=1, padx=5, pady=5)
tk.Button(student_inner, text="Search", command=search_student, **button_style).grid(row=8, column=2, padx=5)

# Treeview
columns = ("Reg No", "Name", "Age", "Gender", "Email", "Phone", "Course")
student_table = ttk.Treeview(student_frame, columns=columns, show="headings")
for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=150)

student_table.place(relx=0.5, rely=0.45, anchor="n")
student_scroll = ttk.Scrollbar(student_frame, orient="vertical", command=student_table.yview)
student_table.configure(yscrollcommand=student_scroll.set)
student_scroll.place(relx=0.84, rely=0.45, relheight=0.27, anchor="n")

tk.Button(student_frame, text="Back", command=show_dashboard, bg="lightgrey", padx=10, pady=5).place(relx=0.5, rely=0.77, anchor="s")

# --- Course Frame ---
course_frame = tk.Frame(window, bg="#e0f7fa")

course_inner = tk.Frame(course_frame, bg="#e0f7fa")
course_inner.place(relx=0.5, rely=0.05, anchor="n")

tk.Label(course_inner, text="Course Code", **label_style).grid(row=0, column=0, sticky="e", padx=5, pady=5)
course_code_entry = tk.Entry(course_inner, **entry_style)
course_code_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(course_inner, text="Course Name", **label_style).grid(row=1, column=0, sticky="e", padx=5, pady=5)
course_name_entry = tk.Entry(course_inner, **entry_style)
course_name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(course_inner, text="Student Count", **label_style).grid(row=2, column=0, sticky="e", padx=5, pady=5)
student_count_entry = tk.Entry(course_inner, **entry_style)
student_count_entry.grid(row=2, column=1, padx=5, pady=5)

button_frame = tk.Frame(course_inner, bg="#e0f7fa")
button_frame.grid(row=3, column=0, columnspan=2, pady=(15, 25))

tk.Button(button_frame, text="Add Course", command=add_course, **button_style).pack(side="left", padx=10)
tk.Button(button_frame, text="Delete Course", command=delete_course, **button_style).pack(side="left", padx=10)

# Treeview
course_columns = ("Course Code", "Course Name", "Student Count")
course_table = ttk.Treeview(course_frame, columns=course_columns, show="headings")
for col in course_columns:
    course_table.heading(col, text=col)
    course_table.column(col, width=150)

course_table.place(relx=0.5, rely=0.3, anchor="n")

course_scroll = ttk.Scrollbar(course_frame, orient="vertical", command=course_table.yview)
course_table.configure(yscrollcommand=course_scroll.set)
course_scroll.place(relx=0.65, rely=0.3, relheight=0.27, anchor="n")

tk.Button(course_frame, text="Back", command=show_dashboard, bg="lightgrey", padx=10, pady=5).place(relx=0.5, rely=0.65, anchor="s")

# --- MAINLOOP ---
window.mainloop()