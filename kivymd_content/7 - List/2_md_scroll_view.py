# Arquivo de exemplo da função MDScrollView.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, MDListItem, MDListItemHeadlineText
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *


# String da implementação da função MDScrollView.
scroll_view_string = '''
MDScrollView:
    do_scroll_x: False
    md_bg_color: (1, 0, 0, 0.2)
    size_hint_x: 0.5
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO
        screen = MDScreen(md_bg_color = self.theme_cls.backgroundColor)

        # Criação do contêiner da barra de rolar.
        scroll_view = Builder.load_string(scroll_view_string)

        # Crição de uma lista e adição de 40 itens nela.
        list_itens = MDList()
        for i in range(40):
            item = MDListItem(MDListItemHeadlineText(text = "Utilização da função MDScrollView"))
            list_itens.add_widget(item)

        # Adição da lista no contêiner da barra.
        scroll_view.add_widget(list_itens)

        # Adição do contêiner da barra na tela.
        screen.add_widget(scroll_view)
        return screen


MyApp().run()



#                                           ----- Descrição -----

# MDScrollView
# Descrição: Um widget de rolagem da biblioteca KivyMD que permite visualizar conteúdo que
# excede o tamanho disponível na tela, especialmente útil para listas ou layouts extensos.

# Propriedades importantes personalizadas neste exemplo:

# do_scroll_x: False
# Função: Desabilita a rolagem horizontal. Apenas a rolagem vertical será permitida.
# Uso comum: Utilizado em cenários onde o conteúdo se expande verticalmente, como listas ou layouts empilhados.


# md_bg_color: (1, 0, 0, 0.2)
# Função: Define a cor de fundo do componente usando o padrão RGBA.
# Significado no exemplo:
# R (Vermelho): 1 (100%)
# G (Verde): 0 (0%)
# B (Azul): 0 (0%)
# A (Alpha): 0.2 (20% de opacidade)
# Resultado: Uma cor de fundo vermelha com transparência.

# size_hint_x: 0.5
# Função: Determina a largura proporcional do componente em relação ao widget pai (do scroll, neste caso).
# No exemplo: O componente ocupa 50% da largura do widget pai.

# pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# Função: Centraliza o componente no eixo X e no eixo Y dentro de seu widget pai (do scroll, neste caso).
# Valores detalhados:
# center_x: 0.5: Centraliza horizontalmente (50% da largura do pai).
# center_y: 0.5: Centraliza verticalmente (50% da altura do pai).