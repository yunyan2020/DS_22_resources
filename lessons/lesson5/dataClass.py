from dataclasses import dataclass


@dataclass(init=True, repr=False, kw_only=True)
class Animal:
    height: float
    weight: float
    name: str
    diet: str

    def update_name(self, name):
        self.name = name

    # def __str__(self):
    #    return "Hello"


@dataclass(kw_only=True)
class Dog(Animal):
    race: str
    pass


@dataclass(kw_only=True)
class Cat(Animal):
    race: str
    pass


mouse = Animal(name="Mouse", height=5, weight=300, diet="Omnivore")
mouse.update_name("Rat")
fido = Dog(race="Dalmatian", name="Fido",
           height=10, weight=1000, diet="Omnivore")

print(mouse)

print(fido)
# meowson = Cat(fur ="Naked",diet="Carnivore",height="300")
