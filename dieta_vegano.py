from modelos.dieta import Dieta
class DietaVegano(Dieta):
    """Clase Hija que hereda de Dieta y excluye productos animales."""
    def __init__(self, nombre_usuario, edad):
        super().__init__(nombre_usuario, edad)
        self.tipo = "Vegano (100% Plant-based)"

    def obtener_menu(self):
        # Implementación basada en plantas
        return {
            "Desayuno": "Leche de almendras con avena, semillas de chía y rodajas de banana.",
            "Almuerzo": "Medallones de lentejas con ensalada completa de rúcula, tomate y palta.",
            "Cena": "Wok de tofu saltado con vegetales varios (morrón, cebolla, zuchini) y salsa de soja."
        }