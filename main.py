print("Hello amigocode ")

# "variables"

fullName = "J jam"
age = 29
number = [1, 2, 3, 4]
name, age = "jam", 60
print(name)
# constants
PI = 3.14
name = input("Enter your name: ")
print("Hello", name + "!")

# tuples
lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
#      indexes  0  1       2      3   4   5

# lucky_numbers[0] = 90  # tuples are immutable
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))


# Data Types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# inheritance
class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ItalianChef(Chef):
    def make_pasta(self):
        print("The chef makes pasta")

    def make_special_dish(self):
        print("The chef makes chicken parm")


myChef = Chef()
myChef.make_chicken()

myItalianChef = ItalianChef()
myItalianChef.make_special_dish()
