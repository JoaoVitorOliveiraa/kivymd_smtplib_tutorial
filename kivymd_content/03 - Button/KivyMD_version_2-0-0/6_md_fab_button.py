# Arquivo de exemplo da função MDFabButton.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = """
MDScreen:
    MDFabButton:
        icon: "swap-vertical-bold"
        style: "large"
        theme_font_size: "Custom"
        font_size: "48sp"
        theme_bg_color: "Custom"
        md_bg_color: (1, 0, 0, 1)
        theme_icon_color: "Custom"
        icon_color: (1, 1, 0, 1)
        radius: [self.height / 2]
        size_hint: None, None
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""
        # size: "50dp", "50dp"      Teve que ser retirado para visualizar a mundança de tamanho do "large".

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()
