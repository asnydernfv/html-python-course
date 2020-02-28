#!/usr/local/bin/python3

animals = ["cat", "dog", "fish", "Kangaroo"]

# for animal in animals:
#     print(animal)


# for index, animal in enumerate(animals):
#     print(index+1, animal)


for index, animal in enumerate(animals):
        print(index+1, animal)


people = [{"name": "Alex", "age": 24}, {"name": "Tracy", "age": 21}, {"name": "Bob", "age": 12}]

for person in people:
    name = person['name']
    age = person['age']
    if age >= 18:
        print(name, "is an adult")
    else:
        print(name, "is only", age)

