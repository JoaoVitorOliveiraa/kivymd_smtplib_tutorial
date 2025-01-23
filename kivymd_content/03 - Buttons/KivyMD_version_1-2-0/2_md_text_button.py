# Arquivo de exemplo da função MDTextButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDTextButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()                                                              # Criação da tela.
        texto = "Press Here Now"
        text_button = MDTextButton(text = texto,
                                   font_style = H4,                                    # Estilo da fonte do texto.
                                   theme_text_color = CUSTOM,
                                   text_color = ROXO_CLARO,
                                   opacity = 0.5,
                                   pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(text_button)    # Adiciona o botão na tela.
        return  screen                    # Retorna a tela.

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDTEXTBUTTON -----

# O MDTextButton no KivyMD é um botão de texto simples, sem contorno, borda ou fundo, seguindo o padrão de Material Design.
# Ele exibe apenas texto e é utilizado para ações menos proeminentes, onde o botão deve ser discreto. Normalmente, é
# usado em links de "Cancelar", "Esqueci minha senha", "Saiba mais" e outras ações secundárias.

# Aqui estão os principais parâmetros e propriedades do MDTextButton:

# 1. text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Learn More"

# 2. font_size
# Descrição: Define o tamanho da fonte do texto do botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=18

# 3. theme_text_color
# Descrição: Define a cor do texto de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Exemplo: theme_text_color="Hint"

# 4. text_color
# Descrição: Define uma cor personalizada para o texto do botão, utilizada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0.5, 0.3, 0.8, 1] (um tom de roxo).

# 5. on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Button pressed")
# 6. disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False
# Exemplo: disabled=True

# 7. pos_hint
# Descrição: Define a posição do botão na tela com base em proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}

# 8. size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(0.2, 0.05)

# 9. opacity
# Descrição: Define a opacidade do botão, útil para ajustar a visibilidade sem desativá-lo.
# Tipo: float
# Padrão: 1.0 (totalmente opaco)
# Exemplo: opacity=0.8


# Funcionalidade Geral:
# O MDTextButton é ideal para ações secundárias que devem ser discretas na interface do usuário, sendo usado em links de
# ação ou para oferecer opções que não precisam de muito destaque. Com seu estilo minimalista, ele permite a personalização
# de cor, fonte e tamanho, e se adapta a uma variedade de contextos onde é necessário um botão leve, sem contorno ou fundo.
