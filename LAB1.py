from abc import ABC, abstractmethod


class Furniture(ABC):
    def __init__(self, material: str, color: str, weight: float):
        """
        Инициализация объекта Furniture.

        :param material: Материал, из которого изготовлена мебель. Должен быть строкой.
        :param color: Цвет мебели. Должен быть строкой.
        :param weight: Вес мебели в килограммах. Должен быть положительным числом.
        :raises ValueError: Если weight <= 0.
        """
        if weight <= 0:
            raise ValueError("Вес мебели должен быть положительным числом.")

        self.material = material
        self.color = color
        self.weight = weight

    @abstractmethod
    def assemble(self) -> None:
        """Собрать мебель."""
        pass

    @abstractmethod
    def disassemble(self) -> None:
        """Разобрать мебель."""
        pass

    @abstractmethod
    def display_info(self) -> str:
        """Отобразить информацию о мебели."""
        pass


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация объекта Vehicle.

        :param brand: Марка автомобиля. Должен быть строкой.
        :param model: Модель автомобиля. Должен быть строкой.
        :param year: Год выпуска автомобиля. Должен быть положительным целым числом.
        :raises ValueError: Если year < 1886 (первый автомобиль был создан в 1886).
        """
        if year < 1886:
            raise ValueError("Год выпуска должен быть не менее 1886.")

        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """Запустить двигатель автомобиля."""
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        """Остановить двигатель автомобиля."""
        pass

    @abstractmethod
    def honk(self) -> str:
        """Подать сигнал."""
        pass


class ElectronicDevice(ABC):
    def __init__(self, brand: str, power: int, is_on: bool = False):
        """
        Инициализация объекта ElectronicDevice.

        :param brand: Бренд устройства. Должен быть строкой.
        :param power: Мощность устройства в ваттах. Должен быть положительным целым числом.
        :raises ValueError: Если power <= 0.
        """
        if power <= 0:
            raise ValueError("Мощность устройства должна быть положительным числом.")

        self.brand = brand
        self.power = power
        self.is_on = is_on

    @abstractmethod
    def turn_on(self) -> None:
        """Включить устройство."""
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """Выключить устройство."""
        pass

    @abstractmethod
    def get_power_usage(self) -> float:
        """Получить мощность устройства в ваттах."""
        pass


# Примеры подклассов для тестирования

class Chair(Furniture):
    def assemble(self) -> None:
        """Собрать стул."""
        pass

    def disassemble(self) -> None:
        """Разобрать стул."""
        pass

    def display_info(self) -> str:
        """Отобразить информацию о стуле."""
        return f"Стул из {self.material}, цвет: {self.color}, вес: {self.weight} кг."


class Car(Vehicle):
    def start_engine(self) -> None:
        """Запустить двигатель автомобиля."""
        pass

    def stop_engine(self) -> None:
        """Остановить двигатель автомобиля."""
        pass

    def honk(self) -> str:
        """Подать сигнал."""
        return "Бип-бип!"


class Laptop(ElectronicDevice):
    def turn_on(self) -> None:
        """Включить устройство."""
        self.is_on = True

    def turn_off(self) -> None:
        """Выключить устройство."""
        self.is_on = False

    def get_power_usage(self) -> float:
        """Получить мощность устройства в ваттах."""
        return self.power


if __name__ == "__main__":
    import doctest

    # Примеры использования классов
    chair = Chair("дерево", "коричневый", 5.0)
    car = Car("Toyota", "Corolla", 2020)
    laptop = Laptop("Dell", 65)

    print(chair.display_info())
    print(car.honk())

    # Проверка работоспособности
    doctest.testmod()
