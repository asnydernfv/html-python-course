#!/usr/local/bin/python3
animals = ["cat", "dog", "fish", "iguana", "deer"]
print("1.")
if "cat" in animals:
    print("Cat is in the list!")
if "dog" in animals:
    print("Dog is in the list!")
print("You do not have to have and else statement!")

print("2.")
if "monkey" or "cat" in animals:
    print("Monkey or Cat is in the list")
else:
    print("Monkey or cat not in the list")

print("3.")
if "monkey" or "cat" in animals:
    if "monkey" in animals:
        print("Monkey is in the list")
    else:
        print("Monkey is not in the list")
    if "cat" in animals:
        print("cat is in the list")
    if "cat" not in animals:
        print("Cat is not in the list")
else:
    print("Neither cat nor monkey are in the list")