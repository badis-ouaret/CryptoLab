# Ce gestionnaire centralise l'accès aux fenêtres de type "clé"
# Il empêche qu'une nouvelle fenêtre soit créée si une autre est déjà ouverte

class KeyFrameManager:
    _active_instance = None

    @classmethod
    def set_active(cls, instance):
        if cls._active_instance is not None:
            cls._active_instance.bring_to_front()
            return False  # Refuse une nouvelle instance
        cls._active_instance = instance
        return True  # Autorise l'ouverture

    @classmethod
    def clear(cls):
        cls._active_instance = None

    @classmethod
    def bring_current_to_front(cls):
        if cls._active_instance is not None:
            cls._active_instance.bring_to_front()
