# Arquivo de exemplo da função FitImage.

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
        md_bg_color: (1, 0.2, 0, 1)
        radius: (20, 20, 20, 20)

        FitImage:
            source: "../7 - List/Mel.jpg"
            size_hint_y: 0.8
            radius: (36, 36, 36, 36)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)
        return screen


MyApp().run()



#                              ----- Descrição da função FitImage -----

# No KivyMD, o widget FitImage é usado para exibir imagens que se ajustam dinamicamente ao tamanho do contêiner pai,
# mantendo sua proporção ou ocupando o espaço disponível.
# Ele é útil para criar layouts responsivos e para evitar distorções nas imagens.
# Parâmetros do FitImage:

# source: Caminho para a imagem que será exibida.
# Exemplo: "imagens/exemplo.png"

# size_hint_y: Controla o tamanho relativo da imagem em relação ao contêiner pai. no eixo y.
# Tipo: Tupla (largura, altura) com valores entre 0 e 1.

# radius: Define os cantos arredondados da imagem.
# Tipo: Lista ou Tupla [top_left, top_right, bottom_right, bottom_left] em pixels.

# pos_hint: Controla a posição relativa do layout dentro do pai.
# Tipo: Dicionário com chaves como {"center_x": 0.5, "center_y": 0.5}.