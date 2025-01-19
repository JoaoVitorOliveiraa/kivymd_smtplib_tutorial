# Arquivo de exemplo da função MDGridLayout.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDGridLayout:
        cols: 3 
        rows: 1 
        spacing: 10        
        padding: 20
        size_hint: (0.7, 0.7)
        radius: (20, 20, 20, 20)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDLabel:
            text: 'Text 1'
            font_style: 'Headline'
            theme_text_color: 'Custom'
            text_color: 'red'
            italic: True
        
        MDLabel:
            text: 'Text 2'
            font_style: 'Headline'
            theme_text_color: 'Custom'
            text_color: 'green'
            italic: True
        
        MDLabel:
            text: 'Text 3'
            font_style: 'Headline'
            theme_text_color: 'Custom'
            text_color: 'blue'
            italic: True
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)
        return screen


MyApp().run()



#                              ----- Descrição da função MDGridLayout -----

# O MDGridLayout é uma variação do GridLayout do Kivy, fornecendo suporte para designs estilizados e
# responsivos com a ajuda do KivyMD. Ele organiza widgets em uma grade com linhas e colunas, e pode
# ser configurado para ajustar dinamicamente seus itens ao tamanho da tela.
# Parâmetros Importantes:

# cols: Define o número de colunas na grade.
# rows: Define o número de linhas na grade (opcional se cols estiver definido).
# spacing: Espaçamento entre os widgets na grade.
# padding: Espaçamento interno ao redor da grade.
# size_hint: Ajusta o tamanho dos widgets em relação à tela.
# pos_hint: Define a posição relativa do widget dentro do layout pai.
# md_bg_color: Define a cor de fundo do layout.
# radius: Cria cantos arredondados no layout.