Student Management System

1. Overview
This is a GUI-based Student Management System built using Python.
The application uses Tkinter for the graphical user interface and SQLite for the database backend.
It enables administrators to efficiently manage student and course data, providing functions to add, update, delete, and search records.

2. Modules Used
- tkinter: Used for creating the GUI.
- ttk: A submodule of tkinter for themed widgets like Treeview.
- sqlite3: Provides an interface for the SQLite database.
- messagebox: Displays pop-up messages for alerts, confirmations, and errors.
- MANAGE: A custom module containing functions to interact with the database.

3. Login System
The system has a secure login interface that only allows admin access.
Admin credentials are hardcoded for demonstration:
Username: Admin
Password: #270707
Login Functionality:
The login() function verifies credentials. If they are valid, the admin is taken to the dashboard.
Otherwise, an error message is shown.
The logout() function confirms logout and returns to the login screen.

4. Window Layout
The window is the main container with a size of 750x550 pixels and a light teal background.
It contains multiple frames for login, dashboard, student, and course management.

5. Dashboard
The dashboard provides navigation buttons:
- Manage Students: Opens the student management interface.
- Manage Courses: Opens the course management interface.
- Logout: Logs out the current user.

6. Student Management
This section allows the admin to:
- Add new students with complete details.
- Update existing student records.
- Delete student records after confirmation.
- Search students by any keyword.
- View all students in a table.
The Treeview widget displays all records, and fields include Reg No, Name, Age, Gender, Email, Phone, and Course.

7. Course Management
The course section allows the admin to:
- Add new courses with Course Code, Name, and Student Count.
- Delete selected courses.
- View all courses in a table.
Like the student section, a Treeview widget is used for display.

8. Database Schema
The database is SQLite-based and contains two tables:

Table: students
- reg_no (Primary Key)
- name
- age
- gender
- email
- phone
- course

Table: courses
- course_code (Primary Key)
- course_name
- student_count

9. Database Functions (MANAGE Module)
Student Functions:
- add_student(): Inserts a new student.
- update_student(): Modifies existing student data.
- delete_student(): Removes a student by Reg No.
- get_students(): Returns all student records.

Course Functions:
- add_course(): Inserts a new course.
- update_course(): Updates a course's details.
- delete_course(): Deletes a course by code.
- get_courses(): Returns all course records.

10. Error Handling
Input fields are validated before submission.
Errors like missing or incorrect input are caught and displayed.
Confirmation dialogs are used for destructive actions like delete and logout.

Follow these steps to run the Student Management System on your computer:
• Ensure Python 3.x is installed on your system.
• Install the required libraries (Tkinter and sqlite3 are standard with Python).
• Download the project files including the main script and MANAGE module.
• Open the main Python script and locate the section where the window is defined.
• Run the main script (`python main.py`) to launch the application.

 Suggestions for Improvement
- Use password hashing for secure login.
- Enable data export to CSV or PDF.
- Include filtering options for better search experience.
