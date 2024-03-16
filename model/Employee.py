class Employee:
    def __init__(self, name, year_of_join, salary, address):
        self.name = name
        self.year_of_join = year_of_join
        self.salary = salary
        self.address = address

    def print_employee_details(self):
        print(f'{self.name:<10} {self.year_of_join:<16} {self.address}')
