import csv
from typing import Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str):
        self.dishes = set()
        self.ingredients = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str) -> None:
        with open(source_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                dish = self._get_dish(dish_name, dish_price)
                ingredient = self._get_ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _get_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish

    def _get_ingredient(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient

        ingredient = Ingredient(name)
        self.ingredients.add(ingredient)
        return ingredient
