"""
Defines the recipe rendering functionality
"""
import math


def render(recipe, flour_weight):
    """
    Replace percentages in a recipe with weights.
    """
    check_recipe(recipe)
    rendered = dict()
    if "levain" in recipe:
        levain = recipe["levain"]["recipe"]
        levain_weight = flour_weight * recipe["levain"]["percentage"] / 100
        rendered["levain"] = render(
            levain,
            flour_weight=levain_flour_weight(levain, total_weight=levain_weight),
        )
    ingredients = [name for name in recipe if name != "levain"]
    for ingredient in ingredients:
        rendered[ingredient] = dict()
        for name, percentage in recipe[ingredient].items():
            rendered[ingredient][name] = math.floor(flour_weight * percentage / 100)
            if "levain" in recipe and ingredient in rendered["levain"]:
                if name in rendered["levain"][ingredient]:
                    rendered[ingredient][name] -= rendered["levain"][ingredient][name]
    return rendered


def levain_flour_weight(recipe, total_weight):
    """
    Figure out the weight of flour in the levain from the total weight.
    """
    total_liquid = sum(recipe["liquid"][i] for i in recipe["liquid"])
    flour = total_weight / (1 + total_liquid / 100)
    return flour


def check_recipe(recipe):
    """
    Assert that a recipe conforms to the right style.
    """
    if "levain" in recipe:
        check_recipe(recipe["levain"]["recipe"])
