class Dog:
    species = "Mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        #instance method 
    def description(self):
        return "{}  is {} years old".format(self.name, self.age)
     #instatnce method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
# Instantiate the Dog object
Mikey = Dog("Mikey", 6) 
print(Mikey.description())
print(Mikey.speak("Wouw, Wouw"))