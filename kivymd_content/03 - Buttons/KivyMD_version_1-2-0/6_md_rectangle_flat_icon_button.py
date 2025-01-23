# Arquivo de exemplo da função MDRectangleFlatIconButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()    # Criação da tela.
        texto = "João"
        rect_flat_icon_button = MDRectangleFlatIconButton(text = texto,
                                    icon = "alpha",
                                    font_size = 20,
                                    theme_text_color = CUSTOM,
                                    text_color = ROXO_CLARO,
                                    line_color = ROXO_ESCURO,
                                    md_bg_color = AMARELO,
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(rect_flat_icon_button)   # Adiciona o botão na tela.
        return  screen                             # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDRECTANGLEFLATICONBUTTON -----

# O MDRectangleFlatIconButton no KivyMD é um botão que combina um ícone e texto em um formato retangular, seguindo as
# diretrizes do Material Design. Este botão é ideal para ações que precisam de um destaque moderado, permitindo que o
# usuário identifique rapidamente a ação associada tanto pelo texto quanto pelo ícone.
#
# Aqui estão os principais parâmetros e propriedades do MDRectangleFlatIconButton:
#
# 1. text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Add"

# 2. icon
# Descrição: Define o ícone exibido no botão, utilizando a coleção de ícones do Material Design.
# Tipo: str
# Padrão: Nenhum ícone.
# Exemplo: icon="plus".

# 3. font_size
# Descrição: Define o tamanho da fonte do texto do botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=18.

# 4. theme_text_color
# Descrição: Define a cor do texto e do ícone de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom".
# Exemplo: theme_text_color="Primary".

# 5. text_color
# Descrição: Define uma cor personalizada para o texto do botão, utilizada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0.2, 0.6, 0.8, 1] (um tom de azul).

# 6. line_color
# Descrição: Define a cor do contorno do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Padrão: A cor padrão do Material Design para o texto.
# Exemplo: line_color=[0, 0, 0, 1] (preto).

# 7. md_bg_color
# Descrição: Define a cor de fundo do botão, que é visível apenas quando o botão é pressionado.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: md_bg_color=[0.9, 0.9, 0.9, 1] (um cinza claro).

# 8. on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Button pressed").

# 9. disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False.
# Exemplo: disabled=True.

# 10. pos_hint
# Descrição: Define a posição do botão na tela usando proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}.

# 11. size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(0.3, 0.1).


# Funcionalidade Geral:
# O MDRectangleFlatIconButton é ideal para ações que requerem um destaque moderado e visualização clara, com suporte a
# ícones e texto. Ele é frequentemente utilizado em contextos onde a identificação rápida da função é importante, como
# em formulários, menus de navegação e listas de ações. Com a capacidade de personalização em termos de cor, ícone,
# texto e posicionamento, ele se adapta bem a diversas aplicações com design moderno e intuitivo.
