from model.Person import Person
from model.Animal import Animal
from model.Rectangle import Rectangle
from model.Employee import Employee

if __name__ == '__main__':
    # EX1
    first_student = Person("Gil", "Cohen", 23, "Male", "Tel Aviv", None)
    second_student = Person("Or", "Levi", 21, "Female", "Ramat Gan", None)
    third_student = Person("Mor", "Ganon", 24, "Female", "Holon", None)

    print(type(first_student))
    print(type(second_student))
    print(type(third_student))

    print(getattr(first_student, 'first_name'))
    print(setattr(first_student, 'city', 'Bat Yam'))

    print(second_student.first_name)
    second_student.age = 22
    print(second_student.age)

    # EX2
    dog = Animal("dog", "house", "medium", "brown", "house pet")
    fish = Animal("fish", "sea", "small", "silver", "osteichthyes")
    tiger = Animal("tiger", "jungle", "big", "brown with black stripes", "cats")

    first_student.add_animal(dog)
    first_student.add_animal(dog)
    first_student.remove_animal(dog)
    first_student.remove_animal(fish)

    # EX3
    rectangle = Rectangle(6, 8)
    print(f'The area of the rectangle: {rectangle.get_area()}')

    # EX4
    first_employee = Employee("Robert", 1994, 20000,"64C- WallsStreet")
    second_employee = Employee("Sam", 2000, 15000, "68D- WallsStreet")
    third_employee = Employee("John", 1999, 16000, "26B- WallsStreet")

    print()
    print(f"{'Name':<10} {'Year of joining':<16} {'Address'}")
    first_employee.print_employee_details()
    second_employee.print_employee_details()
    third_employee.print_employee_details()
