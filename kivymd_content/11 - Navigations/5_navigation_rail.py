# Arquivo de exemplo da função MDNavigationRail.
# Obs: No final do arquivo, há uma versão do código que não utiliza orientação a objetos.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.navigationrail import MDNavigationRailItem

screen_string = '''
# Componente personalizado que combina um ícone e um texto.
<CommonNavigationRailItem>
    on_active: print(root.text)
    on_enter: print(root.text)
    on_leave: print(root.text)
    
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
            on_release: print("Botão de Menu")

        # Botão flutuante central. Podem ser utilizados os mesmos parâmetros da função MDFabButton.
        MDNavigationRailFabButton:
            icon: "home"
            on_release: print("Botão de Home")

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



#                               ----- Descrição das funções -----

# MDNavigationRail
# A MDNavigationRail é um componente de navegação lateral que permite alternar entre diferentes telas ou seções do aplicativo.
# Ela é ideal para aplicativos com poucas opções de navegação e oferece um design compacto.
# Principais Parâmetros
# type:	#Define se a navegação exibe rótulos. Valores possíveis: "selected" (default), "unselected" e "labeled".
# anchor: Define o alinhamento da barra. Valores possíveis: "top", "bottom" e "center" (default).
# radius: Define o arredondamento das bordas da barra de navegação.

# MDNavigationRailMenuButton
# O MDNavigationRailMenuButton é um botão localizado no topo da barra de navegação lateral.
# Ele pode ser usado para abrir menus laterais ou ativar outras funções do aplicativo.
# Podem ser utilizados os mesmos parâmetros da função MDIconButton.

# MDNavigationRailFabButton
# O MDNavigationRailFabButton é um botão flutuante que pode ser usado para ações principais, como voltar à tela inicial.
# Podem ser utilizados os mesmos parâmetros da função MDFabButton.

# MDNavigationRailItem
# O MDNavigationRailItem representa um item dentro da barra de navegação. Ele pode conter um ícone e um texto.
# Principais Parâmetros
# active: Este parâmetro indica se o item está ativo ou não. Valores: True ou False
# radius: Define o raio das bordas arredondadas do item.
# on_active: Este evento é disparado quando o valor de active muda.
# on_enter: Disparado quando o mouse entra na área do item.
# on_leave: Disparado quando o mouse sai da área do item.
# add_widget: Adiciona um widget filho dentro do MDNavigationRailItem.

# MDNavigationRailItemIcon
# O MDNavigationRailItemIcon é o componente que exibe o ícone dentro de um MDNavigationRailItem.
# Podem ser utilizados os mesmos parâmetros da função MDIcon.

# MDNavigationRailItemLabel
# O MDNavigationRailItemLabel exibe o texto associado a um MDNavigationRailItem.
# Podem ser utilizados os mesmos parâmetros da função MDLabel.

# Resumo Final
# MDNavigationRail              Barra lateral de navegação.
# MDNavigationRailMenuButton	Botão no topo da barra para abrir menus.
# MDNavigationRailFabButton	    Botão flutuante para ações principais.
# MDNavigationRailItem	        Item dentro da barra lateral (ícone + texto).
# MDNavigationRailItemIcon	    Ícone de um item de navegação.
# MDNavigationRailItemLabel	    Texto de um item de navegação.



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