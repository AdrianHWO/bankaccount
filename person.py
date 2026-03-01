class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi I am {self.name} and I'm {self.age} years old!")


person1 = Person("Aye Aye", 22)
person1.greet()

person2 = Person("Tun Tun", 12)
person2.greet()
