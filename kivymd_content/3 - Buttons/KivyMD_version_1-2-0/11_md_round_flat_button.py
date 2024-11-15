# Arquivo de exemplo da função MDRoundFlatButton.
from tkinter.constants import UNDERLINE

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()    # Criação da tela.
        texto = "João"
        round_flat_button = MDRoundFlatButton(text = texto,
                                    #font_size = 50,
                                    font_style = H1,
                                    theme_text_color = CUSTOM,
                                    text_color = ROXO_CLARO,
                                    line_color = ROXO_ESCURO,
                                    md_bg_color = AMARELO,
                                    size_hint = (0.6, 0.4),
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(round_flat_button)   # Adiciona o botão na tela.
        return  screen                         # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDRoundFlatButton -----

# O MDRoundFlatButton no KivyMD é um botão que apresenta um design arredondado e um fundo plano, seguindo as diretrizes
# do Material Design. Esse tipo de botão é ideal para ações secundárias ou complementares, onde um visual mais discreto
# é desejado em comparação com botões elevados. O design arredondado torna o botão visualmente agradável e fácil de usar,
# especialmente em interfaces modernas.


# Aqui estão os principais parâmetros e propriedades do MDRoundFlatButton:

# text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Cancel".

# font_size
# Descrição: Define o tamanho da fonte do texto do botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=16.

# theme_text_color
# Descrição: Define a cor do texto do botão de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom".
# Exemplo: theme_text_color="Secondary".

# text_color
# Descrição: Define uma cor personalizada para o texto do botão, utilizada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0, 0, 0, 1] (preto).

# md_bg_color
# Descrição: Define a cor de fundo do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: md_bg_color=[1, 1, 1, 1] (branco).

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

# radius
# Descrição: Define o raio das bordas arredondadas do botão.
# Tipo: int ou float
# Padrão: 25
# Exemplo: radius=[30] (arredondamento uniforme).


# Funcionalidade Geral:
# O MDRoundFlatButton é um botão funcional e estiloso que se destaca em interfaces onde um design discreto é preferido.
# Ele é frequentemente utilizado em contextos onde as ações são secundárias ou complementares, como em formulários ou menus.
# Sua aparência arredondada e plana torna-o versátil e esteticamente agradável, ajudando a criar uma interface# de usuário limpa e moderna.
