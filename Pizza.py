class Pizza:
    def __init__(self,name,ingredients,prix,description,base):
        self.__name = name
        self.__ingredients = ingredients
        self.__prix = prix
        self.__description = description
        if(base=="tomate" or base=="crème"):
            self.__base = base
        else:
            raise ValueError("Le nom de la base n'est pas bon")

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

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self,d):
        self.__description = d

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self,b):
        if(b=="tomate"or b=="crème"):
            self.__base = b
        else:
            print("La base n'est pas valide")

