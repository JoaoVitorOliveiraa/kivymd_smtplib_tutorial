# Arquivo de exemplo da função MDButton.

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        screen = MDScreen()                                                        # Criação da tela.
        button = MDButton(style = ELEVATED_BUTTON_STYLE,                           # Estilo do botão.
                               height = 50,                                        # Altura do botão.
                               width = 100,                                        # Largura do botão.
                               pos_hint = {"center_x": 0.5, "center_y": 0.5})      # Posição do centro do botão na tela.

        screen.add_widget(button)                                                  # Adiciona o botão na tela.
        return  screen                                                             # Retorna a tela.

MyApp().run()



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