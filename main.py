from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Category:
    total_categories = 0
    unique_products = 0

    def __init__(self, title, description, products=None):
        self.title = title
        self.description = description
        self.products = products if products else []
        Category.total_categories += 1
        Category.unique_products += len(set(products))

    def __str__(self):
        return f"Категория: {self.title}, Описание: {self.description}"


class Smartphone(BaseProduct):
    def __init__(self, name, price, quantity, model, performance, memory, color):
        super().__init__(name, price, quantity)
        self.model = model
        self.performance = performance
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name} {self.model}, {self._price} руб. Остаток: {self.quantity} шт., " \
               f"Производительность: {self.performance}, Память: {self.memory}Гб, Цвет: {self.color}"

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self._price * self.quantity + other._price * other.quantity
        return NotImplemented


class LawnGrass(BaseProduct):
    def __init__(self, name, price, quantity, country, germination_period, color):
        super().__init__(name, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт., " \
               f"Страна-производитель: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self._price * self.quantity + other._price * other.quantity
        return NotImplemented
