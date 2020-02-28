def capitalize(word):
    new_word = word[:1].upper() + word[1:]
    return new_word

print(capitalize('hello'))


def count(number):
    if hasattr(number, '__round__') and not hasattr(number, 'is_integer'):
        i = 1
        while i <= number:
            print(i)
            i+=1
    else:
        raise TypeError("Argument must be an integer")
count(10)