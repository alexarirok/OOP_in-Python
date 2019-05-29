class Dog:
    species = "Mammall"

    def __init__(self, name, age):
        self.name = name
        self.age = age

brian = Dog("Brian", 5)
mike = Dog("Mike", 4)
john = Dog("John", 12)

def get_biggest_num(*args):
    return max(args)

print ("the oldest dog is {} years old".format(get_biggest_num(brian.age, john.age, mike.age)))
