# Arquivo de exemplo de como usar um campo de texto com um botão.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *


screen_string = """
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    
    MDButton:
        style: "filled"
        height: 50
        width: 80
        on_release: app.show_text()
        pos_hint: {"center_x": 0.5, "center_y": 0.37}

        MDButtonText:
            text: "Aperte aqui"
            font_style: "Title"

        MDButtonIcon:
            icon: "walk"
"""

textfield_string = """
MDTextField:
    mode: "outlined"
    size_hint_x: 0.6
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    
    MDTextFieldLeadingIcon:
        icon: "tram"
        theme_icon_color: "Custom"
        icon_color_normal: (97/255, 74/255, 211/255, 1)
    
    MDTextFieldHintText:
        text: "Nome"
    
    MDTextFieldHelperText:
        text: "Insira seu nome"
        mode: "on_focus"
    
    MDTextFieldTrailingIcon:
        icon: "tray-arrow-down"
        theme_icon_color: "Custom"
        icon_color_normal: (97/255, 74/255, 211/255, 1)
"""

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AMARELO
        self.theme_cls.theme_style = TEMA_CLARO

        self.text_field = Builder.load_string(textfield_string)     # Transforma em um atributo da classe.
        screen = Builder.load_string(screen_string)
        screen.add_widget(self.text_field)

        return screen

    def show_text(self):
        "Função que mostra o texto inserido no campo."

        print(self.text_field.text)     # Impressão do atributo "text" da MDTextField.

MyApp().run()