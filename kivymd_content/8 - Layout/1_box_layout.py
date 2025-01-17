# Arquivo de exemplo da função MDBoxLayout.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDBoxLayout:
        size_hint: (0.7, 0.5)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        orientation: 'horizontal'
        adaptive_size: False
        md_bg_color: (0, 0, 0, 1)
        radius: (20, 20, 20, 20)
        spacing: 5
        padding: 10
        
        MDButton:
            style: "filled"
            height: 50
            width: 100
            pos_hint: {"center_y": 0.5}
        
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
            pos_hint: {"center_y": 0.5}
        
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
            pos_hint: {"center_y": 0.5}
        
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



#                              ----- Descrição da função MDBoxLayout -----

# O MDBoxLayout é um layout do KivyMD usado para organizar widgets em uma linha ou coluna.
# Ele combina a funcionalidade do BoxLayout com estilos adicionais da biblioteca KivyMD.
# Abaixo estão os principais parâmetros e suas funções:

# orientation: Define a direção de organização dos widgets.
# Valores: "horizontal" (linha, padrão) ou "vertical" (coluna).

# spacing: Define o espaço entre os widgets.
# Tipo: int ou float (em pixels).

# padding: Define o espaço interno ao redor do layout.
# Pode ser um único valor (para todos os lados) ou uma tupla (esquerda, topo, direita, baixo).

# size_hint: Controla o tamanho relativo do layout ao contêiner pai.
# Tipo: Tupla (largura, altura) com valores entre 0 e 1 (ou None para tamanho fixo).

# pos_hint: Controla a posição relativa do layout dentro do pai.
# Tipo: Dicionário com chaves como {"center_x": 0.5, "center_y": 0.5}.

# adaptive_size: Ajusta automaticamente o tamanho do layout ao conteúdo.
# Valores: True ou False.

# md_bg_color: Define a cor de fundo do layout.
# Tipo: Lista [R, G, B, A], com valores de 0 a 1.

# radius: Cria cantos arredondados no layout.
# Tipo: Lista [top_left, top_right, bottom_right, bottom_left] (em pixels).