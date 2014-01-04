# define a class called Animal that can make a sound
class Animal:
    def __init__(self):
        self.name  = None
        self.sound = None

    def PrintSound(self):
        print( "My sound is ", self.sound )

    def PrintName(self):
        print( "I am a ", self.name )

# Derive a Dog from the Animal class
# Animal is the parent class, Dog is the child class
class Dog(Animal):
    def __init__(self):
        Animal.name  = 'Dog'
        Animal.sound = 'bark'

# Derive a Cat from the Animal class
class Cat(Animal):
    def __init__(self):
        self.name  = 'Cat'
        self.sound = 'meow'
        

def main():
    # See what the animals do
    animal_1 = Dog()
    animal_1.PrintName()
    animal_1.PrintSound()
    
    animal_2 = Cat()
    animal_2.PrintName()
    animal_2.PrintSound()
    

if __name__ == "__main__":
    main()
