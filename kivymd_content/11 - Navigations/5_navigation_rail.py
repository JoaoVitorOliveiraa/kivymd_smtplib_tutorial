# Arquivo de exemplo da função MDNavigationRail.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.navigationrail import MDNavigationRailItem

screen_string = '''
<CommonNavigationRailItem>

    MDNavigationRailItemIcon:
        icon: root.icon

    MDNavigationRailItemLabel:
        text: root.text


MDBoxLayout:

    MDNavigationRail:
        type: "selected"

        MDNavigationRailMenuButton:
            icon: "menu"

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

    MDScreen:
        md_bg_color: self.theme_cls.secondaryContainerColor
'''


class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen


MyApp().run()