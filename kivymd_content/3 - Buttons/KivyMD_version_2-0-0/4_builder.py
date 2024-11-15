# Arquivo de exemplo do módulo Builder.

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


# Importa automaticamente as funções utilizadas para o código.
# OBS: É necessária a utilização das tabulações para o reconhecimento da função Builder.
# OBS: É preciso trocar o operador de atribuição "=" por ":".
button_string = """
MDButton:
    style: "filled"
    height: 50
    width: 100
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDButtonText:
        text: "Aperte aqui"
        font_style: "Title"
        role: "large"
        font_size: 22
        theme_text_color: "Custom"
        text_color: (1, 0, 0, 1)

    MDButtonIcon:
        icon: "plus"
        theme_icon_color: "Custom"
        icon_color: (1, 1, 0, 1)
"""

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        screen = MDScreen()

        # Carrega e constrói o botão a partir da string "button_string".
        button = Builder.load_string(button_string)

        screen.add_widget(button)
        return screen

MyApp().run()


# screen_string = """
# MDScreen:
#     MDButton:
#         style: "filled"
#         height: 50
#         width: 100
#         pos_hint: {"center_x": 0.5, "center_y": 0.5}
#
#         MDButtonText:
#             text: "Aperte aqui"
#             font_style: "Title"
#             role: "large"
#             font_size: 22
#             theme_text_color: "Custom"
#             text_color: (1, 0, 0, 1)
#
#         MDButtonIcon:
#             icon: "plus"
#             theme_icon_color: "Custom"
#             icon_color: (1, 1, 0, 1)
# """
#
#
# class BatComputer(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         # Carrega e constrói a tela a partir da string "screen_string".
#         screen = Builder.load_string(screen_string)
#         return screen
#
# BatComputer().run()



#                       ----- Explicação do módulo Builder -----

# O Builder em Kivy é um módulo utilizado para carregar e analisar código de layout escrito na linguagem KV (Kivy Language).
# Ele permite que você defina a interface de usuário em um arquivo .kv ou como uma string, em vez de codificar a interface diretamente em Python.
# Isso facilita a separação entre lógica de aplicação e definição de interface, tornando o código mais organizado.

# É possível definir a interface diretamente em uma string usando Builder.load_string()

# Se a interface for mais complexa, é mais organizado defini-la em um arquivo ".kv". Você pode carregar um arquivo .kv usando Builder.load_file()

# Observação: O Kivy também tenta automaticamente carregar um arquivo.kv que tenha o mesmo nome da classe principal(sem o sufixo "App"),
# mas é uma boa prática carregar explicitamente com Builder para melhor controle.