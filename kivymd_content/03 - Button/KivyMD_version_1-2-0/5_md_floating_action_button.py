# Arquivo de exemplo da função MDFloatingActionButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        # Criação da tela.
        screen = Screen()
        floating_action_button = MDFloatingActionButton(icon = "alpha",
                                    theme_text_color = CUSTOM,
                                    text_color = AZUL,
                                    md_bg_color = PRETO,
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(floating_action_button)    # Adiciona o botão na tela.
        return  screen                               # Retorna a tela.

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDFLOATINGACTIONBUTTON -----

# O MDFloatingActionButton no KivyMD é um botão de ação flutuante, seguindo o estilo Material Design, geralmente usado
# para destacar ações principais em uma interface. Este tipo de botão é redondo e costuma ficar posicionado em um canto
# ou sobreposto ao conteúdo da tela, chamando a atenção para a ação associada, como adicionar, editar ou compartilhar.

# Abaixo estão os principais parâmetros e propriedades do MDFloatingActionButton:

# 1. icon
# Descrição: Define o ícone exibido no botão, utilizando a coleção de ícones do Material Design.
# Tipo: str
# Padrão: "android"
# Exemplo: icon="plus" (para um botão de adicionar).

# 2. md_bg_color
# Descrição: Define a cor de fundo do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Padrão: A cor padrão do Material Design, como um tom de azul claro.
# Exemplo: md_bg_color=[1, 0.3, 0.2, 1] (um tom de vermelho).

# 3. theme_text_color
# Descrição: Define a cor do ícone dentro do botão com base no tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Exemplo: theme_text_color="Secondary"

# 4. text_color
# Descrição: Define uma cor personalizada para o ícone, usada apenas quando theme_text_color está configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0, 1, 0, 1] (um tom de verde).

# 5. elevation
# Descrição: Define a elevação (sombra) do botão, criando um efeito de profundidade para destacá-lo.
# Tipo: int ou float
# Padrão: Um valor padrão que segue o estilo do Material Design (geralmente 6).
# Exemplo: elevation=10

# 6. on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Button clicked")

# 7. pos_hint
# Descrição: Define a posição do botão na tela usando proporções, o que é útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.9, "center_y": 0.1}

# 8. size
# Descrição: Define o tamanho do botão em pixels, permitindo ajustes manuais do tamanho padrão.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size=(56, 56)

# 9. disabled
# Descrição: Desabilita o botão, tornando-o visualmente opaco e inacessível.
# Tipo: bool
# Padrão: False
# Exemplo: disabled=True

# 10. opacity
# Descrição: Controla a opacidade do botão, podendo ser usada para dar destaque visual.
# Tipo: float
# Padrão: 1.0 (totalmente opaco)
# Exemplo: opacity=0.8


# Funcionalidade Geral:

# O MDFloatingActionButton é ideal para ações principais que precisam de destaque visual na interface, sendo utilizado
# em contextos onde se deseja facilitar o acesso a uma função central. Com suporte a personalização de cor, ícone, elevação
# e posição, ele se integra bem em aplicativos com design limpo e moderno, chamando a atenção para as ações mais importantes.
