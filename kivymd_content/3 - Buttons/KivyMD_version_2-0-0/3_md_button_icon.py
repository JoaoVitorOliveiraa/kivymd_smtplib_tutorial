# Arquivo de exemplo da função MDButtonIcon.

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        # Criação da tela.
        screen = MDScreen()
        texto = "Aperte aqui"

        # Funcionamento similar a MDIcon.
        button = MDButton(MDButtonText(text = texto,
                                            font_style = TITLE_TEXT_STYLE,
                                            role = LARGE_TEXT_ROLE,
                                            font_size = SIZE_22,
                                            theme_text_color = CUSTOM,
                                            text_color = VERMELHO),
                                MDButtonIcon(icon = "plus",
                                            theme_icon_color = CUSTOM,
                                            icon_color = AMARELO),
                                style = FILLED_BUTTON_STYLE,
                                height = 50,
                                width = 100,
                                pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(button)        # Adiciona o botão na tela.
        return  screen                   # Retorna a tela.


MyApp().run()