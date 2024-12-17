student_number = int(input("Enter student number : "))
student_name = input("Enter student name : ")
c_marks = int(input("Enter student marks in C :"))
cpp_marks =int(input("Enter student marks in C++ :"))
java_marks = int(input("Enter student marks in java :"))
total_marks = c_marks + cpp_marks + java_marks
print("Total marks of the student : ",total_marks)
avg_marks = total_marks / 3
print("Average marks of the student : ",avg_marks)
if avg_marks>70 :
    result = "Pass"
    print("Result is : ",result)
else :
    result = "Fail"
    print("Result is : ",result)

def calculate_grade(avg_marks):
    if (avg_marks >=90):
        print("Grade is : A+")
    elif (avg_marks >=80):
        print("Grade is : A")
    elif (avg_marks >=70):
        print("Grade is : B")
    else :
        print("Grade is : F")
grade = calculate_grade(avg_marks)

if (result == 'Pass'):
    print(grade)