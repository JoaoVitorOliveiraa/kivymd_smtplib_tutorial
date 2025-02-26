# Arquivo de exemplo da função MDTabsSecondary.

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import (
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsBadge, MDTabsItemSecondary,
)

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTabsSecondary:
        id: tabs
        pos_hint: {"center_x": .5, "center_y": .5}

        MDDivider:
'''


class Example(MDApp):
    def on_start(self):
        for tab_icon, tab_name in {
            "airplane": "Flights",
            "treasure-chest": "Trips",
            "compass-outline": "Explore",
        }.items():
            if tab_icon == "treasure-chest":
                self.root.ids.tabs.add_widget(
                    MDTabsItemSecondary(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                        MDTabsBadge(
                            text="5",
                        ),
                    )
                )
            else:
                self.root.ids.tabs.add_widget(
                    MDTabsItemSecondary(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
        self.root.ids.tabs.switch_tab(icon="airplane")

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)


Example().run()