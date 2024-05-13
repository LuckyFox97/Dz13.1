import pytest
from main import Category, Product


@pytest.fixture
def sample_product():
    return Product("Наушники", "Беспроводные наушники", 9999, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Категория электронных товаров", [sample_product])


def test_total_categories(sample_category):
    assert Category.total_categories == 1


def test_unique_products(sample_category, sample_product):
    assert sample_product.title in Category.unique_products


def test_category_init(sample_category):
    assert sample_category.title == "Электроника"
    assert sample_category.description == "Категория электронных товаров"
    assert sample_category.products[0].title == "Наушники"


def test_product_init(sample_product):
    assert sample_product.title == "Наушники"
    assert sample_product.description == "Беспроводные наушники"
    assert sample_product.price == 9999
    assert sample_product.quantity_in_stock == 10
