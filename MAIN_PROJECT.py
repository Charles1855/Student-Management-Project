import tkinter as tk
from tkinter import ttk, messagebox
import MANAGE

MANAGE.coon()

window = tk.Tk()
window.title("Student Management System")
window.geometry("1200x650")


# Variables
gender_var = tk.StringVar()

# --- FUNCTIONS ---
def add_student():
    reg_no = student_id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not (reg_no and name and age and gender and email and phone and course):
        messagebox.showerror("Error", "Please fill all fields.")
        return
    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return

    for child in display_students.get_children():
        student_details = display_students.item(child)['values']
        if reg_no == student_details[0] or (email == student_details[4] and phone == student_details[5]):
            messagebox.showerror("Error", "Duplicate Reg No, Email or Phone!")
            return

    MANAGE.add_student(reg_no, name, int(age), gender, email, phone, course)
    display_students.insert("", "end", values=(reg_no, name, int(age), gender, email, phone, course))
    messagebox.showinfo("Success", "Student added successfully.")
    clear_student_form()

def update_student():
    selected = display_students.focus()
    if not selected:
        messagebox.showerror("Error", "Select a student to update.")
        return
    values = display_students.item(selected, 'values')
    reg_no = values[0]

    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not (name and age and gender and email and phone and course):
        messagebox.showerror("Error", "Please fill all fields.")
        return
    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return

    MANAGE.update_student(reg_no, name, int(age), gender, email, phone, course)
    display_students.item(selected, values=(reg_no, name, int(age), gender, email, phone, course))
    messagebox.showinfo("Success", "Student updated.")
    clear_student_form()

def delete_student():
    selected = display_students.focus()
    if not selected:
        messagebox.showerror("Error", "Select a student to delete.")
        return
    values = display_students.item(selected, 'values')
    reg_no = values[0]

    if messagebox.askyesno("Confirm", "Are you sure you want to delete?"):
        MANAGE.delete_student(reg_no)
        display_students.delete(selected)
        clear_student_form()
        messagebox.showinfo("Deleted", "Student deleted.")

def add_course():
    course_code = course_code_entry.get()
    course_name = course_name_entry.get()
    student_count = student_count_entry.get()

    if not (course_code and course_name and student_count):
        messagebox.showerror("Error", "Please fill all fields.")
        return
    if not student_count.isdigit():
        messagebox.showerror("Error", "Student count must be a number.")
        return

    MANAGE.add_course(course_code, course_name, int(student_count))
    display_courses.insert("", "end", values=(course_code, course_name, int(student_count)))
    messagebox.showinfo("Success", "Course added successfully.")
    clear_course_form()

def update_course():
    selected = display_courses.focus()
    if not selected:
        messagebox.showerror("Error", "Select a course to update.")
        return
    values = display_courses.item(selected, 'values')
    course_code = values[0]

    course_name = course_name_entry.get()
    student_count = student_count_entry.get()

    if not (course_name and student_count):
        messagebox.showerror("Error", "Please fill all fields.")
        return
    if not student_count.isdigit():
        messagebox.showerror("Error", "Student count must be a number.")
        return

    MANAGE.update_course(course_code, course_name, int(student_count))
    display_courses.item(selected, values=(course_code, course_name, int(student_count)))
    messagebox.showinfo("Success", "Course updated.")
    clear_course_form()

def delete_course():
    selected = display_courses.focus()
    if not selected:
        messagebox.showerror("Error", "Select a course to delete.")
        return
    values = display_courses.item(selected, 'values')
    course_code = values[0]

    if messagebox.askyesno("Confirm", "Are you sure you want to delete?"):
        MANAGE.delete_course(course_code)
        display_courses.delete(selected)
        clear_course_form()
        messagebox.showinfo("Deleted", "Course deleted.")

def clear_student_form():
    student_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    gender_var.set("")

def clear_course_form():
    course_code_entry.delete(0, tk.END)
    course_name_entry.delete(0, tk.END)
    student_count_entry.delete(0, tk.END)

