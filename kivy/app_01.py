import numpy as np

class Food(name, recipe, *ingredient):
    def __init__(self, name, recipe, ingredient):
        self.name = name
        self.recipe = recipe
        self.ingredient = ingredient
    