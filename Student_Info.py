students=[]

while True:
    print("1.add students")
    print("2.display all students")
    print("3.update student information")
    print("4.delete student")
    print("5.student id of search")
    print("6.display subjects offered")
    print("7.exit")

    choice = int(input("enter your choice:"))
    match choice:
        case 1:
            id =int(input("Enter your id:"))
            name = input("Enter your name: ")
            age = int(input("Enter your age:"))
            course = input("Enter your course:")
            
            student={"id":id,"name":name,"age":age,"course":course}
            students.append(student)
            print("Student Added!")
            
        case 2:
            for student in students:
                print(student)
        case 3:
            id = int(input("Enter student ID to update:"))
            for student in students:
                student["id"]=int(input("enter new id:"))
                student["name"]=input("enter new name:")
                student["age"]=int(input("enter new age:"))
                student["course"]=input("enter new course:")
                break
            print(student)
        case 4:
            name=input("Enter name to delete:")
            
            for student in students:
                if student["name"]==name:
                    students.remove(student)
                    print("student deleted")
                    break
            else:
                print("student not found")
        case 5:
            id=int(input("Enter id to search:"))
            
            for student in students:
                if student["id"]==id:
                    print(student)
                    break
            else:
                print("student not found!")
        case 6:
            print("----Display Subjects----")
            print("1.AI")
            print("2.Python")
            print("3.ML")
        
        case 7:
            print("Thank you..")
            break
        
        case _:
            print("Invalid choice,Please Enter valid choice")           
                                     