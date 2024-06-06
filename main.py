class Category:
    """Класс для добавления категории"""
    title: str
    description: str
    _products: list

    total_categories = 0  # Общее количество категорий
    unique_products = 0  # Общее количество уникальных продуктов

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self._products = products
        Category.total_categories += 1
        for product in products:
            Category.unique_products += 1

    def add_product(self, product):
        """Метод для добавления продукта в список продуктов категории"""
        self._products.append(product)

    @property
    def products(self):
        """Геттер для приватного атрибута _products"""
        return [str(product) for product in self._products]



class Product:
    """Класс для добавления продуктов"""
    name: str
    _price: float
    quantity: int

    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно.")
        else:
            self._price = new_price

    @classmethod
    def create_product(cls, name, price, quantity=0):
        """Класс-метод для создания продукта"""
        return cls(name, price, quantity)

