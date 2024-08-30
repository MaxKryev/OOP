class Calculator:
    """Класс выполняет конкатенацию 2-х чисел"""
    # def __init__(self, a: int, b: int):
    #     self.a = a
    #     self.b = b

    def get_sum(self, a:int , b: int) -> int:
        return a.__add__(b)

class ConcatStr(Calculator):
    """Класс выполняет конкатенацию 2-х строк"""
    def get_sum(self, a:str , b: str) -> str:
        return a.__add__(b)

number_1 = Calculator()
number_2 = ConcatStr()
print(number_1.get_sum(80, 100))
print(number_2.get_sum("Мак", "сим"))