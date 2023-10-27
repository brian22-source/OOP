class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


person1 = Person("Brian", 20)
person2 = Person("Angel", 25)
print(person1.greet())  # Output: Hello, my name is Alice and I'm 30 years old.
print(person2.greet())  # Output: Hello, my name is Bob and I'm 25 years old.
