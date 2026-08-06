class Weapon:

    def attack(self):
        print("Attacking with weapon")


class Health:

    def __init__(self):
        self.hp = 100

    def show_health(self):
        print(f"Health: {self.hp}")


class Inventory:

    def show_items(self):
        print("Showing inventory")


class Player:

    def __init__(self):
        self.weapon = Weapon()
        self.health = Health()
        self.inventory = Inventory()


    def play(self):
        self.weapon.attack()
        self.health.show_health()
        self.inventory.show_items()


player = Player()

player.play()