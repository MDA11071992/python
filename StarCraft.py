class Terran():
    """создаём Человека"""
    health = 10
    damage = 2

    def __init__(self):
        """Объект произносит боевой клич при появлении"""
        print("Зададим им жару!")

    def death(self):
        print("Человек погиб.")

    def shoot(self, enemy):
        if self.health != 0:
            """Атакуем врага"""
            enemy.health -= self.damage
            print("У зерга", enemy.health, "HP.")
            if enemy.health == 0:
                enemy.death()


class Zerg():
    """Создаём Зерга"""
    health = 8
    damage = 3

    def __init__(self):
        """Объект произносит боевой клич при появлении"""
        print("Ггр-гхгх!!")

    def death(self):
        print("Зерг погиб.")
        del self

    def bite(self, enemy):
        if self.health != 0:
            """Атакуем врага"""
            enemy.health -= self.damage
            print("У человека", enemy.health, "HP.")
            if enemy.health == 0:
                enemy.death()


Rainor = Terran()
Zergling = Zerg()


while Rainor.health != 0 and Zergling.health != 0:
    Rainor.shoot(Zergling)
    Zergling.bite(Rainor)
print("Битва окончена.")