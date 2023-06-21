import random


class Entity:
    def __init__(self, name, hp, atk) -> None:
        self.name = name
        self.hp = hp
        self.atk = atk


class Enemy(Entity):
    enemy_names = [
        "Чёрт",
        "Суккуб",
        "Полтергейст",
        "Призрак",
        "Кошмар",
        "Злой Дух"]

    def __init__(self) -> None:
        name = random.choice(Enemy.enemy_names)
        hp = random.randint(1, 10)
        atk = random.randint(1, 10)
        super().__init__(name, hp, atk)


class Player(Entity):
    def __init__(self, name, hp, atk) -> None:
        name = "Кейн"
        hp = 10
        atk = 1
        super().__init__(name, hp, atk)


def main():
    pass


if __name__ == "__main__":
    main()
