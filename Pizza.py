class Pizza:
    def __init__(self,name,ingredients,prix):
        self.__name = name
        self.__ingredients = ingredients
        self.__prix = prix

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,n):
        self.__name = n

    @property
    def ingredients(self):
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self,i):
        self.__ingredients = i

    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self,p):
        self.__prix = p


