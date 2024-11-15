# Arquivo de exemplo de Temas e Palhetas de Cores.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

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
                
        MDButtonIcon:
            icon: "plus"
"""


class MyApp(MDApp):

    # O self faz a "aplicação mobile" que estamos construindo.
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_ROXO             # Muda a cor do tema da "aplicação mobile".
        self.theme_cls.theme_style = TEMA_CLARO                  # Muda o estilo de tema (claro ou escuro).

        screen = Builder.load_string(screen_string)
        return  screen

MyApp().run()



#                       ----- Explicação da linha "self.theme_cls.primary_palette" -----

# A linha self.theme_cls.primary_palette = 'Purple' em KivyMD é usada para definir a cor primária do tema da aplicação.

# self.theme_cls:
# theme_cls é uma propriedade da classe MDApp, que gerencia o tema visual do aplicativo no KivyMD.
# Com theme_cls, é possível acessar e personalizar várias configurações do tema, como a cor primária (primary_palette),
# o tema (claro ou escuro), e a cor de destaque (accent_palette).

# primary_palette:
# primary_palette define a cor principal do tema do aplicativo. Essa cor é aplicada a vários elementos da interface que
# seguem o Material Design, como botões, barras de navegação, sliders e outros componentes.

# 'Purple':
# Aqui, a cor primária está sendo configurada como 'Purple' (roxo). Isso significa que todos os componentes da interface
# que usam a cor primária aparecerão em roxo, de acordo com as diretrizes do Material Design.



#                       ----- Explicação da linha "self.theme_cls.primary_hue" -----

#A propriedade self.theme_cls.primary_hue no KivyMD permite ajustar a tonalidade (hue) da cor primária definida no tema.
# Em outras palavras, ela ajusta a intensidade ou variação da cor escolhida como primary_palette. As tonalidades são um
# conjunto de valores pré-definidos que alteram a "luminosidade" ou "saturação" da cor, variando do mais claro ao mais escuro.

# No Material Design, cada cor da paleta possui várias tonalidades, e esses valores são organizados numericamente para indicar
# a intensidade da cor. As tonalidades disponíveis são normalmente: "50", "100", "200", "300", "400", "500", "600", "700", "800"
# , e "900", além de tonalidades de destaque como "A100", "A200", "A400", e "A700".

# Tons mais claros: Valores como "50", "100" etc.
# Tons mais escuros: Valores como "800", "900" etc.
# Tons de destaque (Accent): Os valores A100, A200, A400, A700 são mais vibrantes e são geralmente usados para cores de destaque.



#                       ----- Explicação da linha "self.theme_cls.theme_style" -----

# A propriedade self.theme_cls.theme_style no KivyMD permite alternar entre o tema claro e o tema escuro da aplicação,
# seguindo as diretrizes do Material Design. Isso altera automaticamente as cores de fundo e de texto para melhorar a
# legibilidade e estética em diferentes condições de iluminação.

# A propriedade theme_style aceita dois valores principais:
# "Light": Ativa o tema claro, que utiliza cores de fundo mais claras e cores de texto e elementos em tons mais escuros.
# "Dark": Ativa o tema escuro, que utiliza cores de fundo mais escuras e ajusta as cores de texto e elementos para tons mais claros,
# proporcionando um contraste melhor em ambientes com baixa luminosidade.


#                       ----- Explicação da linha "md_bg_color: self.theme_cls.backgroundColor" -----

# Define a cor de fundo da tela usando a cor de fundo do tema ativo do aplicativo.
# Essa cor será Dark (preto) ou Light (branco) dependendo do tema configurado.
