import doctest

class Radio:
    def __init__(self, volume: int, wave: float):
        """
        Создание и подготовка к работе объекта "Радио"

        :param volume: громкость
        :param wave: волна

        Примеры:
        >>> radio = Radio(5, 105.6)  # инициализация экземпляра класса
        """
        if not isinstance(volume, int):
            raise TypeError("Громкость должна быть типа int")
        if volume < 0:
            raise ValueError("Громкость должна иметь положительное значение")
        if volume > 10:
            raise ValueError("Громкость не должна иметь значение больше 10")
        self.volume = volume

        if not isinstance(wave, float):
            raise TypeError("Волна должна быть типа float")
        if wave < 0:
            raise ValueError("Волна должна иметь положительное значение")
        self.wave = wave


    def add_volume(self, value: int):
        """
        Метод, который увеличивает громкость
        :param value: значение, которое нужно добавить к громкости

        Примеры:
        >>> radio = Radio(6, 103.8)
        >>> radio.add_volume(1)
        """
        if not isinstance(value, int):
            raise TypeError("Добавляемое значение должно быть типа int")
        if value < 0:
            raise ValueError("Добавляемое значение должно быть положительным числом")
        if self.volume + value > 10:
            raise ValueError("Громкость не должна быть больше 10")
        self.volume += value


    def about_radio(self):

        """
        Метод, описывающий при какой громкости и какую волну пользователь сейчас слушает радио


        Примеры:
        >>> radio = Radio(10, 104.6)
        >>> radio.about_radio()
        На данный момент пользователь слушает 104.6 волну при громкости 10
        """

        print(f"На данный момент пользователь слушает {self.wave} волну при громкости {self.volume}")

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
