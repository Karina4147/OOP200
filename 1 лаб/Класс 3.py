import doctest

class Car:
    def __init__(self, color: str, model: str):

        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param color: цвет
        :param model: марка

        Примеры:
        >>> car = Car("blue", "BMV")  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        if not isinstance(model, str):
            raise TypeError("Марка должна быть типа str")
        self.model = model

    def starting_the_engine(self):
        """
        Метод, имитирующий запуск двигателя.

        Примеры:
        >>> car = Car("Rose", "Ford")
        >>> car.starting_the_engine()
        Rose автомобиль марки Ford завел двигатель

        """
        print(f"{self.color} автомобиль марки {self.model} завел двигатель")

    def speeding(self):
        """
        Метод, возвращающий информацию об автомобиле, который привысил скорость.

        Примеры:
        >>> car = Car("Black", "Ford")
        >>> car.speeding()
        Black автомобиль марки Ford превысил допустимую скорость
        """
        print(f'{self.color} автомобиль марки {self.model} превысил допустимую скорость')


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
