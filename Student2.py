# Initial list of students with dictionaries
students = [
    {"name": "Jahaira", "hometown": "Detroit", "favorite_food": "Chicken"},
    {"name": "Sevyn", "hometown": "Farmington Hills", "favorite_food": "Fries"},
    {"name": "Aniya", "hometown": "Southfield", "favorite_food": "Pasta"}
]


def list_names(students):
    """
    Prints out the list of student names with their index.
    Takes in the list of students as a parameter.
    """
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']}")


def get_new_student():
    """
    Prompts the user to input a new student's information and returns a dictionary.
    """
    name = input("Enter the student's name: ")
    hometown = input("Enter the student's hometown: ")
    favorite_food = input("Enter the student's favorite food: ")

    return {"name": name, "hometown": hometown, "favorite_food": favorite_food}


def main():
    """Main function to handle user interaction and loop through options."""
    while True:
        # Ask the user what they want to do
        option = input(
            "\nType 'add' to create a new student, 'view' to look at existing students, or 'quit' to exit: ").lower()

        if option == 'quit':
            print("Goodbye!")
            break  # Exit the loop and end the program
        elif option == 'view':
            list_names(students)  # Show the list of students

            try:
                # Ask the user to select a student by index
                student_index = int(input("Enter the number of the student you'd like to view: ")) - 1

                if 0 <= student_index < len(students):
                    student = students[student_index]
                    print(f"\nSelected student: {student['name']}")

                    # Ask what info they want to see
                    detail = input("Would you like to see their 'hometown' or 'favorite food'? ").lower()

                    if detail in student:
                        print(f"{student['name']}'s {detail} is {student[detail]}.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif option == 'add':
            new_student = get_new_student()  # Get a new student's details
            students.append(new_student)  # Add the new student to the list
            print(f"{new_student['name']} has been added.")
        else:
            print("Invalid option. Please type 'add', 'view', or 'quit'.")


# Run the program
main()