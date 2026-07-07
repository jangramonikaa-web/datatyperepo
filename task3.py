#  dictionary and funtion 
student = {
    "name": "monika",
    "age": 18,
    "course": "python",
}
print(student.get("name"))  # Output: monika
print(student.get("city", "Not Found"))  # Output: Not Found
print(student.keys())  # Output: dict_keys(['name', 'age', 'course'])
print(student.values())  # Output: dict_values(['monika', 18, 'python'])
print(student.items())  # Output: dict_items([('name', 'monika'), ('age', 18), ('course', 'python')])
print(student.pop("age"))  # Output: 18
print(student.update({"age": 19}))  # Output: None
print(student.popitem())  # Output: ('course', 'python')
print(student.clear())  # Output: None
student_copy= student.copy()
print(student_copy)
student.setdefault("city","gurgaon")
keys=["name","age","course"]
new_dict= dict.fromkeys(keys)
print(keys)
print(len(student))

print(student)
print("name" in student)
print("salary" not in student)
