from abc import ABC, abstractmethod

class People(ABC):
    """Абстрактный класс определения списка людей"""

    @abstractmethod
    def set_human_list(self, human_list: list) -> list:
        """Интерфейс добавления людей в список"""
        while len(human_list) < 7:
            human_list.append(input())
            print(human_list)
        return human_list

class People_list(People):
    def set_human_list(self, human_list: list) -> list:
        while len(human_list) < 7:
            human_list.append(input())
            print(human_list)
        return human_list

humans = ["Петя", "Вася", "Ира"]

result = People_list()
print(result.set_human_list(humans))