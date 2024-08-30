class MeansOfTransport:
    """Класс определения свойств транспорта"""

    def __init__(self, __brand: str, __color: str):
        self.__brand = __brand
        self.__color = __color

    @property
    def show_color(self) -> str:
        """Геттер атрибута color"""
        return self.__color

    @show_color.setter
    def show_color(self, x: str):
        """Сеттер атрибута color"""
        self.__color = x

    @property
    def show_brand(self) -> str:
        """Геттер атрибута brand"""
        return self.__brand

    @show_brand.setter
    def show_brand(self, x: str):
        """Сеттер атрибута brand"""
        self.__brand = x


my_car = MeansOfTransport("Тойота", "Черный")
my_car.show_color = "Красный"
my_car.show_brand = "Ниссан"
print(my_car.show_color)
print(my_car.show_brand)


class Car(MeansOfTransport):
    """Класс определения свойств автомобиля"""

    car_drive = 4

    def __init__(self, brand: str, color: str, wheels: int):
        super().__init__(brand, color)
        self._wheels = wheels

    @classmethod
    def get_car_drive(cls) -> int:
        """Метод получения атрибута car_drive"""
        return Car.car_drive


class Moped(MeansOfTransport):
    """Класс определения свойств мопеда"""

    def __init__(self, brand: str, color: str, wheels: int):
        super().__init__(brand, color)
        self._wheels = wheels

    @staticmethod
    def get_time(distance: int, speed: int) -> float:
        """Метод определения времени преодоления дистанции"""
        return (distance / speed).__round__(2)


my_moped = Moped("Хонда", "красный", 2)
print(my_moped.get_time(500, 60))
my_car = Car("БМВ", "Белый", 4)
print(my_car.show_brand, my_car.show_color, Car.get_car_drive())
