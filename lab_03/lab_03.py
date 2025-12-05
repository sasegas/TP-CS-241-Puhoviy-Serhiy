import sys
from student import Student
from student_list import StudentList
from utils import FileManager

def main():
    filename = "lab3.csv"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file_manager = FileManager(filename)
    stud_list = StudentList()
    
    loaded_data = file_manager.load_data()
    for s in loaded_data:
        stud_list.add_student(s)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                name = input("Please enter student name: ")
                surname = input("Please enter student surname: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                new_student = Student(name, surname, phone, email)
                stud_list.add_student(new_student)
                stud_list.print_all()
            
            case "u":
                print("Existing element will be updated")
                name = input("Please enter name to be updated: ")
                found = stud_list.find_student(name)
                
                if found:
                    print(f"Updating student: {found}")
                    new_name = input(f"Enter new name [{found.name}]: ") or found.name
                    new_surname = input(f"Enter new surname [{found.surname}]: ") or found.surname
                    new_phone = input(f"Enter new phone [{found.phone}]: ") or found.phone
                    new_email = input(f"Enter new email [{found.email}]: ") or found.email
                    
                    updated_student = Student(new_name, new_surname, new_phone, new_email)
                    stud_list.update_student(name, updated_student)
                    stud_list.print_all()
                else:
                    print("Student not found")

            case "d":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                stud_list.delete_student(name)
                stud_list.print_all()

            case "p":
                print("List will be printed")
                stud_list.print_all()

            case "x":
                print("Exit()")
                file_manager.save_data(stud_list.get_all_students())
                break
            
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()