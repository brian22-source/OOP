# Parent class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Parent class 2
class Company:
    def __init__(self, company_name, employee_id):
        self.company_name = company_name
        self.employee_id = employee_id

    def display_company_info(self):
        print(f"Company: {self.company_name}, Employee ID: {self.employee_id}")


# Child class Employee inherits from both Person and Company
class Employee(Person, Company):
    def __init__(self, name, age, company_name, employee_id):
        # Initialize attributes of both parent classes
        Person.__init__(self, name, age)
        Company.__init__(self, company_name, employee_id)

    def display_employee_info(self):
        # Call methods of both parent classes
        self.display_person_info()
        self.display_company_info()


# Create an instance of the Employee class
employee = Employee("Brian Mbithi", 30, "ABC Inc.", "E12345")

# Call the display_employee_info method to print employee information
employee.display_employee_info()
