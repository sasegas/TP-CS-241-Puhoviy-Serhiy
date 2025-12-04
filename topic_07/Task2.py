class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

students = [
    Student("Андрій", 21),
    Student("Олена", 19),
    Student("Богдан", 22),
    Student("Вікторія", 20)
]

def main():
	sorted_by_age = sorted(students, key=lambda student: student.age)

	print("--- Сортування за віком (від найменшого) ---")
	for student in sorted_by_age:
		print(student)


	sorted_by_name = sorted(students, key=lambda student: student.name)

	print("\n--- Сортування за ім'ям (алфавіт) ---")
	for student in sorted_by_name:
         print(student)

main()