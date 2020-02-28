class Person(object):
    species = 'Homo sapiens'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old. My species is: {self.species}"

alex = Person('Alex', 24)

print(alex.talk())
print(type(alex))
print(dir(alex))

print(alex)