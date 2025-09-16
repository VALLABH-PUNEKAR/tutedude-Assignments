student_marks={"Alice":85,"Vallabh":99,"Tony":95,"Peter":55}
name=input("Enter the Student 's Name: ")
if name in student_marks:
    print(name,"'s marks:",student_marks.get(name))
else:
    print("Student not Found")