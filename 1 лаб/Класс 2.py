import doctest

class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        """
        Создание и подготовка к работе объекта "Время"

        :param hours: часы
        :param minutes: минуты
        :param seconds: секунды

        Примеры:
        >>> time = Time(20, 6, 56)  # инициализация экземпляра класса
        """
        if not isinstance(hours, int):
            raise TypeError("Часы должны быть типа int")
        if hours < 0:
            raise ValueError("Часы должны иметь положительное значение")
        if hours > 24:
            raise ValueError("Часы не должны иметь значение больше 24")
        self.hours = hours

        if not isinstance(minutes, int):
            raise TypeError("Минуты должны быть типа int")
        if minutes < 0:
            raise ValueError("Минуты должны иметь положительное значение")
        if hours > 24:
            raise ValueError("Минуты не должны иметь значение больше 60")
        self.minutes = minutes

        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть типа int")
        if seconds < 0:
            raise ValueError("Секунды должны иметь положительное значение")
        if hours > 24:
            raise ValueError("Секунды не должны иметь значение больше 60")
        self.seconds = seconds

    def add_hours(self, value: int):
        """
        Метод, который добавляет значение к часам
        :param value: значение, которое нужно добавить

        Примеры:
        >>> time = Time(13, 45, 50)
        >>> time.add_hours(2)
        """
        if not isinstance(value, int):
            raise TypeError("Добавляемое значение должно быть типа int")
        if value < 0:
            raise ValueError("Добавляемое значение должно быть положительным числом")
        if self.hours + value > 24:
            raise ValueError("Часы не должны быть больше 24")
        self.hours += value

    def remove_hours(self, value: int):
        """
        Метод, который убавляет значение от часов
        :param value: значение, которое нужно добавить

        Примеры:
        >>> time = Time(13, 45, 50)
        >>> time.remove_hours(3)
        """
        if not isinstance(value, int):
            raise TypeError("Убавляемое значение должно быть типа int")
        if value < 0:
            raise ValueError("Убавляемое значение должно быть положительным числом")
        if self.hours - value > 24:
            raise ValueError("Часы не должны быть больше 24")
        self.hours -= value


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
