class CartePizzaException(Exception):
    """Exception levée lorsqu'une pizza ne peut pas être supprimée de la carte."""
    def __init__(self, name):
        message="Erreur: Impossible de supprimer la pizza. Aucune pizza '" + name + "' n'a été trouvé."
        super().__init__(message)