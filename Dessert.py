
class Dessert:
    def __init__(self, name, prix: float, fait_maison: bool):
        self.name = name
        self.prix = prix
        self.ingredients = []
        self.fait_maison = fait_maison

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_name(self):
        return self.name
    
    def get_prix(self):
        return self.prix
    
    def get_ingredients(self):
        return self.ingredients
    
    def is_fait_maison(self):
        return self.fait_maison
    
    def set_name(self, name):
        self.name = name

    def set_prix(self, prix):
        self.prix = prix
    
    def set_ingredients(self, ingredients):
        self.ingredients = ingredients
    
    def set_fait_maison(self, fait_maison):
        self.fait_maison = fait_maison
    