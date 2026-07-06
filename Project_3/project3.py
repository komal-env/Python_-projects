students = []

while True:
    print("\n===== Student Report Card =====")
    print("1. Add Students")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Class Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ------------------ ADD STUDENTS ------------------
    if choice == "1":
        n = int(input("How many students do you want to add? "))

        for i in range(n):
            print("\nStudent", i + 1)

            name = input("Enter Name: ")
            roll = input("Enter Roll No: ")

            marks = []
            total = 0
            fail = False

            for j in range(5):
                mark = int(input(f"Enter Marks of Subject {j+1}: "))

                while mark < 0 or mark > 100:
                    print("Invalid Marks! Enter between 0 and 100.")
                    mark = int(input(f"Enter Marks of Subject {j+1}: "))

                marks.append(mark)
                total += mark

                if mark < 33:
                    fail = True

            percentage = total / 5

            if fail:
                grade = "Fail"
                status = "Fail"

            else:
                status = "Pass"

                if percentage >= 90:
                    grade = "A+"

                elif percentage >= 80:
                    grade = "A"

                elif percentage >= 70:
                    grade = "B"

                elif percentage >= 60:
                    grade = "C"

                elif percentage >= 40:
                    grade = "D"

                else:
                    grade = "Fail"
                    status = "Fail"

            student = [name, roll, marks, total, percentage, grade, status]
            students.append(student)

        print("\nStudents Added Successfully!")

    # ------------------ SHOW ALL STUDENTS ------------------
    elif choice == "2":

        if len(students) == 0:
            print("No Student Records Found.")

        else:
            print("\n===== Student Records =====")

            for student in students:
                print("--------------------------")
                print("Name :", student[0])
                print("Roll :", student[1])
                print("Marks :", student[2])
                print("Total :", student[3])
                print("Percentage :", round(student[4], 2), "%")
                print("Grade :", student[5])
                print("Status :", student[6])

    # ------------------ SEARCH STUDENT ------------------
    elif choice == "3":

        if len(students) == 0:
            print("No Student Records Found.")

        else:
            search = input("Enter Name or Roll No: ")

            found = False

            for student in students:

                if student[0] == search or student[1] == search:
                    print("\nStudent Found")
                    print("---------------------")
                    print("Name :", student[0])
                    print("Roll :", student[1])
                    print("Marks :", student[2])
                    print("Total :", student[3])
                    print("Percentage :", round(student[4], 2), "%")
                    print("Grade :", student[5])
                    print("Status :", student[6])

                    found = True
                    break

            if found == False:
                print("Student Not Found.")

    # ------------------ CLASS TOPPER ------------------
    elif choice == "4":

        if len(students) == 0:
            print("No Student Records Found.")

        else:
            topper = students[0]

            for student in students:
                if student[4] > topper[4]:
                    topper = student

            print("\n===== Class Topper =====")
            print("Name :", topper[0])
            print("Roll :", topper[1])
            print("Percentage :", round(topper[4], 2), "%")
            print("Grade :", topper[5])

    # ------------------ EXIT ------------------
    elif choice == "5":
        print("Thank You! Program Closed.")
        break

    # ------------------ INVALID CHOICE ------------------
    else:
        print("Invalid Choice! Please Enter 1 to 5.")