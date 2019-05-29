#Creating a method in python

class Point:
    def reset(self):  #method
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)
