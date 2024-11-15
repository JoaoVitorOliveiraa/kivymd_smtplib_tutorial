# Arquivo de exemplo da função MDRectangleFlatButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()                                                              # Criação da tela.
        texto = "Press Here"
        rect_flat_button = MDRectangleFlatButton(text = texto,
                                    font_size = 50,
                                    #font_style = H4,                                  # Estilo da fonte do texto.
                                    theme_text_color = CUSTOM,
                                    text_color = ROXO_CLARO,
                                    line_color = ROXO_ESCURO,
                                    md_bg_color = AMARELO,
                                    size_hint = (0.7, 0.3),
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(rect_flat_button)     # Adiciona o botão na tela.
        return  screen                          # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDRECTANGLEFLATBUTTON -----

# O MDRectangleFlatButton no KivyMD é um botão com formato retangular, sem elevação (sombra), com bordas simples e uma
# linha contornando o botão. Ele segue o padrão Material Design e é ideal para ações que precisam de destaque moderado,
# funcionando bem em interfaces que visam simplicidade e clareza.

# Aqui estão os principais parâmetros e propriedades do MDRectangleFlatButton:

# 1. text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Submit"

# 2. font_size
# Descrição: Define o tamanho da fonte do texto do botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=18

# 3. theme_text_color
# Descrição: Define a cor do texto de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Exemplo: theme_text_color="Primary"

# 4. text_color
# Descrição: Define uma cor personalizada para o texto do botão, usada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0.2, 0.6, 0.8, 1] (um tom de azul).

# 5. line_color
# Descrição: Define a cor do contorno do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Padrão: A cor padrão do Material Design para o texto.
# Exemplo: line_color=[0, 0, 0, 1] (preto).

# 6. md_bg_color
# Descrição: Define a cor de fundo do botão, que é visível apenas quando o botão é pressionado.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: md_bg_color=[0.9, 0.9, 0.9, 1] (um cinza claro).

# 7. on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Button pressed")

# 8. disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False
# Exemplo: disabled=True

# 9. pos_hint
# Descrição: Define a posição do botão na tela usando proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}

# 10. size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(0.3, 0.1)


# Funcionalidade Geral:
# O MDRectangleFlatButton é ideal para ações que necessitam de destaque, mas que não devem desviar
# muito a atenção do usuário, como opções secundárias ou botões de confirmação. Com contornos claros
# e sem elevação, ele oferece um estilo limpo e minimalista, sendo facilmente personalizável em termos
# de cor, texto, contorno e posicionamento para se adaptar ao design da aplicação.
