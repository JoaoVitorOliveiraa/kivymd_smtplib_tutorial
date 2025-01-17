# Arquivo de exemplo da função MDFloatLayout.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDFloatLayout:
        size_hint: (0.7, 0.7)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        md_bg_color: (0, 0, 0, 1)
        radius: (20, 20, 20, 20)
        
        MDButton:
            style: "filled"
            height: 50
            width: 100
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDButtonText:
                text: "Aperte aqui"
                font_style: "Title"
                role: "large"
                font_size: 22
                theme_text_color: "Custom"
                text_color: (1, 0, 0, 1)

            MDButtonIcon:
                icon: "plus"
                theme_icon_color: "Custom"
                icon_color: (1, 1, 0, 1)
        
        MDButton:
            style: "filled"
            height: 50
            width: 100
            pos_hint: {"x": 0.1, "y": 0.8}
        
            MDButtonText:
                text: "Aperte"
                font_style: "Title"
                role: "large"
                font_size: 22
                theme_text_color: "Custom"
                text_color: (0, 1, 0, 1)
        
            MDButtonIcon:
                icon: "plus"
                theme_icon_color: "Custom"
                icon_color: (1, 0, 0, 1)
                
        MDButton:
            style: "filled"
            height: 50
            width: 100
            pos_hint: {"center_x": 1, "center_y": 1}
        
            MDButtonText:
                text: "Pressione aqui"
                font_style: "Title"
                role: "large"
                font_size: 22
                theme_text_color: "Custom"
                text_color: (0, 0, 1, 1)
        
            MDButtonIcon:
                icon: "plus"
                theme_icon_color: "Custom"
                icon_color: (0, 1, 0, 1)
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)
        return screen


MyApp().run()



#                              ----- Descrição da função MDFloatLayout -----

# O MDFloatLayout é um layout do Kivy que posiciona os widgets com base em coordenadas absolutas ou proporcionais,
# oferecendo liberdade para organizar os elementos na tela.
# Ele é ideal para casos em que os widgets precisam de posições específicas.
# Parâmetros do MDFloatLayout:

# size_hint: Controla o tamanho relativo do widget em relação ao layout pai.
# Tipo: Tupla (largura, altura) com valores entre 0 e 1 (ou None para tamanho fixo).

# pos_hint: Define a posição relativa do widget dentro do layout pai.
# Tipo: Dicionário com chaves como:
# "center_x" e "center_y": Centralizam o widget proporcionalmente.
# "x" e "y": Definem a posição relativa em frações (de 0 a 1).

# md_bg_color: Define a cor de fundo do layout.
# Tipo: Lista [R, G, B, A], com valores de 0 a 1.

# radius: Cria cantos arredondados no layout.
# Tipo: Lista [top_left, top_right, bottom_right, bottom_left] (em pixels).

# size
# Define o tamanho absoluto do widget, ignorando size_hint.
# Tipo: Tupla (largura, altura) em pixels.

# pos
# Define a posição absoluta do widget no layout.
# Tipo: Tupla (x, y) em pixels, onde (0, 0) é o canto inferior esquerdo.