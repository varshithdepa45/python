class Salaar():
    species='dinosaur'
    def __init__(self,mybreed,mytype,myname):
        self.breed = mybreed
        self.type = mytype
        self.name = myname
    def roar(self):
        print(f"salaar devaratha raisaar and my name is {self.name}")
    pass
fav=Salaar(mybreed='shouryanga',mytype='moms kid',myname='salaar')
print(type(fav))
print(f"{fav.breed},{fav.type},{fav.species}")
choice = input("Do you want Salaar to roar? (yes/no): ").strip().lower() #.strip for spaces and .lower to lowercases
if choice == "yes":
    fav.roar()
else:
    print("You missed the greatest roar of all time!")