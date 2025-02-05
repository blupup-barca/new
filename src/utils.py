import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    category = []
    for product in data:
        products = []
        for product_list in product["products"]:
            products.append(Product(**product_list))
        product["products"] = products
        category.append(Category(**product))
    return category
