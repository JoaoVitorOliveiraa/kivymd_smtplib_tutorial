# Arquivo de exemplo da função MDFillRoundFlatIconButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatIconButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()    # Criação da tela.
        texto = "João"
        fill_round_flat_icon_button = MDFillRoundFlatIconButton(text = texto,
                                    icon = "alpha",
                                    font_size = 20,
                                    theme_text_color = CUSTOM,
                                    text_color = AMARELO,
                                    line_color = VERMELHO,
                                    md_bg_color = PRETO,
                                    theme_icon_color = CUSTOM,
                                    icon_color = VERDE,
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(fill_round_flat_icon_button)   # Adiciona o botão na tela.
        return  screen                                   # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDFillRoundFlatIconButton -----

# O MDFillRoundFlatIconButton no KivyMD é um botão que combina um ícone e texto em um design arredondado e preenchido,
# seguindo as diretrizes do Material Design. Este tipo de botão é ideal para ações que requerem um destaque visual,
# sendo fácil de identificar e utilizar. Ele é frequentemente usado em interfaces onde a combinação de um ícone e
# texto pode ajudar a esclarecer a ação do botão, como em menus de navegação ou ações em formulários.


# Aqui estão os principais parâmetros e propriedades do MDFillRoundFlatIconButton:

# text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Add"

# icon
# Descrição: Define o ícone exibido no botão, utilizando a coleção de ícones do Material Design.
# Tipo: str
# Padrão: Nenhum ícone.
# Exemplo: icon="plus".

# font_size
# Descrição: Define o tamanho da fonte do texto do botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=18.

# theme_text_color
# Descrição: Define a cor do texto e do ícone de acordo com o tema da aplicação.
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

# radius
# Descrição: Define o raio das bordas arredondadas do botão.
# Tipo: int ou float
# Padrão: 25
# Exemplo: radius=[20] (arredondamento uniforme).


# Funcionalidade Geral:
# O MDFillRoundFlatIconButton é ideal para ações que requerem um destaque visual significativo, como botões de adição,
# compartilhamento ou qualquer outra chamada à ação importante. Com seu design arredondado e fundo preenchido, ele
# oferece um visual moderno e atraente, facilmente personalizável em termos de cor, ícone, texto e tamanho. Isso o
# torna uma escolha popular para desenvolvedores que buscam criar interfaces intuitivas e esteticamente agradáveis
# em seus aplicativos KivyMD.
