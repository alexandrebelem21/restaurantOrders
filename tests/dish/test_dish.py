from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction

# Req 2


def test_dish():
    # 2.1
    dish = Dish("Lasanha", 29.99)
    assert isinstance(dish, Dish)
    name = "Lasanha"
    assert dish.name == name

    # 2.2
    # 2.3
    dish2 = Dish("Lasanha", 29.99)
    dish3 = Dish("Macarrão", 15.99)
    assert dish == dish2
    assert dish != dish3
    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    # 2.4
    # 2.5
    assert dish == dish2
    assert dish != dish3

    # 2.6
    assert repr(dish) == "Dish('Lasanha', R$29.99)"

    # 2.7
    with pytest.raises(TypeError):
        Dish("Lasanha", "29.99")

    # 2.8
    with pytest.raises(ValueError):
        Dish("Lasanha", -10.0)

    # 2.9
    ingredient = Ingredient("queijo mussarela")
    assert str(ingredient) not in map(str, dish.get_ingredients())

    # 2.10
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("farinha")
    dish.add_ingredient_dependency(ingredient1, 200)
    dish.add_ingredient_dependency(ingredient2, 300)
    expected_restrictions = {Restriction.GLUTEN, Restriction.LACTOSE,
                             Restriction.ANIMAL_DERIVED}
    obtained_restrictions = dish.get_restrictions()
    assert obtained_restrictions == expected_restrictions

    # 2.11
    expected_ingredients = {ingredient1, ingredient2}
    obtained_ingredients = dish.get_ingredients()
    assert obtained_ingredients == expected_ingredients

    # 2.12
    assert isinstance(dish.recipe, dict)
