# Arquivo de exemplo da função MDRoundFlatIconButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatIconButton
from old_config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()    # Criação da tela.
        texto = "João"
        round_flat_icon_button = MDRoundFlatIconButton(text = texto,
                                    icon = "account-box",
                                    font_size = 50,
                                    theme_text_color = CUSTOM,
                                    text_color = ROXO_CLARO,
                                    line_color = ROXO_ESCURO,
                                    md_bg_color = AMARELO,
                                    theme_icon_color = CUSTOM,
                                    icon_color = VERMELHO,
                                    size_hint = (0.4, 0.4),
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(round_flat_icon_button)   # Adiciona o botão na tela.
        return  screen                              # Retorna a tela

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDRoundFlatIconButton -----

# O MDRoundFlatIconButton no KivyMD é um componente que combina um design arredondado e plano com a funcionalidade de um
# botão que inclui um ícone. Este tipo de botão é ideal para ações que requerem uma representação visual clara, como um
# ícone, e é frequentemente usado em interfaces modernas para indicar funções específicas. O design arredondado oferece
# uma estética suave e acessível, alinhada com as diretrizes do Material Design.


# Aqui estão os principais parâmetros e propriedades do MDRoundFlatIconButton:

# icon
# Descrição: Define o ícone a ser exibido no botão. Este deve ser um nome de ícone válido do Material Design.
# Tipo: str
# Exemplo: icon="home".

# theme_text_color
# Descrição: Define a cor do texto (ou do ícone) do botão de acordo com o tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom".
# Exemplo: theme_text_color="Primary".

# text_color
# Descrição: Define uma cor personalizada para o texto (ou ícone) do botão, utilizada quando theme_text_color é configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0, 0, 0, 1] (preto).

# md_bg_color
# Descrição: Define a cor de fundo do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: md_bg_color=[1, 1, 1, 1] (branco).

# size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(0.1, 0.1).

# pos_hint
# Descrição: Define a posição do botão na tela usando proporções, útil para layouts responsivos.
# Tipo: Dicionário com valores x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}.

# on_release
# Descrição: Função a ser chamada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Icon button pressed").

# disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e deixando-o visualmente opaco.
# Tipo: bool
# Padrão: False.
# Exemplo: disabled=True.


# Funcionalidade Geral:
# O MDRoundFlatIconButton é um botão versátil e esteticamente agradável, ideal para ações que são frequentemente
# representadas por ícones. Sua combinação de design arredondado e aparência plana torna-o uma ótima opção para
# interfaces que precisam de elementos interativos, mas que também priorizam um visual moderno e limpo. Esse botão
# pode ser usado em barras de ferramentas, menus ou em qualquer lugar onde a representação visual da ação seja importante.
