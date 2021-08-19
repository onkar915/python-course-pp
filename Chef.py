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
