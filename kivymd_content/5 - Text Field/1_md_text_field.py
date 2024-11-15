# Arquivo de exemplo da função MDTextField.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDTextField:
        mode: "filled"
        size_hint_x: 0.8
        font_style: "Headline"
        role: "medium"
        theme_text_color: "Custom"
        text_color_normal: "yellow"
        text_color_focus: "green"
        fill_color_normal: (0, 1, 0, 1)
        fill_color_focus: (1, 1, 0, 1)
        theme_line_color: "Custom"
        line_color_normal: "purple"
        line_color_focus: "blue"
        radius: [self.height / 2]
        required: True
        max_height: "50dp"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDTextFieldLeadingIcon:
            icon: "phone"
            theme_icon_color: "Custom"
            icon_color_normal: "lightgreen"
            icon_color_focus: (97/255, 74/255, 211/255, 1)

        MDTextFieldHintText:
            text: "Outlined"
            text_color_normal: "yellow"

        MDTextFieldHelperText:
            text: "Helper text"
            text_color_focus: "blue"
            mode: "persistent"

        MDTextFieldTrailingIcon:
            icon: "information"
            theme_icon_color: "Custom"
            icon_color_normal: "yellow"
            icon_color_focus: (97/255, 74/255, 211/255, 1)

        MDTextFieldMaxLengthText:
            max_text_length: 15
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_ROXO
        self.theme_cls.theme_style = TEMA_ESCURO

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()


#                       ----- Explicação da função MDTextField -----

# O MDTextField no KivyMD é um widget de entrada de texto que segue o estilo do Material Design, oferecendo uma interface
# estilizada para campos de texto. Ele inclui efeitos de animação, como uma linha de foco que aparece ao interagir
# com o campo, além de suporte para validação, texto auxiliar e ícones integrados.

# Aqui estão os principais parâmetros que podem ser usados com MDTextField:

# mode: "filled": Define o estilo do campo de texto como preenchido.
# size_hint_x: 0.8: O campo ocupará 80% da largura disponível do container pai.
# font_style: "Headline": Aplica o estilo de fonte como "Headline".
# role: "medium": Define o papel de importância do texto.
# theme_text_color: "Custom": Permite definir uma cor personalizada para o texto.
# text_color_normal: "yellow": Cor do texto quando o campo não está focado.
# text_color_focus: "green": Cor do texto quando o campo está focado.
# fill_color_normal: (0, 1, 0, 1): Cor de preenchimento (fundo) quando o campo não está focado. Usa valores RGBA.
# fill_color_focus: (1, 1, 0, 1): Cor de preenchimento quando o campo está focado.
# theme_line_color: "Custom": Permite definir uma cor personalizada para a linha subjacente do campo.
# line_color_normal: "purple": Cor da linha quando o campo não está focado.
# line_color_focus: "blue": Cor da linha quando o campo está focado.
# radius: [self.height / 2]: Define os cantos arredondados com um raio baseado na altura do campo.
# required: True: O campo é obrigatório, e deve mostrar um alerta se deixado vazio.
# multiline: True: Permite que o campo aceite múltiplas linhas de texto.
# max_height: "50dp" e max_height: "200dp": Define a altura máxima do campo.
# pos_hint: {"center_x": 0.5, "center_y": 0.5}: Posiciona o campo no centro da tela.

# validator: O parâmetro validator define uma função de validação predefinida para a entrada de texto no campo.
# Ele pode ser usado para garantir que os dados digitados pelo usuário estejam em um formato específico.
# Opções:
# "email": Valida se o texto inserido é um endereço de e-mail válido.
# "time": Valida se o texto inserido está em um formato de hora válido.
# "date": Valida se o texto inserido está em um formato de data válido.

# date_format: Este parâmetro é usado quando o validator está definido como "date".
# Ele especifica o formato de data esperado para a validação. Isso garante que o usuário insira a data em um padrão específico.
# Exemplo de formato:
# "dd/mm/yyyy": O campo espera uma data no formato dia/mês/ano, como 15/08/2023.
# "mm/dd/yyyy": O campo espera uma data no formato mês/dia/ano, como 08/15/2023.


# Aqui estão os principais parâmetros que podem ser usados com MDTextFieldLeadingIcon:

# icon: "phone": Define um ícone de telefone antes do campo de texto.
# theme_icon_color: "Custom": Permite a personalização da cor do ícone.
# icon_color_normal: "lightgreen": Cor do ícone quando o campo não está focado.
# icon_color_focus: (97/255, 74/255, 211/255, 1): Cor do ícone quando o campo está focado.


# Aqui estão os principais parâmetros que podem ser usados com MDTextFieldHintText:

# text: "Outlined": Texto de dica que aparece quando o campo está vazio.
# text_color_normal: "yellow": Cor do texto de dica quando o campo não está focado.


# Aqui estão os principais parâmetros que podem ser usados com MDTextFieldHelperText:

# text: "Helper text": Texto auxiliar exibido abaixo do campo.
# text_color_focus: "blue": Cor do texto auxiliar quando o campo está focado.
# mode: "persistent": O texto auxiliar permanece visível o tempo inteiro.


# Aqui estão os principais parâmetros que podem ser usados com MDTextFieldTrailingIcon:

# icon: "information": Define um ícone de informação após o campo de texto.
# theme_icon_color: "Custom": Permite a personalização da cor do ícone.
# icon_color_normal: "yellow": Cor do ícone quando o campo não está focado.
# icon_color_focus: (97/255, 74/255, 211/255, 1): Cor do ícone quando o campo está focado.


# Aqui estão os principais parâmetros que podem ser usados com MDTextFieldMaxLengthText:

# max_text_length: 15: Define o limite máximo de caracteres permitidos no campo.