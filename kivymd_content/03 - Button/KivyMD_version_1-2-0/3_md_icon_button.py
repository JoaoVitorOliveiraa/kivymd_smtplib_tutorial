# Arquivo de exemplo da função MDIconButton.
from kivy import icon_dir
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        # Criação da tela.
        screen = Screen()
        icon_button = MDIconButton(icon = "airplane-check",
                                   theme_text_color = CUSTOM,
                                   text_color = PRETO,
                                   md_bg_color = VERMELHO,
                                   size_hint = (0.2, 0.2),
                                   pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(icon_button)      # Adiciona o botão na tela.
        return  screen                      # Retorna a tela.

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDICONBUTTON -----

# O MDIconButton no KivyMD é um botão composto apenas por um ícone, sem texto ou borda, seguindo o estilo Material Design.
# Este tipo de botão é útil para ações rápidas e compactas, como ícones de configurações, fechar, compartilhar, etc.
# É frequentemente usado em barras de navegação, cabeçalhos e em qualquer lugar onde um botão textual ocuparia muito espaço.

# Abaixo estão os principais parâmetros e propriedades do MDIconButton:

# 1. icon
# Descrição: Define o ícone exibido no botão, com base na coleção de ícones do Material Design.
# Tipo: str
# Padrão: "android"
# Exemplo: icon="home"

# 2. theme_text_color
# Descrição: Define a cor do ícone de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Exemplo: theme_text_color="Secondary"

# 3. text_color
# Descrição: Define uma cor personalizada para o ícone, utilizada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[1, 0, 0, 1] (um tom de vermelho).

# 4. on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Icon button clicked")

# 5. disabled
# Descrição: Define se o botão está desativado, impedindo interações e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False
# Exemplo: disabled=True

# 6. pos_hint
# Descrição: Define a posição do botão na tela usando proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}

# 7. md_bg_color
# Descrição: Define a cor de fundo do botão (usado raramente, já que o MDIconButton é geralmente um botão transparente).
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Padrão: Transparente.
# Exemplo: md_bg_color=[0, 0.5, 0.5, 0.2] (um tom de ciano com transparência).

# 8. opacity
# Descrição: Define a opacidade do botão, útil para controlar a visibilidade sem desativar o botão.
# Tipo: float
# Padrão: 1.0 (totalmente opaco)
# Exemplo: opacity=0.8


# Funcionalidade Geral:
# O MDIconButton é ideal para ações rápidas e visuais que não precisam de rótulos textuais, tornando-se uma escolha
# popular para ícones de navegação, ações em listas, ou atalhos em barras de ferramentas. Com opções de personalização
# de cor, tamanho e posicionamento, ele oferece flexibilidade para se adaptar ao design da aplicação,
# seguindo as diretrizes de design minimalista e responsivo do Material Design.
