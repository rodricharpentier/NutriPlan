from modelos.dieta import Dieta

class DietaCeliaco(Dieta):
    """Clase Hija que hereda de Dieta y adapta las opciones SIN TACC."""
    def __init__(self, nombre_usuario, edad):
        # Llamada al constructor de la clase padre
        super().__init__(nombre_usuario, edad)
        self.tipo = "Celíaco (Sin TACC)"

    def obtener_menu(self):
        # Implementación estricta libre de gluten
        return {
            "Desayuno": "Café con leche y tostadas de pan de arroz con mermelada (Certificado Libre de Gluten).",
            "Almuerzo": "Bife de lomo con arroz primavera (Cuidado con la contaminación cruzada).",
            "Cena": "Tarta con masa de harina de maíz (polenta) rellena de verduras y queso."
        }
