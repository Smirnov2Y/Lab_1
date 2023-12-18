import doctest

class PoolBowl:
    """
        Документация на класс.
        Класс описывает модель чаши бассейна.
        """
    def __init__(self, width: int, height: int, depth: int, occupied_volume: int):
        """
               Создание и подготовка к работе объекта "Чаша бассейна"

               :param width: Ширина бассейна в см
               :param height: Длина бассейна в см
               :param depth: Глубина бассейна в см
               :param occupied_volume: объём бассейна в см³

               Примеры:
               >>> bowl = PoolBowl(1000, 2500, 450, 10)  # инициализация экземпляра класса
               """
        if not isinstance((width, height, depth, occupied_volume), int):
            raise TypeError("Линейные размеры бассейна должны быть целыми числами")
        if width or height or depth or occupied_volume <= 0:
            raise ValueError("Линейные размеры бассейна должны быть положительным числом")
        self.width = width
        self.height = height
        self.height = depth
        self.occupied_volume = occupied_volume

    def is_empty_pool_bowl(self) -> bool:
        """
        Функция которая проверяет имеет ли является ли бассейн пустым

        :return: Является ли бассейн пустым

        Примеры:
        >>> bowl = PoolBowl(1000, 2500, 450, 10)
        >>> bowl.is_empty_pool_bowl()
        """

    def add_water_to_pool_bowl(self, water: float) -> None:
        """
        Добавление воды в бассейн.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бассейне, то вызываем ошибку

        Примеры:
        >>> bowl = PoolBowl(1000, 2500, 450, 10)
        >>> bowl.add_water_to_pool_bowl(200)
        """
        if not isinstance(water, int):
            raise TypeError("Добавляемая жидкость должна быть типа int")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")

class PoolPump:
    """
            Документация на класс.
            Класс описывает модель насоса бассейна.
            """
    def __init__(self, pump_power: float, pump_pressure: float):
        """
        Создание и подготовка к работе объекта "Насос бассейна"

        :param pump_power: мощность насоса в Вт
        :param pump_pressure: Создаваемое давление насосом в Па

        Примеры:
        >>> pump = PoolPump(220, 500)  # инициализация экземпляра класса
        """
        if not isinstance((pump_power, pump_pressure), (int, float)):
            raise TypeError("Мощность насоса и создаваемое им давление должены быть типа int или float")
        if pump_power or pump_pressure <= 0:
            raise ValueError("Мощность насоса и создаваемое им давление должены быть положительными числами")
        self.pump_power = pump_power
        self.pump_pressure = pump_pressure

    def is_pump_power(self) -> bool:
        """
        Функция которая проверяет есть ли у насоса мощность

        :return: Есть ли у насоса мощность

        Примеры:
        >>> pump = PoolPump(220, 500)
        >>> pump.is_pump_power()
        """

    def remove_pressure_from_pump(self, estimate_pressure: float) -> None:
        """
        Уменьшение давления в насосе.

        :param estimate_pressure: Уменьшение давления
        :raise ValueError: Если количество уменьшаемого давления превышает количество исходного,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> pump = PoolPump(220, 500)
        >>> pump.remove_pressure_from_pump(200)
        """
class PoolMassageShower:
    """
                Документация на класс.
                Класс описывает модель массажного душа бассейна.
                """

    def __init__(self, water_consumption: float, water_pressure: float):
        """
        Создание и подготовка к работе объекта "Массажный душ"

        :param water_consumption: Расход воды в массажном душе в м³/с
        :param water_pressure: Напор воды в массажном душе в H

        Примеры:
        >>> shower = PoolMassageShower(500, 120)  # инициализация экземпляра класса
        """
        if not isinstance((water_consumption, water_pressure), (int, float)):
            raise TypeError("Расход и напор воды должен быть типа int или float")
        if water_consumption or water_pressure <= 0:
            raise ValueError("Расход и напор воды должены быть положительным числами")
        self.water_consumption = water_consumption
        self.water_pressure = water_pressure

        def is_water_consumption_ok(self) -> bool:
            """
            Функция которая проверяет является ли расход воды соответсвующим нормам

            :return: Является ли расход воды соответсвующим нормам

            Примеры:
            >>> consumption = PoolMassageShower(500, 120)
            >>> consumption.is_water_consumption_ok()
            """

        def remove_water_pressure_from_shower(self, estimate_pressure: float) -> None:
            """
            Уменьшение напора в душе.

            :param estimate_water: Объем уменьшаемого напора
            :raise ValueError: Если количество уменьшаемого напора превышает количество напора в душе,
            то возвращается ошибка.

            :return: Объем реально уменьшенного давления

            Примеры:
            >>> pressure = PoolMassageShower(500, 120)
            >>> pressure.remove_water_pressure_from_shower(20)
            """



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
