class Animal:
    """Базовый класс для животных."""

    def __init__(self, name: str, age: int):
        """
        Инициализация животного.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Непубличный атрибут для инкапсуляции
        self._age = age  # Непубличный атрибут для инкапсуляции

    @property
    def name(self) -> str:
        """Возвращает имя животного."""
        return self._name

    @property
    def age(self) -> int:
        """Возвращает возраст животного."""
        return self._age

    def speak(self) -> str:
        """Издает звук животного. Этот метод будет перегружен в дочерних классах."""
        return "Животное издает звук."

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self.name} (возраст: {self.age} лет)"

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"

class Dog(Animal):
    """Класс для собак."""

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация собаки.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self._breed = breed  # Непубличный атрибут для инкапсуляции

    @property
    def breed(self) -> str:
        """Возвращает породу собаки."""
        return self._breed

    def speak(self) -> str:
        """Издает звук собаки. Перегружает метод базового класса."""
        return "Гав!"  # Собака лает

    def __str__(self) -> str:
        """Возвращает строковое представление собаки."""
        return f"{super().__str__()} (порода: {self.breed})"

    def __repr__(self) -> str:
        """Возвращает представление объекта собаки для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, breed={self.breed!r})"

class Cat(Animal):
    """Класс для кошек."""

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация кошки.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self._color = color  # Непубличный атрибут для инкапсуляции

    @property
    def color(self) -> str:
        """Возвращает цвет кошки."""
        return self._color

    def speak(self) -> str:
        """Издает звук кошки. Перегружает метод базового класса."""
        return "Мяу!"  # Кошка мяукает

    def __str__(self) -> str:
        """Возвращает строковое представление кошки."""
        return f"{super().__str__()} (цвет: {self.color})"

    def __repr__(self) -> str:
        """Возвращает представление объекта кошки для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, color={self.color!r})"

if __name__ == "__main__":
    # Создаем экземпляры классов
    my_dog = Dog("Бобик", 3, "Лабрадор")
    my_cat = Cat("Мурка", 2, "Черный")

    # Выводим информацию о животных
    print(my_dog)  # Выводит: Бобик (возраст: 3