import wx
from modelos.dieta import Dieta
from modelos.dieta_celiaco import DietaCeliaco
from modelos.dieta_vegano import DietaVegano


class VentanaPrincipal(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='NutriPlan - Gestor de Dietas', size=(400, 300))
        self.inicializar_ui()
        self.Center()

    def inicializar_ui(self):
        panel = wx.Panel(self)
        sizer_principal = wx.BoxSizer(wx.VERTICAL)

        # Título
        titulo = wx.StaticText(panel, label="Planificador de Menús", style=wx.ALIGN_CENTER)
        font = titulo.GetFont()
        font.SetPointSize(14)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        titulo.SetFont(font)
        sizer_principal.Add(titulo, 0, wx.ALL | wx.EXPAND, 15)

        # Campo: Nombre
        sizer_nombre = wx.BoxSizer(wx.HORIZONTAL)
        lbl_nombre = wx.StaticText(panel, label="Nombre:", size=(80, -1))
        self.txt_nombre = wx.TextCtrl(panel)
        sizer_nombre.Add(lbl_nombre, 0, wx.ALIGN_CENTER_VERTICAL)
        sizer_nombre.Add(self.txt_nombre, 1, wx.EXPAND)
        sizer_principal.Add(sizer_nombre, 0, wx.ALL | wx.EXPAND, 10)

        # Campo: Edad
        sizer_edad = wx.BoxSizer(wx.HORIZONTAL)
        lbl_edad = wx.StaticText(panel, label="Edad:", size=(80, -1))
        self.txt_edad = wx.TextCtrl(panel)
        sizer_edad.Add(lbl_edad, 0, wx.ALIGN_CENTER_VERTICAL)
        sizer_edad.Add(self.txt_edad, 1, wx.EXPAND)
        sizer_principal.Add(sizer_edad, 0, wx.ALL | wx.EXPAND, 10)

        # Campo: Tipo de Dieta
        sizer_dieta = wx.BoxSizer(wx.HORIZONTAL)
        lbl_dieta = wx.StaticText(panel, label="Condición:", size=(80, -1))
        self.opciones_dieta = ["Normal", "Celíaco", "Vegano"]
        self.cmb_dieta = wx.ComboBox(panel, choices=self.opciones_dieta, style=wx.CB_READONLY)
        self.cmb_dieta.SetSelection(0) # "Normal" por defecto
        sizer_dieta.Add(lbl_dieta, 0, wx.ALIGN_CENTER_VERTICAL)
        sizer_dieta.Add(self.cmb_dieta, 1, wx.EXPAND)
        sizer_principal.Add(sizer_dieta, 0, wx.ALL | wx.EXPAND, 10)

        # Botón de Acción
        self.btn_generar = wx.Button(panel, label="Generar Plan Alimentario")
        self.btn_generar.Bind(wx.EVT_BUTTON, self.on_generar_plan)
        sizer_principal.Add(self.btn_generar, 0, wx.ALL | wx.CENTER, 15)

        panel.SetSizer(sizer_principal)

    def on_generar_plan(self, event):
        nombre = self.txt_nombre.GetValue().strip()
        edad_str = self.txt_edad.GetValue().strip()
        tipo_seleccionado = self.cmb_dieta.GetValue()

        # Validación básica con condicionales
        if not nombre or not edad_str:
            wx.MessageBox("Por favor, completa todos los campos.", "Error de validación", wx.OK | wx.ICON_WARNING)
            return

        if not edad_str.isdigit():
            wx.MessageBox("La edad debe ser un número válido.", "Error de validación", wx.OK | wx.ICON_WARNING)
            return

        edad = int(edad_str)

        # Condicionales para determinar qué clase instanciar (Polimorfismo en acción)
        if tipo_seleccionado == "Celíaco":
            usuario_dieta = DietaCeliaco(nombre, edad)
        elif tipo_seleccionado == "Vegano":
            usuario_dieta = DietaVegano(nombre, edad)
        else:
            usuario_dieta = Dieta(nombre, edad)

        # Mostrar el diálogo con el resultado
        self.mostrar_dialogo_resultado(usuario_dieta)

    def mostrar_dialogo_resultado(self, dieta_objeto):
        # Obtener el menú correspondiente según la instancia de la clase
        menu = dieta_objeto.obtener_menu()
        
        mensaje = (
            f"Plan Nutritional para: {dieta_objeto.nombre}\n"
            f"Edad: {dieta_objeto.edad} años\n"
            f"Perfil Seleccionado: {dieta_objeto.tipo}\n"
            f"--------------------------------------------------\n\n"
            f"🍳 DESAYUNO:\n   {menu['Desayuno']}\n\n"
            f"🍽️ ALMUERZO:\n   {menu['Almuerzo']}\n\n"
            f"🌙 CENA:\n   {menu['Cena']}\n"
        )

        # Usamos un mensaje de diálogo nativo para mostrar la salida de forma limpia
        wx.MessageBox(mensaje, "Tu Plan Diario Asignado", wx.OK | wx.ICON_INFORMATION)