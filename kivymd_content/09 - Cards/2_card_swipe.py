# Arquivo de exemplo da função MDCardSwipe.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
# Este é um widget customizado baseado no MDCardSwipe.
<SwipeToDeleteItem>:
    size_hint_y: None       # Remove o redimensionamento automático da altura em relação ao pai.
    height: 50              # Define uma altura fixa para o cartão.
    anchor: "left"          # Define para qual lado o cartão pode ser deslizado. Valores: "left" e "right".
    type_swipe: "hand"      # Controla como o comportamento de deslizar o cartão é configurado. Valores: "hand" e "auto".

    # Parte oculta do cartão (visível ao deslizar).
    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            # Ao clicar, chama a função remove_item do aplicativo, passando a instância atual (root) como argumento.
            on_release: app.remove_item(root)

    # Parte visível do cartão.
    MDCardSwipeFrontBox:
        MDLabel:
            text: root.text     # Exibe o texto da propriedade root.text (fornecido dinamicamente).
            halign: "center"


# Definição da tela principal.
MDScreen:
    MDScrollView:
        MDBoxLayout:
            id: box                             # Define um identificador para referência no código Python.
            adaptive_height: True               # Garante que a altura do contêiner interno se ajuste automaticamente ao número de widgets adicionados.
            orientation: 'vertical'             # Organiza os widgets em uma pilha vertical.
            padding: 20                         # Define o preenchimento entre os itens.
            spacing: 20                         # Define o espaçamento entre os itens.
            md_bg_color: (0.3, 0.5, 0.7, 1)     # Define o fundo do layout.
'''

# Classe que herda de MDCardSwipe e adiciona uma propriedade dinâmica chamada text.
class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()    # Será usado para exibir informações específicas em cada cartão.

# Classe Principal.
class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        self.screen = Builder.load_string(screen_string)
        return self.screen

    # É chamado ao clicar no botão de "lixeira" em um cartão.
    def remove_item(self, instance):
        "Função que remove o widget passado (instance) do layout com id: box."

        self.screen.ids.box.remove_widget(instance)

    def on_start(self):
        "Função que é chamada automaticamente após o aplicativo iniciar."

        # Adiciona 20 instâncias do SwipeToDeleteItem ao contêiner box.
        # Cada instância recebe um texto dinâmico como argumento.
        for i in range(20):
            self.screen.ids.box.add_widget(SwipeToDeleteItem(text=f'Deslize para excluir o item {i+1}'))


MyApp().run()



#                               ----- VERSÃO QUE REMOVE O WIDGET APENAS COM A DESLIZADA DO CARD -----

# screen_string = '''
# # Este é um widget customizado baseado no MDCardSwipe.
# <SwipeToDeleteItem>:
#     size_hint_y: None       # Remove o redimensionamento automático da altura em relação ao pai.
#     height: 50              # Define uma altura fixa para o cartão.
#     anchor: "left"          # Define para qual lado o cartão pode ser deslizado. Valores: "left" e "right".
#     type_swipe: "auto"      # Controla como o comportamento de deslizar o cartão é configurado. Valores: "hand" e "auto".
#
#     # Evento que é disparado automaticamente quando o cartão é deslizado completamente para o lado definido pelo parâmetro anchor.
#     on_swipe_complete: app.on_swipe_complete(root)
#     # Quando o deslizamento do cartão termina, a função app.on_swipe_complete(instance) é chamada.
#     # O parâmetro root é a instância atual do SwipeToDeleteItem, ou seja, o cartão que foi deslizado.
#     # Assim, o cartão é automaticamente removido da lista de cartões, sem necessidade de pressionar o botão de lixeira.
#
#     # Parte oculta do cartão (visível ao deslizar).
#     MDCardSwipeLayerBox:
#         padding: "8dp"
#
#         MDIconButton:
#             icon: "trash-can"
#             pos_hint: {"center_y": .5}
#
#     # Parte visível do cartão.
#     MDCardSwipeFrontBox:
#         MDLabel:
#             text: root.text     # Exibe o texto da propriedade root.text (fornecido dinamicamente).
#             halign: "center"
#
#
# # Definição da tela principal.
# MDScreen:
#     MDScrollView:
#         MDBoxLayout:
#             id: box                             # Define um identificador para referência no código Python.
#             adaptive_height: True               # Garante que a altura do contêiner interno se ajuste automaticamente ao número de widgets adicionados.
#             orientation: 'vertical'             # Organiza os widgets em uma pilha vertical.
#             padding: 20                         # Define o preenchimento entre os itens.
#             spacing: 20                         # Define o espaçamento entre os itens.
#             md_bg_color: (0.3, 0.5, 0.7, 1)     # Define o fundo do layout.
# '''
#
# # Classe que herda de MDCardSwipe e adiciona uma propriedade dinâmica chamada text.
# class SwipeToDeleteItem(MDCardSwipe):
#     text = StringProperty()    # Será usado para exibir informações específicas em cada cartão.
#
# # Classe Principal.
# class MyApp(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         self.theme_cls.primary_palette = PALETA_AZUL
#         self.theme_cls.theme_style = TEMA_CLARO
#
#         self.screen = Builder.load_string(screen_string)
#         return self.screen
#
#     # É chamado ao se deslizar o cartão.
#     def on_swipe_complete(self, instance):
#         "Função que remove o widget deslizado (instance) do layout com o identificador box."
#
#         self.root.ids.box.remove_widget(instance)
#
#     def on_start(self):
#         "Função que é chamada automaticamente após o aplicativo iniciar."
#
#         # Adiciona 20 instâncias do SwipeToDeleteItem ao contêiner box.
#         # Cada instância recebe um texto dinâmico como argumento.
#         for i in range(20):
#             self.screen.ids.box.add_widget(SwipeToDeleteItem(text=f'Deslize para excluir o item {i+1}'))
#
#
# MyApp().run()



#                               ----- Descrição da função MDCardSwipe -----

# O MDCardSwipe é um widget do KivyMD que permite criar cartões deslizáveis (swipeable cards).
# Ele é utilizado para criar interações em que os usuários podem deslizar um cartão para revelar
# ações ocultas, como excluir um item ou realizar outras operações relacionadas ao cartão.

# Estrutura Básica
# Um MDCardSwipe é dividido em duas camadas principais:

# MDCardSwipeLayerBox:
# A camada oculta, visível somente ao deslizar o cartão.
# Contém widgets e ações (ex.: botões de exclusão).
# Geralmente tem um fundo destacado e elementos como ícones.

# MDCardSwipeFrontBox:
# A camada visível, exibida inicialmente ao usuário.
# Contém o conteúdo principal do cartão, como textos, ícones ou imagens.

# Propriedades Principais
# 1. Deslizamento (Swipe)
# anchor: Define a direção do deslizamento.
# Valores possíveis:
# "left" (padrão): Desliza para a esquerda.
# "right": Desliza para a direita.

# type_swipe: Define o comportamento do deslizamento.
# Valores possíveis:
# "hand" (padrão): O usuário deve deslizar manualmente.
# "auto": O cartão desliza automaticamente para o final se ultrapassar uma distância mínima.

# 2. Tamanho e Layout
# size_hint_y: Controla o redimensionamento vertical. Geralmente definido como None para altura fixa.
# height: Define a altura do cartão.

# 3. Personalização Visual
# Widgets como MDIconButton, MDLabel, etc., podem ser adicionados às camadas para personalizar ações e conteúdo.