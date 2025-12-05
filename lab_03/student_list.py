from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print("Student has been added")

    def delete_student(self, name):
        for item in self.students:
            if item.name == name:
                self.students.remove(item)
                print(f"Student {name} has been deleted")
                return
        print("Element was not found")

    def find_student(self, name):
        for item in self.students:
            if item.name == name:
                return item
        return None

    def update_student(self, old_name, new_student: Student):
        student_to_remove = self.find_student(old_name)
        if student_to_remove:
            self.students.remove(student_to_remove)
            self.add_student(new_student) 
            print("Student has been updated")
        else:
            print("Student not found")

    def get_all_students(self):
        return self.students

    def print_all(self):
        for student in self.students:
            print(student)