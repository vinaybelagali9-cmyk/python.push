# student_marks.py

name = input("Enter student's name: ")
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    status = "Pass"
else:
    status = "Fail"

print("\n--- Student Report ---")
print(f"Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:2f}")
print(f"Status: {status}")