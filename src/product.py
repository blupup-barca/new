class Product:
    """Класс для описания товаров. Также указаны цена и имеющееся в наличии количество"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
