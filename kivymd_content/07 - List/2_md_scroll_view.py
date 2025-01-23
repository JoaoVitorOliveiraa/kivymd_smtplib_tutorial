# Arquivo de exemplo da função MDScrollView.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDListItem, MDListItemHeadlineText
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *


# String da implementação da função MDScrollView.
screen_string = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDScrollView:
        do_scroll_x: False
        md_bg_color: (1, 0, 0, 0.2)
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        MDList:
            id: list_container
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)

        # Crição de uma lista e adição de 40 itens nela.
        for i in range(40):
            item = MDListItem(MDListItemHeadlineText(text = "Utilização da função MDScrollView"))
            screen.ids.list_container.add_widget(item)

        return screen


MyApp().run()



#                              ----- Descrição da função MDScrollView -----

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


#                  ----- Descrição da expressão "screen.ids.list_container.add_widget(item)" -----

# id:
# Em Kivy (e KivyMD), id é uma identificação única atribuída a widgets em arquivos ou strings KV.
# Ele permite que você referencie widgets no código Python sem precisar de variáveis explícitas.
# Declarar um id associa um nome único ao widget dentro da hierarquia da interface.
# Aqui, o widget MDList recebe o identificador list_container, que pode ser usado para manipular o widget diretamente no Python.

# .ids:
# ".ids" é um dicionário especial que armazena todos os widgets associados a id no escopo do widget pai.
# Ele mapeia os nomes dos id para os objetos correspondentes.
# Você pode usar ".ids" para acessar qualquer widget definido com um id no KV.
# No Python, você pode acessar list_container (o MDList) usando self.root.ids.list_container

# Resumo:

# screen:
# É o widget MDScreen, carregado com o KV.

# screen.ids:
# É o dicionário que armazena todos os widgets que possuem um id no escopo do MDScreen.

# screen.ids.list_container:
# Acessa o widget MDList, permitindo que o código Python adicione itens a ele.

# Manipulação:
# Com screen.ids.list_container.add_widget(item), você adiciona dinamicamente widgets (neste caso, MDListItem) ao MDList.