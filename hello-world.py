print("Hello world")

msg = "hello world"

msg2 = msg.capitalize

print(msg)
print(msg2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name(self):
        print("Hallo. Ich heisse " + self.name )
        
    def print_age(self):
        print("Ich bin " + str(self.age) + " Jahre alt")
        
person1 = Person('Ben', 36)

print( person1.name )
print( person1.age )

person1.print_name();
person1.print_age();

class PersonSuper:
    pass
    
    
