from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    assert hash(Ingredient("queijo mussarela")) == hash(
        Ingredient("queijo mussarela"))
    assert hash(Ingredient("queijo mussarela")) != hash(Ingredient("presunto"))
    assert Ingredient("queijo mussarela") == Ingredient("queijo mussarela")
    assert Ingredient("queijo mussarela") != Ingredient("presunto")
    assert repr(Ingredient("cebola")) == "Ingredient('cebola')"
    assert Ingredient("cebola").name == "cebola"
    assert Ingredient("bacon").restrictions != {Restriction.GLUTEN}
    assert set(Ingredient("farinha").restrictions) == {Restriction.GLUTEN}
