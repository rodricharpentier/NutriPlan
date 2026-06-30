import wx

from interfaz.ventana_principal import VentanaPrincipal
from interfaz.splash import mostrar_splash


app = wx.App()

splash = mostrar_splash()
frame = VentanaPrincipal()
frame.Hide()

if splash is not None:
    wx.CallLater(2500, lambda: (frame.Show(), frame.Center(), splash.Destroy()))
else:
    frame.Show()

app.MainLoop()