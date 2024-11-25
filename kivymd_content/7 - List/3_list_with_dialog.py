# Arquivo de exemplo de como usar uma lista com um diálogo.
# Obs: Este arquivo é uma atualização do "2_dialog_with_input".

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import *
from kivymd.uix.button import MDButton, MDButtonText
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = """
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDButton:
        style: "filled"
        height: 50
        width: 80
        on_release: app.open_dialog()
        pos_hint: {"center_x": 0.5, "center_y": 0.37}

        MDButtonText:
            text: "Confirmar"
            font_style: "Title"

        MDButtonIcon:
            icon: "check"
"""

textfield_string = """
MDTextField:
    mode: "outlined"
    size_hint_x: 0.6
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDTextFieldLeadingIcon:
        icon: "account"
        theme_icon_color: "Custom"
        icon_color_normal: (97/255, 74/255, 211/255, 1)

    MDTextFieldHintText:
        text: "Nome"

    MDTextFieldHelperText:
        text: "Insira seu nome"
        mode: "on_focus"

    MDTextFieldTrailingIcon:
        icon: "account-circle"
        theme_icon_color: "Custom"
        icon_color_normal: (97/255, 74/255, 211/255, 1)
"""

list_string = """
MDList:
    theme_bg_color: "Custom"
    md_bg_color: app.theme_cls.transparentColor
    
    MDListItem:
        MDListItemSupportingText:
            text: "user01@gmail.com"
            font_style: "Label"
                        
        MDListItemLeadingAvatar:
            source: "Mel.jpg"
            size_hint_y: 1
            radius: "36dp"
            
    MDListItem:
        MDListItemSupportingText:
            text: "user02@gmail.com"
            font_style: "Label"
                        
        MDListItemLeadingAvatar:
            source: "Mel.jpg"
            size_hint_y: 1
            radius: "36dp"
"""


class MyApp(MDApp):
    def __init__(self):
        super().__init__()
        self.dialog = None
        self.text_field = None
        self.list_items = None

    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AMARELO
        self.theme_cls.theme_style = TEMA_CLARO

        self.list_items = Builder.load_string(list_string)
        self.text_field = Builder.load_string(textfield_string)
        screen = Builder.load_string(screen_string)
        screen.add_widget(self.text_field)

        return screen

    def open_dialog(self):
        "Função para abrir o campo Dialog."

        if self.text_field.text == "":
            check_username = "Erro!\nPor favor, insira um nome."
            secondary_button = False
        else:
            check_username = self.text_field.text + " é o seu nome?"
            secondary_button = True

        self.dialog = MDDialog(

            MDDialogIcon(icon = "account-check"),

            MDDialogHeadlineText(text = "Checar Usuário", font_style = HEADLINE_TEXT_STYLE, halign = "left"),

            MDDialogSupportingText(text = check_username, font_style = TITLE_TEXT_STYLE, halign = "center"),

            MDDialogContentContainer(orientation="vertical"),

            MDDialogButtonContainer(

                MDButton(MDButtonText(text = "Fechar", font_style = BODY_TEXT_STYLE),
                         height = 50,
                         width = 100,
                         on_release = lambda x: self.dialog.dismiss()),

                spacing = "50px"),

            size_hint_x = 0.3,
            size_hint_y = 0.5
        )

        second_button = MDButton(MDButtonText(text="Sim", font_style=BODY_TEXT_STYLE),
                                 height=50,
                                 width=100,
                                 on_release=None)

        if secondary_button:
            self.dialog.add_widget(MDDialogButtonContainer(second_button))

        self.dialog.open()


MyApp().run()