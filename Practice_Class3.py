class Animals:
    """Класс инициализации Animals"""

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, nickname: str, age: int, sound: str):
        self.nickname = nickname
        self.age = age
        self.sound = sound

    def voice(self, sound: str) -> str:
        """Метод определения voice"""
        return self.sound


class Cat(Animals):
    """Дочерний класс Animals"""

    def __init__(self, nickname: str, age: int, sound: str):
        super().__init__(nickname, age, sound)
        self.sound = "Мяу-мяу"

    def get_info(self, nickname, age):
        """Метод получения сведений экземпляра Cat"""
        return self.nickname, self.age

    @classmethod
    def voice(cls, sound = "Мяу-мяу") -> str:
        """Метод определения voice для Cat"""
        return cls.voice(sound)

class Dog(Animals):
    """Дочерний класс Animals"""
    def __init__(self, nickname: str, breed: str, age: int, sound: str, playing: bool):
        super().__init__(nickname, age, sound)
        self.breed = breed
        self.playing = playing

    def get_info(self,nickname, breed, age, playing):
        """Метод получения сведений экземпляра Dog"""
        return self.nickname, self.breed, self.age, self.playing

    def catch_ball(self, playing: bool) -> bool:
        """Метод получения значения playing"""
        self.playing = playing
        return self.playing

my_cat = Cat("Виски", 5, "Мяу-мяу")
my_cat.sound = "Мяу-мяу"
print(my_cat.sound)
