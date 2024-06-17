class Category:
    """Класс для добавления категории"""
    title: str
    description: str
    _products: list
    _total_products = 0  # Общее количество продуктов на складе

    total_categories = 0  # Общее количество категорий
    unique_products = 0  # Общее количество уникальных продуктов

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self._products = products
        Category.total_categories += 1
        for product in products:
            Category.unique_products += 1
            Category._total_products += product.quantity

    def add_product(self, product):
        """Метод для добавления продукта в список продуктов категории"""
        self._products.append(product)
        Category._total_products += product.quantity

    @property
    def products(self):
        """Геттер для приватного атрибута _products"""
        return [str(product) for product in self._products]

    def __len__(self):
        return Category._total_products

    def __str__(self):
        return f"{self.title}, количество продуктов: {len(self)} шт."


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

    def __add__(self, other):
        """
        Возвращает стоимость продукта, умноженную на количество.
        """
        return self.price * self.quantity + other.price * other.quantity

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
