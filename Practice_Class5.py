import logging

class Character:
    """Класс персонаж"""
    hp = 100
    mana = 100
    stamina = 100
    skillpoints = 0

    def level_up(self, hp, mana, stamina, skillpoints):
        """Метод изменения характеристик персонажа"""
        if self.skillpoints % 500 == 0:
            self.hp += 20
            self.mana += 5
            self.stamina += 10
            logging.basicConfig(filename="Practice_part5.log", level=logging.INFO, filemode="w",
                                format="%(asctime)s %(message)s")
            logging.info("Персонаж повысил уровень")
        else:
            logging.basicConfig(filename="Practice_part5.log", level=logging.WARNING, filemode="w",
                                format="%(asctime)s %(message)s")
            logging.warning("Недостаточно опыта для повышения")
        return f"Здоровье: {self.hp}, Мана: {self.mana}, Выносливость: {self.stamina}"

ork = Character()
ork.skillpoints = 500
print(ork.level_up(120, 100, 120, ork.skillpoints))
ork.skillpoints = 700
print(ork.level_up(ork.hp, ork.mana, ork.stamina, ork.skillpoints))
ork.skillpoints = 1000
print(ork.level_up(ork.hp, ork.mana, ork.stamina, ork.skillpoints))
