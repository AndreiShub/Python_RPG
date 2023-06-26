import random
import string


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
    def __init__(self) -> None:
        name = "Кейн"
        hp = 10
        atk = 1
        super().__init__(name, hp, atk)

    def flee(self):
        print("running")

    def cry(self):
        print("crying")

    def fight(self):
        print("fighting")

    def rest(self):
        print("resting")

    __synonyms = [({"сбежать", "убежать"}, flee),
                  ({"отдохнуть", "поспать"}, rest),
                  ({"сражаться", "биться"}, fight),]
    commands = {}
    for i in __synonyms:
        commands.update(commands.fromkeys(i[0], i[1]))

    def decide_action(self):
        player_input = input("> ").lower().strip(string.punctuation)
        try:
            Player.commands[player_input](self)
        except KeyError:
            print("no command")
