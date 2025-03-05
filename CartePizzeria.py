import CartePizzeriaException

class CartePizzeria:
    def __init__(self):
        self.pizzas = []
        self.desserts = []
        self.drinks = []

    def is_empty(self):
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        return len(self.pizzas)

    def nb_desserts(self):
        return len(self.desserts)

    def nb_drinks(self):
        return len(self.drinks)
    
    def add(self, element):
        if isinstance(element, Boisson) :
            self.drinks.append(element)
        else if isinstance(element, Dessert) :
            self.desserts.append(element)
        else if isinstance(element, Pizza) :
            self.pizzas.append(element)
            
    def remove(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
            else :
                for drink in self.drinks:
                    if drink.name == name:
                        self.drinks.remove(drink)
                        return
                    else :
                        for dessert in self.desserts:
                            if dessert.name == name:
                                self.desserts.remove(dessert)
                                return
        raise CartePizzeriaException(name)
    
    
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(name)
