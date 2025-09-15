class animal():
    def __init__(self):
        print("animal created")
    def who_am_i(self):
        print("kateramma koduku")
    def eat(self):
        print("done with extra spice..!!")
    def __str__(self):
        return "i am animal"
class salaar(animal):
    def __init__(self):
        super().__init__()
        print("salaar created")
    def __str__(self):
        return "i am salaar"
my_species = salaar()
my_animal = animal()
print(f"{my_animal} {my_species}")

    
