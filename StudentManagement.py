students=[]
while True:
    print("1. Add student")
    print("2. View students")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        name =input("Enter student name:")
        age=input("Enter student age:")
        course=input("Enter student course:")
        students.append({'name':name, 'age':age, 'course':course})
    elif choice == '2':
        print("-------- Student List --------")
        for student in students:
            print(f"name: {student['name']}, age: {student['age']}, course: {student['course']}")
    elif choice == '3':
        print("exiting...")
        break
else:
    print("invalid choice. please try again.")