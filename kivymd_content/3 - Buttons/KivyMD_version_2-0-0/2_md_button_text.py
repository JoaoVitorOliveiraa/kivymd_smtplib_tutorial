# Arquivo de exemplo da função MDButtonText.

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        # Criação da tela.
        screen = MDScreen()
        texto = "Aperte aqui"

        # Mesmo funcionamento da MDLabel.
        button = MDButton(MDButtonText(text = texto,
                                            font_style = DISPLAY_TEXT_STYLE,
                                            role = SMALL_TEXT_ROLE,
                                            font_size = SIZE_36,
                                            theme_text_color = CUSTOM,
                                            text_color = VERMELHO),
                            style = OUTLINED_BUTTON_STYLE,
                            height = 50,
                            width = 100,
                            pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(button)        # Adiciona o botão na tela.
        return  screen                   # Retorna a tela.


MyApp().run()