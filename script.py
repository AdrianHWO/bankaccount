class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof Woof")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner1 = Owner("Aye Aye", "Yangon", "09112233")
dog1 = Dog("Ne Kyar", "Terrier", owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

owner2 = Owner("Tun Tun", "Mandalay", "09444555")
dog2 = Dog("Pu Lone", "Burmese Stary", owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.contact_number)
