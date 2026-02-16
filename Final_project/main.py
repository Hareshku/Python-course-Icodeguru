from student_manager import StudentManager


def display_menu():
    print("\n" + "="*50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")
    print("="*50)


def get_marks():
    marks = []
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    return marks


def display_student(student):
    print(f"\nID: {student.id}")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Marks: {student.marks}")
    print(f"Total: {student.total}")
    print(f"Percentage: {student.percentage:.2f}%")
    print(f"Grade: {student.grade}")


def main():
    manager = StudentManager()
    
    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == '1':
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                marks = get_marks()
                student = manager.add_student(student_id, name, age, marks)
                print("\nStudent added successfully!")
                display_student(student)
            
            elif choice == '2':
                students = manager.view_students()
                if not students:
                    print("\nNo students found.")
                else:
                    print(f"\nTotal Students: {len(students)}")
                    for student in students:
                        display_student(student)
            
            elif choice == '3':
                student_id = int(input("Enter Student ID to search: "))
                student = manager.search_student(student_id)
                if student:
                    display_student(student)
                else:
                    print("\nStudent not found.")
            
            elif choice == '4':
                student_id = int(input("Enter Student ID to update: "))
                student = manager.search_student(student_id)
                if not student:
                    print("\nStudent not found.")
                    continue
                
                print("\nLeave blank to keep current value")
                name = input(f"Enter new name [{student.name}]: ").strip()
                age_input = input(f"Enter new age [{student.age}]: ").strip()
                age = int(age_input) if age_input else None
                
                update_marks = input("Update marks? (y/n): ").lower()
                marks = get_marks() if update_marks == 'y' else None
                
                manager.update_student(
                    student_id,
                    name if name else None,
                    age,
                    marks
                )
                print("\nStudent updated successfully!")
                display_student(manager.search_student(student_id))
            
            elif choice == '5':
                student_id = int(input("Enter Student ID to delete: "))
                confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ")
                if confirm.lower() == 'y':
                    manager.delete_student(student_id)
                    print("\nStudent deleted successfully!")
            
            elif choice == '6':
                print("\nThank you for using Student Management System!")
                break
            
            else:
                print("\nInvalid choice. Please try again.")
        
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
