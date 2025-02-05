# Arquivo de exemplo da função MDFloatingActionButtonSpeedDial.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        # Criação da tela.
        screen = Screen()
        floating_action_button_speed_dial = MDFloatingActionButtonSpeedDial(
                                    data = [{"text": "Add", "icon": "plus"},
                                            {"text": "Edit", "icon": "pencil"},
                                            {"text": "Delete", "icon": "trash-can"}],
                                    icon = "plus",
                                    bg_hint_color = ROXO_CLARO,
                                    bg_color_stack_button = VERMELHO,
                                    bg_color_root_button = VERDE,
                                    color_icon_root_button = AMARELO,
                                    color_icon_stack_button = MARROM,
                                    label_bg_color = AZUL,
                                    label_text_color = ROXO_ESCURO,
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(floating_action_button_speed_dial)   # Adiciona o botão na tela.
        return  screen                                         # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDFloatingActionButtonSpeedDial -----

# O MDFloatingActionButtonSpeedDial no KivyMD é um componente que combina um botão de ação flutuante (FAB) com um menu
# de opções que podem ser exibidas quando o botão é pressionado. Esse tipo de botão é ideal para oferecer múltiplas
# ações relacionadas em um espaço compacto, seguindo as diretrizes do Material Design. O FAB principal geralmente é
# um botão grande que, ao ser clicado, revela outras opções de ações que podem ser selecionadas.

# Aqui estão os principais parâmetros e propriedades do MDFloatingActionButtonSpeedDial:

# data
# Descrição: Um dicionário que define os itens do menu de opções a serem exibidos no Speed Dial. Cada item deve incluir um ícone e um texto.
# Tipo: list de dicionários.
# Exemplo:
# data = [
#     {"text": "Add", "icon": "plus"},
#     {"text": "Edit", "icon": "pencil"},
#     {"text": "Delete", "icon": "trash-can"}]

# label
# Descrição: Um rótulo que pode ser exibido para o botão principal. É uma string que aparece ao lado do FAB.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: label="Actions"

# icon
# Descrição: Define o ícone do botão flutuante principal.
# Tipo: str
# Exemplo: icon="plus".

# callback
# Descrição: Uma função que é chamada quando uma das opções do menu é selecionada. Essa função recebe o item selecionado como argumento.
# Tipo: Função (callable).
# Exemplo:
# callback=lambda x: print(f"Selected: {x['text']}")

# pos_hint
# Descrição: Define a posição do botão na tela usando proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.9, "center_y": 0.1}.

# size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(None, None).

# transition
# Descrição: Define a transição a ser usada quando o menu é aberto ou fechado.
# Tipo: str
# Padrão: "scale" (outras opções incluem "fade" e "slide").
# Exemplo: transition="fade".

# background_color
# Descrição: Define a cor de fundo do botão flutuante principal.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: background_color=[0.1, 0.6, 0.2, 1] (um tom de verde).

# theme_background_color
# Descrição: Define a cor de fundo do botão flutuante principal de acordo com o tema da aplicação.
# Tipo: str
# Exemplo: theme_background_color="Primary".

# disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False.
# Exemplo: disabled=True.


# Funcionalidade Geral;
# O MDFloatingActionButtonSpeedDial é uma maneira elegante e funcional de agrupar várias ações em um único botão,
# melhorando a usabilidade e a organização da interface. Ao utilizar o botão de ação flutuante principal,
# os usuários podem acessar rapidamente várias opções sem sobrecarregar a interface com botões adicionais.
# Esse componente é especialmente útil em aplicativos móveis e interfaces com espaço limitado, proporcionando
# uma experiência de usuário intuitiva e moderna.
