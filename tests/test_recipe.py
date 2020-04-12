"""
Tests for the main recipe rendering.
"""
from padeiro import render


def test_render():
    "Render a basic recipe "
    recipe = {
        "flour": {"white": 70, "whole wheat": 30},
        "liquid": {"water": 63},
        "levain": {
            "percentage": 20,
            "recipe": {"flour": {"whole wheat": 100}, "liquid": {"water": 100}},
        },
        "extra": {"salt": 2},
    }
    result = render(recipe, flour_weight=1000)
    # 100g of whole wheat and 100g of water is in the levain
    expected = {
        "flour": {"white": 700, "whole wheat": 200},
        "liquid": {"water": 530},
        "levain": {"flour": {"whole wheat": 100}, "liquid": {"water": 100}},
        "extra": {"salt": 20},
    }
    assert result == expected
