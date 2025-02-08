# Arquivo de exemplo da função MDNavigationRail.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.navigationrail import MDNavigationRailItem
#
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
#         CommonNavigationRailItem:
#             icon: "folder-outline"
#             text: "Files"
#
#         CommonNavigationRailItem:
#             icon: "bookmark-outline"
#             text: "Bookmark"
#
#         CommonNavigationRailItem:
#             icon: "library-outline"
#             text: "Library"
# '''
#
#
# class CommonNavigationRailItem(MDNavigationRailItem):
#     text = StringProperty()
#     icon = StringProperty()
#
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

#                               ----- Exemplo de código que não utiliza orientação a objetos -----

screen_string = '''
<CommonNavigationRailItem>

    MDNavigationRailItemIcon:
        icon: root.icon

    MDNavigationRailItemLabel:
        text: root.text

MDScreen:
    md_bg_color: self.theme_cls.secondaryContainerColor

    MDNavigationRail:
        type: "labeled"
        anchor: "top"
        radius: 20

        # Podem ser utilizados os mesmos parâmetros da função MDIconButton.
        MDNavigationRailMenuButton:
            icon: "menu"

        # Podem ser utilizados os mesmos parâmetros da função MDFabButton.
        MDNavigationRailFabButton:          
            icon: "home"

        MDNavigationRailItem:
            MDNavigationRailItemIcon:
                icon: "folder-outline"
            
            MDNavigationRailItemLabel:
                text: "Files"

        MDNavigationRailItem:
            MDNavigationRailItemIcon:
                icon: "bookmark-outline"
            
            MDNavigationRailItemLabel:
                text: "Bookmark"
                
        MDNavigationRailItem:
            MDNavigationRailItemIcon:
                icon: "library-outline"
            
            MDNavigationRailItemLabel:
                text: "Library"    
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen


MyApp().run()