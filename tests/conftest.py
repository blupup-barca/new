import pytest

from src.category import Category
from src.category_iter import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def first_product():
    return Product("Сыр", "Сыр с плесенью", 100.50, 3)


@pytest.fixture
def second_product():
    return Product("Молоко", "Молоко '3.2%", 60.50, 7)


@pytest.fixture
def for_category():
    return Category(
        name="Молочные продукты",
        description="Сыр с плесенью",
        products=[
            Product("Сыр 1", "Сыр с плесенью", 150.50, 5),
            Product("Сыр 2", "Сыр Российский", 100.99, 10),
        ],
    )


@pytest.fixture
def for_category_empty_product():
    return Category(name="Молочные продукты", description="Сыр с плесенью")


@pytest.fixture
def category_iterator(for_category):
    return CategoryIterator(for_category)


@pytest.fixture
def first_smartphone():
    return Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")


@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")


@pytest.fixture
def first_lawn_grass():
    return LawnGrass(
        "Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый"
    )


@pytest.fixture
def second_lawn_grass():
    return LawnGrass(
        "Газонная трава 2", "Выносливая", 450.0, 15, "США", "5 дней", "Темно-зеленый"
    )
