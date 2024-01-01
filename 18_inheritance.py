# Inheritance
print("Class Inheritance")

class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")

class Doctor(Person):
    # pass # python will skip the empty code
    def heal(self):
        print("Heals 10 health points")

class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Moves 6 paces")

class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisible")
    def heal(self):
        print("Heals 15 health points")

character_1 = Person()
character_1.move()
character_2 = Doctor()
character_2.move()
character_2.heal()
character_3 = Fighter()
character_3.move()
character_3.fight()
character_4 = Wizard()
character_4.heal()
character_4.move()