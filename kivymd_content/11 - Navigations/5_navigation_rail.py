# Arquivo de exemplo da função MDNavigationRail.
# Obs: No final do arquivo, há uma versão do código que não utiliza orientação a objetos.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.navigationrail import MDNavigationRailItem

screen_string = '''
# Componente personalizado que combina um ícone e um texto.
<CommonNavigationRailItem>

    # Define o ícone do item.
    MDNavigationRailItemIcon:
        icon: root.icon

    # Define o rótulo do item.
    MDNavigationRailItemLabel:
        text: root.text

# Define uma tela principal.
MDScreen:
    md_bg_color: self.theme_cls.secondaryContainerColor                         # Define a cor de fundo com o tema do app.

    # Cria a barra de navegação lateral.
    MDNavigationRail:
        type: "labeled"                                                         # Exibe o ícone e o texto nos itens.
        anchor: "top"                                                           # Fixa a barra no topo da tela.
        radius: 20                                                              # Arredonda as bordas.

        # Ícone de menu. Podem ser utilizados os mesmos parâmetros da função MDIconButton.
        MDNavigationRailMenuButton:
            icon: "menu"

        # Botão flutuante central. Podem ser utilizados os mesmos parâmetros da função MDFabButton.
        MDNavigationRailFabButton:
            icon: "home"

        CommonNavigationRailItem:
            icon: "folder-outline"
            text: "Files"

        CommonNavigationRailItem:
            icon: "bookmark-outline"
            text: "Bookmark"

        CommonNavigationRailItem:
            icon: "library-outline"
            text: "Library"
'''

# Classe que herda de MDNavigationRailItem para criar um componente reutilizável.
class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()          # Permite definir um texto dinâmico para o item.
    icon = StringProperty()          # Permite definir um ícone dinâmico.


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen


MyApp().run()

#                               ----- Exemplo de código que não utiliza orientação a objetos -----

# screen_string = '''
# <CommonNavigationRailItem>
#
#     MDNavigationRailItemIcon:
#         icon: root.icon
#
#     MDNavigationRailItemLabel:
#         text: root.text
#
# MDScreen:
#     md_bg_color: self.theme_cls.secondaryContainerColor
#
#     MDNavigationRail:
#         type: "labeled"
#         anchor: "top"
#         radius: 20
#
#         # Podem ser utilizados os mesmos parâmetros da função MDIconButton.
#         MDNavigationRailMenuButton:
#             icon: "menu"
#
#         # Podem ser utilizados os mesmos parâmetros da função MDFabButton.
#         MDNavigationRailFabButton:
#             icon: "home"
#
#         MDNavigationRailItem:
#             MDNavigationRailItemIcon:
#                 icon: "folder-outline"
#
#             MDNavigationRailItemLabel:
#                 text: "Files"
#
#         MDNavigationRailItem:
#             MDNavigationRailItemIcon:
#                 icon: "bookmark-outline"
#
#             MDNavigationRailItemLabel:
#                 text: "Bookmark"
#
#         MDNavigationRailItem:
#             MDNavigationRailItemIcon:
#                 icon: "library-outline"
#
#             MDNavigationRailItemLabel:
#                 text: "Library"
# '''
#
# class MyApp(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         self.screen = Builder.load_string(screen_string)
#         return self.screen
#
#
# MyApp().run()