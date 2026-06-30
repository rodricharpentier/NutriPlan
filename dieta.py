class Dieta:
    """Clase Base para una dieta estándar."""
    def __init__(self, nombre_usuario, edad):
        self.nombre = nombre_usuario
        self.edad = edad
        self.tipo = "Normal"

    def obtener_menu(self):
        # Condicional básico basado en la edad para adaptar porciones si es necesario
        if self.edad < 18:
            porcion = "Porción Juvenil (Alta energía)"
        else:
            porcion = "Porción Adulto Estándar"
            
        return {
            "Desayuno": f"Infusión con tostadas de pan integral y queso crema ({porcion}).",
            "Almuerzo": "Pechuga de pollo a la plancha con puré de calabaza y ensalada.",
            "Cena": "Fideos tirabuzón con salsa tuco natural."
            }