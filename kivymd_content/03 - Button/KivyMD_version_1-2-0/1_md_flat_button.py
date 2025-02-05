# Arquivo de exemplo da função MDFlatButton.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from batcomputer_interface.config_text import *

class BatComputer(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Screen()                                                              # Criação da tela.
        texto = "Press"
        flat_button = MDFlatButton(text = texto,
                                   #font_size = 10,
                                   font_style = H3,                                    # Estilo da fonte do texto.
                                   theme_text_color = CUSTOM,
                                   text_color = ROXO_ESCURO,
                                   md_bg_color = MARROM,
                                   size_hint = (0.5, 0.6),
                                   pos_hint = {"center_x": 0.5, "center_y": 0.5})

        screen.add_widget(flat_button)        # Adiciona o botão na tela.
        return  screen                        # Retorna a tela.

BatComputer().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDFLATBUTTON -----

# O MDFlatButton no KivyMD é um botão estilizado de acordo com as diretrizes do Material Design. Ele exibe texto ou um
# ícone sem bordas em destaque, oferecendo um design minimalista e moderno. Este botão é ideal para ações que não precisam
# de ênfase visual (como botões secundários) e é amplamente utilizado em interfaces que buscam manter um layout limpo e funcional.

# Aqui estão os principais parâmetros e propriedades do MDFlatButton:

# 1. text
# Descrição: Define o texto exibido no botão.
# Tipo: str
# Padrão: "" (string vazia).
# Exemplo: text="Confirm"

# 2. icon
# Descrição: Adiciona um ícone ao botão, com base na coleção de ícones do Material Design.
# Tipo: str
# Padrão: Nenhum ícone.
# Exemplo: icon="check"

# 3. font_size
# Descrição: Define o tamanho da fonte do texto exibido no botão.
# Tipo: int ou float
# Padrão: O tamanho padrão do Material Design para botões (14 ou 16 pixels).
# Exemplo: font_size=18

# 4. theme_text_color
# Descrição: Define a cor do texto do botão com base no tema da aplicação.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Exemplo: theme_text_color="Primary"

# 5. text_color
# Descrição: Define uma cor personalizada para o texto do botão, utilizada apenas se theme_text_color estiver configurado como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0.5, 0.2, 0.8, 1] (um tom de roxo).

# 6. md_bg_color
# Descrição: Define a cor de fundo do botão.
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Padrão: Transparente para manter o estilo plano.
# Exemplo: md_bg_color=[0, 0, 0, 0.1] (cinza claro com transparência).

# 7. on_release
# Descrição: Função a ser executada quando o botão é pressionado e solto.
# Tipo: Função (callable).
# Exemplo: on_release=lambda: print("Button pressed")

# 8. disabled
# Descrição: Define se o botão está desativado, impedindo qualquer interação e alterando sua opacidade visualmente.
# Tipo: bool
# Padrão: False
# Exemplo: disabled=True

# 9. pos_hint
# Descrição: Define a posição do botão na tela com base em proporções. Útil para layouts responsivos.
# Tipo: Dicionário que define valores para x e y.
# Exemplo: pos_hint={"center_x": 0.5, "center_y": 0.5}

# 10. size_hint
# Descrição: Define o tamanho do botão com base em uma proporção da tela ou do contêiner.
# Tipo: Tupla de dois valores (largura e altura).
# Exemplo: size_hint=(0.2, 0.1)


# Funcionalidade Geral:

# O MDFlatButton é projetado para ações que não exigem um destaque visual intenso, geralmente usado em botões secundários
# ou para ações que complementam funções principais. Ele permite uma ampla personalização de cor, posicionamento e interação,
# e seu design simples contribui para interfaces organizadas e visualmente agradáveis.




#                               ----- DESCRIÇÃO DA CLASSE SCREEN -----

# A classe Screen no KivyMD é um widget que permite criar uma tela individual dentro de um aplicativo, seguindo o padrão
# do Kivy e das diretrizes do Material Design. Ela é parte do sistema de navegação do Kivy, permitindo que você organize
# sua interface em várias telas, que podem ser trocadas conforme necessário.

# Aqui estão os principais aspectos e funcionalidades da classe Screen:


#                                     Características Principais

# Contêiner de Tela:
# O Screen atua como um contêiner para outros widgets, permitindo que você crie interfaces complexas dentro de uma única tela.
# Cada instância de Screen pode conter diferentes widgets, como botões, textos, imagens, etc.

# Transições:
# O Screen é frequentemente utilizado em conjunto com ScreenManager, que permite alternar entre várias telas com diferentes
# tipos de animações e transições, como deslizamento, desvanecimento e outros efeitos visuais.

# Gerenciamento de Estado:
# Cada Screen pode manter seu próprio estado, o que significa que você pode gerenciar informações e dados específicos da
# tela sem interferir em outras telas. Isso é útil para aplicativos que requerem diferentes contextos de interação.


#                                   Principais Propriedades e Métodos

# name:
# Descrição: Define um nome para a tela, permitindo que você a identifique ao alternar entre telas.
# Tipo: str
# Exemplo: screen = Screen(name="home")

# manager:
# Descrição: Referência ao ScreenManager que contém a tela. Isso é útil se você quiser manipular a tela a partir de dentro dela.
# Tipo: ScreenManager

# on_enter e on_leave:
# Descrição: Eventos que podem ser usados para executar código quando a tela é exibida ou ocultada, respectivamente. Você pode
# adicionar métodos que serão chamados automaticamente nessas situações.
# Tipo: Funções (callables).

# Adicionando Widgets:
# Você pode adicionar widgets à tela simplesmente usando o metodo add_widget().

# Estilo e Layout:
# A classe Screen não impõe um layout específico, permitindo que você use layouts do Kivy, como BoxLayout,
# GridLayout, etc., para organizar os widgets conforme necessário.


# Funcionalidade Geral:
# A classe Screen é uma parte fundamental da estrutura de navegação em aplicativos KivyMD, permitindo a criação de interfaces
# organizadas e responsivas. Com sua capacidade de ser facilmente gerenciada e personalizada, ela é essencial para desenvolver
# aplicativos que exigem múltiplas vistas ou estados.
