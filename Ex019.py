import random

print('=--Student name picker--=')
print('How many students do you want to register?')

nStudents = int(input('Number of students: '))
students = []
index = 0

while index < nStudents:
    studentName = input('Enter the name of student number {} '.format(index + 1))
    students.append(studentName)
    index += 1

# index = 0
# while index < len(students):
#     print(students[index])
#     index += 1

randStudent = random.randrange(0, len(students))
print('The student selected was: {}'.format(students[randStudent]))
