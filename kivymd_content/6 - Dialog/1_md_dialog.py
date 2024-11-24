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
    def __init__(self):
        super().__init__()
        self.dialog = None   # Define o atributo "self.dialog".

    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_ROXO
        self.theme_cls.theme_style = TEMA_ESCURO

        screen = Builder.load_string(screen_string)
        return screen

    def open_dialog(self):
        "Função para abrir o campo Dialog."

        self.dialog = MDDialog(

            # Define o ícone do diálogo. Semelhante à MDButtonIcon.
            MDDialogIcon(
                icon = "language-python",
                theme_icon_color = CUSTOM,
                icon_color = VERMELHO,
                halign= "left"),

            # Define o texto primário do diálogo. Semelhante à MDButtonText.
            MDDialogHeadlineText(
                text = "Descartar Rascunho?",
                font_style = DISPLAY_TEXT_STYLE,
                theme_text_color = CUSTOM,
                text_color = AMARELO,
                halign = "left"),                   # Ajuste horizontal. Opções: 'left', 'center', 'right', 'justify' ou 'auto'.

            # Define o texto secundário do diálogo. Semelhante à MDButtonText.
            MDDialogSupportingText(
                text = "Isso redefinirá seu dispositivo para as configurações padrão de fábrica.",
                font_style = HEADLINE_TEXT_STYLE,
                role = SMALL_TEXT_ROLE,
                font_size = SIZE_24,
                theme_text_color = CUSTOM,
                text_color = VERDE,
                halign = "center"),

            # Organiza/Armazena os botões no rodapé do diálogo, mantendo o alinhamento.
            MDDialogButtonContainer(

                # Declaração do primeiro botão, que fecha o diálogo.
                MDButton(MDButtonText(text = "Cancel", font_style = BODY_TEXT_STYLE),
                         height = 50,
                         width = 100,

                         # Ao ser pressionado, o diálogo é fechado com a função "dismiss()".
                         on_release = lambda x: self.dialog.dismiss()),

                # Declaração do segundo botão.
                MDButton(MDButtonText(text = "Sim", font_style = BODY_TEXT_STYLE),
                         height = 50,
                         width = 100),

                spacing = "50px",               # Define o espaçamento entre os botões (em pixels, neste caso).
                orientation = "horizontal"      # Define a orientação dos botões. Opções: "vertical" e "horizontal".
            )
        )

        # Abre o diálogo com a função "open()".
        self.dialog.open()


MyApp().run()



#                    ----- Descrição da função MDDialog -----

# O MDDialog no KivyMD é um componente de interface gráfica baseado no Material Design usado para exibir
# caixas de diálogo modais. Ele é amplamente utilizado para interagir com o usuário, exibir mensagens
# importantes ou coletar entradas simples, como texto ou botões de escolha.


#                           ----- Observação -----

# Além das funções MDDialogIcon, MDDialogHeadlineText, MDDialogSupportingText e MDDialogButtonContainer,
# também pode ser incluída a função MDDialogContentContainer na MDDialog.
# Esta função adiciona outros widgets (além de botões) no seu diálogo, como listas.


#             ----- Parâmetros da função MDDialogButtonContainer -----

# ['center', 'center_x', 'center_y', 'children', 'cls', 'disabled', 'height', 'id', 'ids', 'minimum_height',
# 'minimum_size', 'minimum_width', 'motion_filter', 'opacity', 'orientation', 'padding', 'parent', 'pos',
# 'pos_hint', 'right', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y',
# 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'spacing',
# 'top', 'width', 'x', 'y']

# Obs: O PyCharm exibiu esta lista após um erro de parâmetro.
