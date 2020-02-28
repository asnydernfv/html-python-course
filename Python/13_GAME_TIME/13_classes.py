class Player(object):
    hp = 100
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name} has {self.hp} hp"
    def takeDamage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def heal(self, hp):
        self.hp = self.hp + hp
        if self.hp > 100:
            self.hp = 100
        return self.hp

Alex = Player("Alex")
print(Alex)
Alex.takeDamage(110)
print(Alex)
Alex.heal(200)
print(Alex)