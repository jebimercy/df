from main import Student

my_student = Student.select()
for student in my_student:
    print(student.name, student.Id, student.room)

