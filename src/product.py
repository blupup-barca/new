from src.base_classes import BaseProduct
from src.mixin import ReprMixin


class Product(BaseProduct, ReprMixin):

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, dict_product, products=None):
        if products:
            for product in products:
                if product.name == dict_product["name"]:
                    product.quantity += dict_product["quantity"]
                    product.price = max([product.price, dict_product["price"]])
                    return product
        return cls(
            dict_product["name"],
            dict_product["description"],
            dict_product["price"],
            dict_product["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if price < self.__price:
            check_input = input("Изменять цену? Введите y если да,и n если нет.\n")
            if check_input != "y":
                return
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError
