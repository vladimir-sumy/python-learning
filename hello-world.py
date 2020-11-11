print("Hello world")

msg = "hello world"

msg2 = msg.capitalize

print(msg)
print(msg2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
person1 = Person('John', 66)

print( person1.name )
print( person1.age )