#see how method over riding works in oops. 

#example 1 

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a sound")
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")
        self.make_sound()

class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        print(f"{self.name} says Woof! 🐕")

class Cat(Animal):
    def make_sound(self):  # Overriding parent method
        print(f"{self.name} says Meow! 🐱")

class Cow(Animal):
    def make_sound(self):  # Overriding parent method
        print(f"{self.name} says Moo! 🐄")

# Polymorphism in action!
animals = [Dog("Tommy"), Cat("Whiskers"), Cow("Kamadhenu")]

for animal in animals:
    animal.introduce()  # Same method call, different behaviors!

#################
#example 2
class Learning:
    def __init__(self,subject,timeperiod,level):
        self.subject= subject
        self.timeperiod=timeperiod
        self.level=level
    
    def learning_method(self):
        print('this is shravana')

class Trilo(Learning):
    def __init__(self, subject, timeperiod, level,mentor):
        super().__init__(subject, timeperiod, level,)
        self.mentor=mentor 
    
    def learning_method(self):
        print(f"learning is {self.mentor}")

l1 = Trilo('philo','1 month',5,'sarrthi')
l1.learning_method()
