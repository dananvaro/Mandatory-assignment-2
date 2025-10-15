from study_reminders.students import Students 
from study_reminders.reminder_generator import generate_reminder 
from study_reminders.reminder_sender import send_reminder 
from study_reminders.logger import log_reminder
from study_reminders.students_manager import StudentsManager
from study_reminders.scheduler_ import schedule_reminders 


# Tests the object Student Manager

# Calls the Student manager class
studentManager = StudentsManager()

# Loads all the students
studentList = studentManager.load_students()

print("-----------------------------------------------")

# List all the students
studentManager.list_students()

# Adds the new student
studentManager.add_student("Minh", "Minh@gmail.com", "Data Science", "10:00 AM")

print("-----------------------------------------------")
studentManager.list_students()

# Removes studen
studentManager.remove_student("Minh")

print("-----------------------------------------------")
studentManager.list_students()

print("-----------------------------------------------")

# Send a reminder with a spesific name and email
for students in studentList:
    reminder = generate_reminder(students['name'], students['course'])
    send_reminder(students['email'], reminder)
    log_reminder(students, reminder)
print("-----------------------------------------------")

schedule_reminders(studentManager,generate_reminder, send_reminder,log_reminder)
