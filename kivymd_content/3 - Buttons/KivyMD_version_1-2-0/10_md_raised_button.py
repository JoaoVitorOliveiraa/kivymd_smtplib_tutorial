# Arquivo de exemplo da função MDRaisedButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        # Criação da tela.
        screen = Screen()
        texto = "João"
        raised_button = MDRaisedButton(text = texto,
                                    font_size = 50,
                                    theme_text_color = CUSTOM,
                                    text_color = ROXO_CLARO,
                                    line_color = PRETO,
                                    md_bg_color = AMARELO,
                                    size_hint = (0.8,0.2),
                                    elevation = 8,
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(raised_button)   # Adiciona o botão na tela.
        return  screen                     # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDRaisedButton -----

# O MDRaisedButton no KivyMD é um tipo de botão que se destaca na interface, apresentando uma elevação que o separa 
# visualmente do fundo. Esse estilo é baseado nas diretrizes do Material Design, onde botões elevados são usados 
# para indicar ações primárias e são frequentemente usados em formulários e interações que requerem destaque. 
# Os botões elevados são ideais para chamar a atenção do usuário e facilitar a interação.


# Aqui estão os principais parâmetros e propriedades do MDRaisedButton:

# text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Submit".

# font_size
# Descrição: Define o tamanho da fonte do texto do botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=18.

# theme_text_color
# Descrição: Define a cor do texto do botão de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom".
# Exemplo: theme_text_color="Primary".

# text_color
# Descrição: Define uma cor personalizada para o texto do botão, utilizada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[1, 1, 1, 1] (branco).

# md_bg_color
# Descrição: Define a cor de fundo do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: md_bg_color=[0.1, 0.6, 0.2, 1] (um tom de verde).

# on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Button pressed").

# disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False.
# Exemplo: disabled=True.

# pos_hint
# Descrição: Define a posição do botão na tela usando proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}.

# size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(0.3, 0.1).

# elevation
# Descrição: Define a elevação do botão, que afeta a aparência de sombra e a sensação de profundidade. O valor deve ser um inteiro.
# Tipo: int
# Padrão: 1
# Exemplo: elevation=8.


# Funcionalidade Geral:
# O MDRaisedButton é um botão de ação proeminente e visualmente atraente, ideal para ações primárias que os usuários precisam
# executar em um aplicativo. Sua elevação proporciona uma sensação de profundidade, tornando-o mais visível e fácil de
# interagir. Este componente é especialmente útil em formulários, interfaces de navegação e qualquer situação em que um
# destaque visual seja desejado.
