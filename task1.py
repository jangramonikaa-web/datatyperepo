# python praogram
student_name = input("Enter your name: ")
student_age= int(input("Enter your age: "))
student_height= float(input("Enter your height in feet: "))
student_ID= input("Enter your student ID: ")
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Height:", student_height)
print("Student ID:", student_ID)  

if student_name:
    print("return name if present.")
else:
    print("return name if not present.")
# list of courses
courses=[ "python","ai","data science"]
print(type(courses))

#  tuple of fav programming language
programming_language = ( "python"," java"," c++")
print(type(programming_language))

# set of skills
skills ={ "commumication","programming", "presentation"}
print(type(skills))

#  dictionary of student details
student_details = {
    "name":"monika",
    "age":18,
    "course":"python",
    "city":"bhiwani"
}

print(type(student_details))