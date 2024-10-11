import json

# 读取 JSON 文件
with open('students.json', 'r') as file:
    data = json.load(file)
print(data)

# 访问学生列表
students = data['students']
print(students)

# 遍历学生列表并访问每个学生的信息
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    print(f"Grades: Math: {student['grades']['math']}, Science: {student['grades']['science']}")

# 计算每个学生的平均成绩
for student in students:
    grades = student['grades']
    average_grade = (grades['math'] + grades['science']) / 2
    print(f"Name: {student['name']}, Average Grade: {average_grade}")