# Arquivo de exemplo de um código que muda o estilo de tema de fundo ao clicar um botão..

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        text: "Estilo de Tema Atual - {}".format(app.theme_cls.theme_style)
        font_style: "Display"
        role: "small"
        bold: True
        italic: True
        theme_text_color: "Custom"
        text_color: (97/255, 74/255, 211/255, 1)
        halign: "center"
        valign: "center"

    MDButton:
        on_release: app.trocar_tema()
        pos_hint: {"center_x": 0.5, "center_y": 0.4}

        MDButtonText:
            text: "Trocar Tema"
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.theme_style_switch_animation = True              # Animar cores de aplicativos ao alternar o
                                                                        # esquema de cores do app.
        self.theme_cls.theme_style_switch_animation_duration = 0.8      # Duração da animação de troca do esquema de cores do app.
        self.theme_cls.theme_style = TEMA_ESCURO
        self.theme_cls.primary_palette = PALETA_VERDE

        screen = Builder.load_string(screen_string)
        return screen

    def trocar_tema(self):
        "Função que troca o estilo de tema do app."

        self.theme_cls.primary_palette = (PALETA_VERDE if self.theme_cls.primary_palette == PALETA_LARANJA else PALETA_LARANJA)
        self.theme_cls.theme_style = (TEMA_ESCURO if self.theme_cls.theme_style == TEMA_CLARO else TEMA_CLARO)

        # Função que muda automaticamente o tema.
        # self.theme_cls.switch_theme()

MyApp().run()


#                       ----- Explicação da linha "on_release: app.trocar_tema()" -----

# Usar on_release: app.trocar_tema() é uma maneira de definir uma ação personalizada para um botão no KivyMD,
# que, ao ser pressionado, executará a função trocar_tema() no aplicativo.

# on_release:: Esse evento é disparado quando o botão é pressionado e liberado, o que torna essa linha ideal
# para chamar funções ou realizar ações após a interação com o botão.

# app.trocar_tema(): A palavra-chave "app" refere-se à instância atual do aplicativo principal (que herda de MDApp).
# Assim, ao usar app.trocar_tema(), estamos chamando o metodo trocar_tema() que está definido na classe principal do aplicativo.
