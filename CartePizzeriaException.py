class CartePizzaException(Exception):
    """Exception levée lorsqu'un élément ne peut pas être supprimée de la carte."""
    def __init__(self, name):
        message="Erreur: Impossible de supprimer l'élément. Aucun élément '" + name + "' n'a été trouvé."
        super().__init__(message)