from random import shuffle

print('=--Presentation order picker--=')
print('How many students do you want to register?')

nStudents = int(input('Students: '))
students = []
index = 0

while index < nStudents:
    studentName = input('Enter the name of student number {} '.format(index + 1))
    students.append(studentName)
    index += 1

shuffle(students)
print('The order of presentation is: \n{}'.format(students))
