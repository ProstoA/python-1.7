class Animals:
    food = 'plant'
    growth = True
    reproduction = True
    noise = "wow"

    def wow(self):
        print(self.noise)


class Artiodactyls(Animals):
    hoof = True


class Birds(Animals):
    wing = True


class Cows(Artiodactyls):
    give_milk = True


class Goats(Artiodactyls):
    give_milk = True


class Sheep(Artiodactyls):
    give_meat = True


class Pigs(Artiodactyls):
    give_meat = True


class Ducks(Birds):
    give_meat = True
    noise = "crya-crya"


class Chickens(Birds):
    give_meat = True


class Geese(Birds):
    give_meat = True

    def wow(self):
        print("GA-GA")


g1 = Ducks()
g1.wow()
a1 = Animals()
a1.wow()
