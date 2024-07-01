import pytest
from main import Category, Product, Smartphone, LawnGrass

@pytest.fixture
def sample_product():
    return Product("Наушники", 9999, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Категория электронных товаров", [sample_product])


@pytest.fixture
def smartphone():
    return Smartphone("Тестовый смартфон", 30000.0, 3, 100, "ModelX", 64, "Черный")


@pytest.fixture
def lawngrass():
    return LawnGrass("Тестовая трава", 500.0, 20,"Россия", "7 дней", "Зеленый")

def test_total_categories(sample_category):
    assert Category.total_categories == 1


def test_unique_products():
    assert Category.unique_products == 1


def test_category_init(sample_category):
    assert sample_category.title == "Электроника"
    assert sample_category.description == "Категория электронных товаров"
    assert sample_category.products[0] == "Наушники, 9999 руб. Остаток: 10 шт."


def test_product_init(sample_product):
    assert sample_product.name == "Наушники"
    assert sample_product.price == 9999
    assert sample_product.quantity == 10


def test_count_products(sample_category):
    assert len(sample_category.products) == 1


def test_price_setter(sample_product):
    sample_product.price = -1000
    assert sample_product.price == 9999


def test_product_str_method(sample_product):
    """Тестирование строкового представления продукта"""
    expected_str = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    assert str(sample_product) == expected_str

def test_product_addition(sample_product):
    other_product = Product("Чехол для наушников", 500, 3)
    total_value = sample_product + other_product
    expected_value = (sample_product.price * sample_product.quantity) + (other_product.price * other_product.quantity)
    assert total_value == expected_value, f"Ожидаемое значение: {expected_value}, полученное значение: {total_value}"


def test_smartphone_init(smartphone):
    assert smartphone.name == "Тестовый смартфон"
    assert smartphone.price == 30000.0
    assert smartphone.quantity == 3
    assert smartphone.performance == 100
    assert smartphone.model == "ModelX"
    assert smartphone.memory == 64
    assert smartphone.color == "Черный"

def test_smartphone_str(smartphone):
    expected_str = "Тестовый смартфон ModelX, 30000.0 руб. Остаток: 3 шт., Производительность: 100, Память: 64Гб, Цвет: Черный"
    assert str(smartphone) == expected_str


def test_lawngrass_init(lawngrass):
    assert lawngrass.name == "Тестовая трава"
    assert lawngrass.price == 500.0
    assert lawngrass.quantity == 20
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "7 дней"
    assert lawngrass.color == "Зеленый"

def test_lawngrass_str(lawngrass):
    expected_str = "Тестовая трава, 500.0 руб. Остаток: 20 шт., Страна-производитель: Россия, Срок прорастания: 7 дней, Цвет: Зеленый"
    assert str(lawngrass) == expected_str


if __name__ == "__main__":
    pytest.main()
