# Arquivo de exemplo da função MDTopAppBar.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = '''
MDScreen:
    md_bg_color: (1, 0.8, 0, 1)
    
    MDFloatLayout:
        id: float_layout
        
        MDTopAppBar:
            type: "small"
            size_hint_x: 0.95
            size_hint_y: 0.1
            pos_hint: {"center_x": 0.5, "center_y": 0.94}
    
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "menu"
                    on_release: app.add_card()
    
            MDTopAppBarTitle:
                text: "Arquivo de exemplo da função MDTopAppBar"
                font_style: "Title"
                role: "medium"
                font_size: 14
                pos_hint: {"center_x": 0.5}
    
            MDTopAppBarTrailingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "account-circle-outline"
                    theme_icon_color: 'Custom'
                    icon_color: (1, 0, 0, 1)
                
                MDActionTopAppBarButton:
                    icon: "attachment"
                    theme_bg_color: "Custom"
                    md_bg_color: (0, 1, 0, 1)
    
                MDActionTopAppBarButton:
                    icon: "calendar"
            
                MDActionTopAppBarButton:
                    icon: "dots-vertical"
'''

card_string = '''
MDCard:
    size_hint: 0.4, 0.6
    pos_hint: {"x": 0.028, "y": 0.287}
    radius: (0, 0, 0, 0)
    
    MDFloatLayout:
        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}

        MDLabel:
            text: 'Card'        
            adaptive_size: True
            color: "grey"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            bold: True
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

    def add_card(self):
        "Função que adiciona um card na tela."

        card = Builder.load_string(card_string)
        self.screen.ids.float_layout.add_widget(card)

MyApp().run()