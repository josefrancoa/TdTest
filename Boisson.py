class Boisson:
    def __init__(self,name,prix,alcool):
        self.__name = name
        self.__prix = prix
        self.__alcool = alcool

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,n):
        self.__name = n

    @property
    def alcool(self):
        return self.__alcool
    
    @alcool.setter
    def alcool(self,a):
        self.__alcool = a

    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self,p):
        self.__prix = p
