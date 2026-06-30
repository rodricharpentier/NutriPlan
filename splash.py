import os
import wx
import wx.adv


def mostrar_splash():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.abspath(os.path.join(carpeta_actual, "..", "assets", "logo.png"))

    if not os.path.exists(ruta_imagen):
        return None

    imagen = wx.Image(ruta_imagen)
    if not imagen.IsOk():
        return None

    bitmap = wx.Bitmap(imagen)
    splash = wx.adv.SplashScreen(
        bitmap,
        wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
        2500,
        None
    )
    wx.Yield()
    return splash