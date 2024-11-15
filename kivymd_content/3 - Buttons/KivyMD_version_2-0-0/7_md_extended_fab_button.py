# Arquivo de exemplo da função MDExtendedFabButton.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = """
MDScreen:
    MDExtendedFabButton:
        id: btn
        theme_bg_color: "Custom"
        md_bg_color: (1, 0, 0, 1)
        size_hint: None, None
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDExtendedFabButtonIcon:
            icon: "pencil-outline"
            theme_icon_color: "Custom"
            icon_color: (1, 1, 0, 1)

        MDExtendedFabButtonText:
            text: "Aperte"
"""
        # radius: [self.height / 2]     Arredonda o botão.

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()