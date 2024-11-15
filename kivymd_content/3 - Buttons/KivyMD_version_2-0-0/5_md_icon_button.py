# Arquivo de exemplo da função MDIconButton.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = """
MDScreen:
    MDIconButton:
        icon: "cookie"
        style: "standard"
        theme_font_size: "Custom"
        font_size: "48sp"
        theme_bg_color: "Custom"
        md_bg_color: (30/255, 22/255, 71/255, 1)
        theme_icon_color: "Custom"
        icon_color: (97/255, 74/255, 211/255, 1)
        radius: [self.height / 2]
        size_hint: None, None
        size: "50dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()



#                       ----- Explicação dos parâmetros da função MDIconButton -----

# icon: "cookie"
# Define o ícone exibido pelo botão. "cookie" é o nome do ícone de um cookie da biblioteca de ícones do Material Design.
# Você pode substituir "cookie" por qualquer outro nome de ícone suportado pelo KivyMD.

# style: "standard"
# Define o estilo visual do botão. No KivyMD, o MDIconButton possui alguns estilos, como "standard", "outlined", e "tonal".

# theme_font_size: "Custom"
# Permite definir um tamanho de fonte personalizado para o ícone. Quando theme_font_size está configurado como "Custom",
# o botão usará o valor definido em font_size.
# Se não fosse "Custom", o MDIconButton usaria tamanhos de fonte predefinidos, conforme o tema do Material Design.

# font_size: "48sp"
# Define o tamanho do ícone no botão como 48sp. O sp (Scale-independent Pixels) é uma unidade que considera a escala
# da fonte e é recomendada para tamanhos de texto e ícones.
# Este valor funciona em conjunto com theme_font_size: "Custom" para aplicar um tamanho de ícone personalizado.

# theme_bg_color: "Custom"
# Define a cor de fundo do botão como personalizada, permitindo usar a propriedade md_bg_color para definir uma cor específica.

# md_bg_color: (30/255, 22/255, 71/255, 1)
# Define a cor de fundo do botão. Os valores (30/255, 22/255, 71/255, 1) representam as componentes de cor em formato
# RGBA (Red, Green, Blue, Alpha), com cada valor variando entre 0 e 1.
# Também poderia receber uma string. Exemplo: "white".

# theme_icon_color: "Custom"
# Define a cor do ícone como personalizada, permitindo ajustar a cor específica usando a propriedade icon_color.

# icon_color: (97/255, 74/255, 211/255, 1)
# Define a cor do ícone. Os valores (30/255, 22/255, 71/255, 1) representam as componentes de cor em formato
# RGBA (Red, Green, Blue, Alpha), com cada valor variando entre 0 e 1.
# Também poderia receber uma string. Exemplo: "white".

# radius: [self.height / 2, ]
# Define os raios de arredondamento do botão. Aqui, o botão terá um raio de arredondamento de metade de sua
# altura (self.height / 2), o que o torna um círculo perfeito. O valor de radius é uma lista, onde cada valor
# representa um canto do botão. Com um valor único [self.height / 2], todos os cantos assumem o mesmo raio.

# size_hint: None, None
# Remove a escala automática do tamanho do botão, permitindo definir um tamanho fixo usando a propriedade size.
# Quando size_hint está definido como None, o botão não se ajusta automaticamente ao tamanho da tela ou layout
# e respeitará o valor definido em size.

# size: "84dp", "84dp"
# Define o tamanho absoluto do botão como 84dp tanto em largura quanto em altura. O dp (Density-independent Pixels) é
# uma unidade que se adapta a diferentes resoluções de tela.
# Com size_hint: None, None e size: "84dp", "84dp", o botão terá sempre o mesmo tamanho, independentemente do layout.
