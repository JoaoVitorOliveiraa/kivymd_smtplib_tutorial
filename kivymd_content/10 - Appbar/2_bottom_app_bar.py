# Arquivo de exemplo da função MDBottomAppBar.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.appbar import MDActionBottomAppBarButton

screen_string = '''
# Importação da classe MDActionBottomAppBarButton do módulo kivymd.uix.appbar.
#:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton

MDScreen:
    md_bg_color: (1, 0.8, 0.2, 1)

    # Cria a barra inferior do aplicativo.
    MDBottomAppBar:
        id: bottom_appbar       # Define um identificador para referenciar a barra no código Python.
        
        # Uma lista de botões adicionados à barra inferior. Cada botão é instanciado como MDActionBottomAppBarButton.
        action_items:           
            [
            MDActionBottomAppBarButton(icon="gmail"),
            MDActionBottomAppBarButton(icon="bookmark"),
            ]                   
        
        # O botão flutuante principal exibido na barra inferior.
        MDFabBottomAppBarButton:
            icon: "plus"                            # Define o ícone exibido no botão.
            theme_icon_color: 'Custom'              # Define a cor do ícone como 'customizada'.
            icon_color: (0, 0, 0, 1)                # Define a cor do ícone (quando theme_icon_color é "Custom").
            theme_bg_color: "Custom"                # Define a cor de fundo como 'customizada'.
            md_bg_color: (1, 0, 0, 1)               # Cor de fundo do botão.
            on_release: app.change_actions_items()  # Função chamada ao clicar no botão.
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

    def change_actions_items(self):
        "Função que altera os botões de ação exibidos na MDBottomAppBar."

        self.screen.ids.bottom_appbar.action_items = [
            MDActionBottomAppBarButton(icon="magnify"),
            MDActionBottomAppBarButton(icon="trash-can-outline"),
            MDActionBottomAppBarButton(icon="download-box-outline"),
        ]


MyApp().run()



#                               ----- Descrição da função MDBottomAppBar -----

# A MDBottomAppBar é um componente do KivyMD que cria uma barra de navegação localizada na parte inferior da tela.
# Essa barra pode conter botões de ação (ícones) e um botão flutuante central (FAB), sendo ideal para aplicativos
# que seguem o padrão de design do Material Design.

# Resumo dos Componentes:

# 1. Estrutura
# MDBottomAppBar: Cria a barra inferior que organiza os botões.
# MDFabBottomAppBarButton: Representa o botão flutuante principal na barra inferior.
# MDActionBottomAppBarButton: Representa botões adicionais exibidos na barra inferior.

# 2. Fluxo de Configuração
# A MDBottomAppBar serve como um container para os botões.
# O botão flutuante (FAB) é configurado usando MDFabBottomAppBarButton.
# Botões de ação adicionais são configurados com MDActionBottomAppBarButton e adicionados à lista action_items.


#     ----- Descrição da linha '#:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton' -----

# Essa linha faz parte da linguagem KV e usa a instrução #:import para importar uma
# classe Python no contexto da linguagem KV. Aqui está uma explicação detalhada:

# 1. O que é #:import?
# O #:import é uma diretiva especial da linguagem KV usada para importar classes ou
# objetos Python diretamente no arquivo ou string KV. Ele permite referenciar essas
# classes ou objetos no código KV, como se fossem nativos da linguagem KV.

# 2. O que está sendo importado aqui?
# MDActionBottomAppBarButton: É a classe do KivyMD que define um botão de ação para ser usado dentro da barra inferior (MDBottomAppBar).
# Essa classe é parte do módulo kivymd.uix.appbar.

# 3. Por que usar #:import nesse caso?
# No exemplo, MDActionBottomAppBarButton é usado dentro da propriedade action_items
# da MDBottomAppBar. Como a linguagem KV precisa conhecer a origem dessa classe, é
# necessário importá-la explicitamente com #:import.

# 4. Estrutura da linha #:import
# Estrutura --> #:import <nome_curto> <caminho_da_classe>
# <nome_curto>: O nome pelo qual você usará a classe no código KV.
# Neste caso, MDActionBottomAppBarButton.
# <caminho_da_classe>: O caminho completo do módulo e da classe no código Python.
# Aqui, kivymd.uix.appbar.MDActionBottomAppBarButton.

# 5. O que aconteceria sem #:import?
# Se #:import não fosse usado, você teria um erro no KV, porque o interpretador KV não saberia o que é MDActionBottomAppBarButton.

# 6. Resumo
# A linha #:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton faz o seguinte:
# Importa a classe MDActionBottomAppBarButton do módulo kivymd.uix.appbar.
# Permite o uso dessa classe diretamente no código KV, sem necessidade de referenciá-la no código Python.
# Ela é necessária para usar botões de ação (MDActionBottomAppBarButton) dentro da propriedade action_items da MDBottomAppBar.