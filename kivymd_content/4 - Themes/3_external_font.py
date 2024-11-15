# Arquivo de exemplo de implementação de uma fonte externa.

from kivy.core.text import LabelBase      # "LabelBase" permite registrar fontes personalizadas no Kivy.
from kivy.metrics import sp               # "sp" é uma unidade de medida para fontes baseada na densidade de pixels da tela.
from kivy.lang import Builder
from kivymd.app import MDApp


screen_string = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        text: "for_code"
        theme_text_color: "Custom"
        text_color: (97/255, 74/255, 211/255, 1)
        font_style: "lexend_regular"
        halign: "center"
        valign: "center"
'''


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        LabelBase.register(                         # Registra uma nova fonte no Kivy.
            name = "lexend_regular",                # Nome com o qual a fonte será referenciada no aplicativo.
            fn_regular = "Lexend-Regular.ttf")      # Especifica o arquivo da fonte, que deve estar no mesmo
                                                    # diretório do código ou no caminho correto.

        # Adiciona um estilo personalizado de fonte ao tema KivyMD, usando o nome "lexend_regular".
        self.theme_cls.font_styles["lexend_regular"] = {
            "large": {"line-height": 1.64, "font-name": "lexend_regular", "font-size": sp(57)},
            "medium": {"line-height": 1.52, "font-name": "lexend_regular", "font-size": sp(45)},
            "small": {"line-height": 1.44, "font-name": "lexend_regular", "font-size": sp(36)}}

        # "large", "medium", "small": Define tamanhos personalizados para a fonte, cada um com "line-height", "font-name" e "font-size".
        # "line-height": Altura da linha para o tamanho da fonte.
        # "font-name": Nome da fonte registrada(aqui, "lexend_regular").
        # "font-size": Tamanho da fonte, especificado em sp para manter a escala em diferentes densidades de tela.

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()