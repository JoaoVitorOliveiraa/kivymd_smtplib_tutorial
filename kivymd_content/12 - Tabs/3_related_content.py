# Implementação das funções.

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsItem,
)

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTabsPrimary:
        id: tabs
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .6

        MDDivider:

        MDTabsCarousel:
            id: related_content_container
            size_hint_y: None
            height: dp(320)
'''


class Example(MDApp):
    def on_start(self):
        for tab_icon, tab_name in {
            "airplane": "Flights",
            "treasure-chest": "Trips",
            "compass-outline": "Explore",
        }.items():
            self.root.ids.tabs.add_widget(
                MDTabsItem(
                    MDTabsItemIcon(
                        icon=tab_icon,
                    ),
                    MDTabsItemText(
                        text=tab_name,
                    ),
                )
            )
            self.root.ids.related_content_container.add_widget(
                MDLabel(
                    text=tab_name,
                    halign="center",
                )
            )
            self.root.ids.tabs.switch_tab(icon="airplane")

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)


Example().run()
