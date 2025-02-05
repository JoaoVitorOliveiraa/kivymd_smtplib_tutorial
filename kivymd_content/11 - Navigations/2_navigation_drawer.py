# Arquivo de exemplo da função MDNavigationDrawer.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = '''
<DrawerItem>
    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon

    MDNavigationDrawerItemText:
        text: root.text

<DrawerLabel>
    padding: "18dp", 0, 0, "12dp"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        pos_hint: {"center_y": .5}

    MDNavigationDrawerLabel:
        text: root.text
        pos_hint: {"center_y": .5}
        padding: "6dp", 0, "16dp", 0
        theme_line_height: "Custom"
        line_height: 0

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDButton:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: nav_drawer.set_state("toggle")

                    MDButtonText:
                        text: "Open Drawer"

        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(16), dp(16), 0
            drawer_type: "modal"                # standard, modal
            anchor: "left"                      # left, right
            scrim_color: (1, 0.2, 0.8, 0.2)
            padding: 40
            background_color: (0.2, 1, 0.4, 1)
            theme_elevation_level: 'Custom'
            elevation_level: 5                 # 0 a 5

            MDNavigationDrawerMenu:
            
                MDNavigationDrawerHeader:
                    orientation: "vertical"
                    padding: 0, 0, 0, "12dp"
                    adaptive_height: True

                    MDLabel:
                        text: "Header title"
                        theme_text_color: "Custom"
                        theme_line_height: "Custom"
                        line_height: 0
                        text_color: "#4a4939"
                        adaptive_height: True
                        padding_x: "16dp"
                        font_style: "Display"
                        role: "small"

                    MDLabel:
                        text: "Header text"
                        padding_x: "18dp"
                        adaptive_height: True
                        font_style: "Title"
                        role: "large"

                MDNavigationDrawerLabel:
                    text: "Mail"

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account"

                    MDNavigationDrawerItemText:
                        text: "Inbox"

                    MDNavigationDrawerItemTrailingText:
                        text: "24"

                MDNavigationDrawerDivider:
                
                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "gmail"

                    MDNavigationDrawerItemText:
                        text: "Inbox"

                    MDNavigationDrawerItemTrailingText:
                        text: "+99"
                
                MDNavigationDrawerDivider:
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

MyApp().run()