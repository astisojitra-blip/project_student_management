students = []

while True:

    print("-----------------student management system-------------------")
    print("Select an option:")
    print("1.Add student:")
    print("2.Display all student:")
    print("3.Search student")
    print("4.Update student")
    print("5.Delete student")
    print("6.Display subject offered")
    print("7.Exit:")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":

        name = input("Enter student name:")
        age =int(input("Enter student age:"))
        course = input("Enter student course:")
        student ={"name": name, "age": age, "course": course}
        students.append(student)
        print("Student added successfully!!!")

    elif choice == "2":

        print("-----------------Student List-------------------")
        for student in students:
            print(student)

    elif choice == "3":

        name = input("Enter student name:")
        for student in students:
            if student['name'] == name:
                print(student)
                break
        else:
            print("student not found??")
    elif choice == "4":
        
        print("---------------Update student-------------------")
        name = input("Enter student name:")
        for student in students:
            if student['name'] == name:
                student["name"] = input("Enter new name:")
                student["age"] = int(input("Enter new age:"))
                student["course"] = input("Enter new course:")
                print("Student updated successfully!!!")
                break
        else:
            print("student not found??")

    elif choice == "5":

        print("---------------Delete student-------------------")
        name = input("Enter student name:")
        for student in students:
            if student['name'] == name:
                students.remove(student)
                print("Student deleted successfully!!!")
                break
        else:
            print("student not found??")

    elif choice == "6":
        print("\n--------Subject Name--------")
        print("Python")
        print("C++")
        print("PHP")

    elif choice == "7":

        print("Thank you for using the student management system!")
        break
    
    else:
        print("Invalid choice....")