def search_student():
    search_term = search_entry.get()
    for child in display_students.get_children():
        display_students.delete(child)
    results = MANAGE.get_students()
    found = False
    for student in results:
        if any(search_term.lower() in str(field).lower() for field in student):
            display_students.insert("", "end", values=student)
            found = True
    if not found:
        messagebox.showinfo("No Results", "No student matches your search.")

# --- STUDENT FORM ---
tk.Label(window, text="Reg No").grid(row=0, column=0)
student_id_entry = tk.Entry(window)
student_id_entry.grid(row=0, column=1)

tk.Label(window, text="Name").grid(row=1, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)

tk.Label(window, text="Age").grid(row=2, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=2, column=1)

tk.Label(window, text="Gender").grid(row=3, column=0)
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

tk.Label(window, text="Email").grid(row=4, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=4, column=1)

tk.Label(window, text="Phone").grid(row=5, column=0)
phone_entry = tk.Entry(window)
phone_entry.grid(row=5, column=1)

tk.Label(window, text="Course").grid(row=6, column=0)
course_entry = tk.Entry(window)
course_entry.grid(row=6, column=1)

tk.Button(window, text="Add Student", command=add_student).grid(row=7, column=0)
tk.Button(window, text="Update Student", command=update_student).grid(row=7, column=1)
tk.Button(window, text="Delete Student", command=delete_student).grid(row=7, column=2)

# --- STUDENT TREEVIEW ---
columns = ("Reg No", "Name", "Age", "Gender", "Email", "Phone", "Course")
display_students = ttk.Treeview(window, columns=columns, show="headings", height=8)
for col in columns:
    display_students.heading(col, text=col)
    display_students.column(col, width=100)
display_students.grid(row=8, column=0, columnspan=4)

# Scrollbar for student treeview
student_scrollbar = ttk.Scrollbar(window, orient="vertical", command=display_students.yview)
display_students.configure(yscroll=student_scrollbar.set)
student_scrollbar.grid(row=8, column=4, sticky='ns')

# --- COURSE FORM ---
tk.Label(window, text="Course Code").grid(row=0, column=5)
course_code_entry = tk.Entry(window)
course_code_entry.grid(row=0, column=6)

tk.Label(window, text="Course Name").grid(row=1, column=5)
course_name_entry = tk.Entry(window)
course_name_entry.grid(row=1, column=6)

tk.Label(window, text="Student Count").grid(row=2, column=5)
student_count_entry = tk.Entry(window)
student_count_entry.grid(row=2, column=6)

tk.Button(window, text="Add Course", command=add_course).grid(row=3, column=5)
tk.Button(window, text="Update Course", command=update_course).grid(row=3, column=6)
tk.Button(window, text="Delete Course", command=delete_course).grid(row=3, column=7)

# --- COURSE TREEVIEW ---
course_columns = ("Course Code", "Course Name", "Student Count")
display_courses = ttk.Treeview(window, columns=course_columns, show="headings", height=8)
for col in course_columns:
    display_courses.heading(col, text=col)
    display_courses.column(col, width=100)
display_courses.grid(row=8, column=5, columnspan=3)

# Scrollbar for course treeview
course_scrollbar = ttk.Scrollbar(window, orient="vertical", command=display_courses.yview)
display_courses.configure(yscroll=course_scrollbar.set)
course_scrollbar.grid(row=8, column=8, sticky='ns')

# --- SEARCH FUNCTION ---
tk.Label(window, text="Search Student").grid(row=9, column=0)
search_entry = tk.Entry(window)
search_entry.grid(row=9, column=1)
tk.Button(window, text="Search", command=search_student).grid(row=9, column=2)

# --- Load existing data ---
for student in MANAGE.get_students():
    display_students.insert("", "end", values=student)

for course in MANAGE.get_courses():
    display_courses.insert("", "end", values=course)

window.mainloop()