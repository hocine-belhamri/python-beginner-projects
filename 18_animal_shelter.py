class Animal:
    nbr_animals = 0
    def __init__(self,name, age, is_available):
        self.name = name
        self.age = age
        self.is_available = is_available
        Animal.nbr_animals += 1

    def adopt(self):
        self.is_available = False
        Animal.nbr_animals -= 1
    def describe(self):
        if self.is_available:
            print(f"{self.name} is {self.age} years old it is available")
        else:
            print(f"{self.name} is {self.age} years old it is not available")
class Dog(Animal):
    def __init__(self, name, age, is_available, breed):
        super().__init__(name, age, is_available)
        self.breed = breed
    def Breed(self):
        print(f"the dog's breed is {self.breed}")
    def bark(self):
        print("woaf")
    def describe(self):
        super().describe()
        self.Breed()
        self.bark()
class Cat(Animal):
    def __init__(self, name, age, is_available, indoor):
        super().__init__(name, age, is_available)
        self.indoor = indoor
    def Indoor(self):
        if self.indoor:
            print(f"the {self.name} is indoor")
        else:
            print(f"the {self.name} is not indoor")
    def purr(self):
        print("meow")
    def describe(self):
        super().describe()
        self.Indoor()
        self.purr()
class Bird(Animal):
    def __init__(self, name, age, is_available, can_fly):
        super().__init__(name, age, is_available)
        self.can_fly = can_fly
    def Can_fly(self):
        if self.can_fly:
            print(f"the {self.name} can fly")
        else:
            print(f"the {self.name} can't fly")
    def chirp(self):
        print("chew chew")
    def describe(self):
        super().describe()
        self.Can_fly()
        self.chirp()

dog = Dog("spike" ,10 ,True , "bull dog")
cat = Cat("thomas" , 4, True ,True)
bird = Bird("joujou"  , 2 , True , True)
animals = [dog , cat , bird]
for animal in animals:
    animal.describe()
print(f"the number of animals is: {Animal.nbr_animals}")
adopted = input("enter the name of the animal u want to inherit: ").lower()
for animal in animals:
    if adopted == animal.name:
        animal.adopt()
print(f"the number of animals is: {Animal.nbr_animals}")
