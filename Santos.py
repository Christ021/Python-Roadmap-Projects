# THIS IS A LIST

students = ["RM"] 

students.append("Maria")
students.append("John")
students.append("Carlos")
students.append("added") 

print("Student List:", students)

check_names = ["Added", "Maria", "John", "Carlos", "RM"]
for search_name in check_names:
    if search_name in students:
        print(search_name, "is enrolled.")
    else:
        print(search_name, "is not enrolled.")

students.remove("RM")  # 5. .remove() hindi .delete()
print("Updated Student List:", students)

students.remove("John")
print("Updated Student List:", students)

students.remove("Carlos")
print("Updated Student List:", students)``