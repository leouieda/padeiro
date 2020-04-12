"""
Tests for the main recipe rendering.
"""
from padeiro import render


def test_render():
    "Placeholder test"
    render(recipe={"title": "Basic Rye"}, flour_weight=1000)
