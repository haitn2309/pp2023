# Input number of students in a class
def input_num_students():
    num_students = int(input("Enter the number of students: "))
    return num_students


# Create a list to store student information
students = []
n=input_num_students()
# Input student information: id, name, DoB
for i in range(n):
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    students.append({
        "id": student_id,
        "name": student_name,
        "dob": student_dob,
        "courses": {}
    })

# Input number of courses
num_courses = int(input("Enter the number of courses: "))

# Create a list to store course information
courses = []

# Input course information: id, name
for i in range(num_courses):
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses.append({
        "id": course_id,
        "name": course_name
    })


# Input marks for student in each course
marks=[]
for student in students:
    for course in courses:
        mark = input(f"Enter {student['name']}'s mark for {course['name']}: ")
        marks.append(mark)

# Print the information for each student
i=0
for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Date of Birth:", student["dob"])
    print("Courses:")
    for course in courses:
        print(f"{course['name']}:",marks[i])
        i+=1