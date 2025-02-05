from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_repr_mixin(capsys):
    Product("Сыр", "Сыр с плесенью", 100.50, 3)
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "Product(Сыр, Сыр с плесенью, 100.5, 3)"

    Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "Smartphone(Samsung, 256GB, 180000.0, 5)"

    LawnGrass("Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый")
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "LawnGrass(Газонная трава, Элитная, 500.0, 20)"
