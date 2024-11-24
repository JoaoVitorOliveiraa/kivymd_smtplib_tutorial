# Arquivo de exemplo da função MDDialog.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import *
from kivymd.uix.button import MDButton, MDButtonText
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *


screen_string = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    
    MDButton:
        width: 30
        height: 80
        on_release: app.open_dialog()
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        MDButtonText:
            text: "Abrir Diálogo"
            font_style: "Title"
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_ROXO
        self.theme_cls.theme_style = TEMA_ESCURO

        screen = Builder.load_string(screen_string)
        return screen

    def open_dialog(self):
        "Função para abrir o campo Dialog."

        self.dialog = MDDialog(
            MDDialogIcon(
                icon = "language-python",
                icon_color = VERMELHO,
                halign= "left",
            ),

            MDDialogHeadlineText(
                text = "Descartar Rascunho?",
                font_style = DISPLAY_TEXT_STYLE,
                theme_text_color = CUSTOM,
                text_color = AMARELO,
                halign = "left"),                   # 'left', 'center', 'right', 'justify' ou 'auto'.

            MDDialogSupportingText(
                text = "Isso redefinirá seu dispositivo para as configurações padrão de fábrica.",
                font_style = HEADLINE_TEXT_STYLE,
                role = SMALL_TEXT_ROLE,
                font_size = SIZE_24,
                theme_text_color = CUSTOM,
                text_color = VERDE,
                halign = "center"),

            MDDialogButtonContainer(
                MDButton(MDButtonText(text = "Cancel", font_style = BODY_TEXT_STYLE),
                         height = 50,
                         width = 100,
                         on_release = lambda x: self.dialog.dismiss()),

                MDButton(MDButtonText(text = "Sim", font_style = BODY_TEXT_STYLE),
                         height = 50,
                         width = 100),
                spacing = "50px",               # Espaçamento entre os botões.
                orientation = "horizontal"      # Orientação dos botões. "vertical" ou "horizontal"
            )
        )
        self.dialog.open()


MyApp().run()





#             ----- Parâmetros da função MDDialogButtonContainer -----

# ['center', 'center_x', 'center_y', 'children', 'cls', 'disabled', 'height', 'id', 'ids', 'minimum_height',
# 'minimum_size', 'minimum_width', 'motion_filter', 'opacity', 'orientation', 'padding', 'parent', 'pos',
# 'pos_hint', 'right', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y',
# 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'spacing',
# 'top', 'width', 'x', 'y']
