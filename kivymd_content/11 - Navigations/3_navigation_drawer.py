# Arquivo de exemplo da função MDNavigationDrawer.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText

screen_string = '''
# Um componente personalizado que representa um item dentro do menu lateral (MDNavigationDrawer).
# Itens do menu com ícones (gmail, send), textos (Inbox, Outbox) e um número de mensagens.
<DrawerItem>
    active_indicator_color: "#e7e4c0"               # Define a cor do indicador ativo, que aparece quando o item está selecionado ou destacado.

    # Adiciona um ícone à esquerda do item do menu.
    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon                             # Usa a propriedade icon definida na classe DrawerItem.
        theme_icon_color: "Custom"                  # Define que a cor do ícone será personalizada e não o padrão do tema.
        icon_color: "#4a4939"                       # Define a cor do ícone.

    # Adiciona o texto ao lado do ícone no item do menu.
    MDNavigationDrawerItemText:
        text: root.text                             # Usa a propriedade text definida na classe DrawerItem para definir o texto dinamicamente.
        theme_text_color: "Custom"                  # Define que a cor do texto será personalizada.
        text_color: "#4a4939"                       # Define a cor do texto.


# Um componente personalizado que representa um rótulo dentro do menu lateral (MDNavigationDrawer).
# Representa uma categoria dentro do menu.
<DrawerLabel>
    adaptive_height: True                           # Faz com que a altura do rótulo se ajuste automaticamente ao seu conteúdo, garantindo que o layout fique responsivo.
    padding: "18dp", 0, 0, "12dp"                   # Define o espaçamento interno do rótulo:
    
    # Adiciona um ícone à esquerda do rótulo.
    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon                             # Usa a propriedade icon definida na classe DrawerLabel no Python.
        pos_hint: {"center_y": .5}                  # Posiciona o ícone verticalmente no centro do rótulo.
        theme_icon_color: "Custom"                  # Define que a cor do ícone será personalizada, em vez de usar a cor padrão do tema.
        icon_color: "#4a4939"                       # Define a cor do ícone.

    # Adiciona o texto ao lado do ícone.            
    MDNavigationDrawerLabel:
        text: root.text                             # Usa a propriedade text definida na classe DrawerLabel, tornando o texto dinâmico.
        pos_hint: {"center_y": .5}                  # Posiciona o texto verticalmente no centro do rótulo.
        padding: "6dp", 0, "16dp", 0                # Define o espaçamento interno do texto.
        theme_line_height: "Custom"                 # Define que o espaçamento entre linhas será personalizado.
        line_height: 0                              # Define que não haverá espaçamento entre linhas.
        theme_text_color: "Custom"                  # Define que a cor do texto será personalizada, em vez de usar a cor padrão do tema.
        text_color: "#4a4939"                       # Define a cor do texto.


# Cria uma tela principal da interface do aplicativo.
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    # Componente principal que gerencia layout de navegação, permitindo o uso de um menu lateral (MDNavigationDrawer).
    # Ele deve conter dois filhos obrigatórios: MDScreenManager e MDNavigationDrawer.
    MDNavigationLayout:

        # Gerencia telas e permite alternar entre elas.
        MDScreenManager:
            
            # Cria uma tela dentro do MDScreenManager.
            MDScreen:
                    
                # Botão central que, ao ser pressionado, abre o drawer.
                MDButton:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: nav_drawer.set_state("toggle")

                    MDButtonText:
                        text: "Open Drawer"
        
        # Representa o menu lateral deslizante.
        MDNavigationDrawer:
            id: nav_drawer                      # Define um id para o drawer, permitindo acessá-lo no código Python.
            radius: 0, dp(16), dp(16), 0        # Define o arredondamento dos cantos do drawer.           
            drawer_type: "modal"                # Define o comportamento do drawer. 
                                                # "standard": O drawer empurra o conteúdo da tela ao abrir.
                                                # "modal": O drawer sobrepõe o conteúdo da tela.
            anchor: "left"                      # Define o lado da tela onde o drawer aparece.
                                                # "left":  O drawer desliza da esquerda.
                                                # "right": O drawer desliza da direita.
            scrim_color: (1, 0.2, 0.8, 0.2)     # Define a cor de fundo escurecida quando o drawer está aberto.
            padding: 40                         # Define um espaçamento interno de 40dp dentro do drawer.
            background_color: (0.2, 1, 0.4, 1)  # Define a cor de fundo do drawer.
            theme_elevation_level: 'Custom'     # Define se a sombra do drawer será personalizada ou baseada no tema do app.
            elevation_level: 5                  # Define a intensidade da sombra atrás do drawer. Valores: 0 a 5.

            # Contém os itens do drawer.
            MDNavigationDrawerMenu:
            
                # Cabeçalho do menu com dois MDLabel, sendo eles 'Título do menu' e 'Texto descritivo abaixo do título'.
                MDNavigationDrawerHeader:
                    orientation: "vertical"     # Define a organização dos elementos dentro do cabeçalho.
                    padding: 0, 0, 0, "12dp"    # Define o espaçamento interno dentro do cabeçalho.
                    adaptive_height: True       # Faz com que a altura do cabeçalho se ajuste automaticamente ao conteúdo interno.

                    MDLabel:
                        text: "Header title"
                        adaptive_height: True
                        padding_x: "16dp"
                        font_style: "Display"
                        role: "small"

                    MDLabel:
                        text: "Header text"
                        padding_x: "18dp"
                        adaptive_height: True
                        font_style: "Title"
                        role: "large"

                # Linha divisória entre seções do menu.
                MDNavigationDrawerDivider:

                # Criação de um item.
                DrawerItem:
                    icon: "gmail"
                    text: "Inbox"
                    trailing_text: "+99"
                    
                DrawerItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:
                
                # Rótulo para separar seções do menu.
                MDNavigationDrawerLabel:
                    text: "Labels"
                    padding_y: "12dp"
                
                # Criação de uma label.
                DrawerLabel:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabel:
                    icon: "information-outline"
                    text: "Label"
            
                MDNavigationDrawerDivider:
'''

# Essa classe personalizada representa um item de menu dentro do MDNavigationDrawer.
class DrawerLabel(MDBoxLayout):
    icon = StringProperty()         # Armazena o nome ou caminho de um ícone que será exibido ao lado do texto.
    text = StringProperty()         # Armazena o texto a ser exibido ao lado do ícone no item do menu.
                                    # StringProperty é uma propriedade do Kivy que armazena strings.

# Classe que cria um item de menu dentro do drawer com ícone, texto e texto adicional (trailing text).
class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()                 # Armazena o nome do ícone a ser exibido no item do menu.
    text = StringProperty()                 # Armazena o texto do item de menu.
    trailing_text = StringProperty()        # Armazena um texto adicional que será exibido à direita do item de menu.

    # O metodo on_trailing_text é chamado sempre que o valor da propriedade trailing_text é alterado.
    def on_trailing_text(self, instance, value):

        # Cria um novo widget MDNavigationDrawerItemTrailingText com o valor de trailing_text.
        self.trailing_text_obj = MDNavigationDrawerItemTrailingText(text=value)

        # Adiciona o widget MDNavigationDrawerItemTrailingText ao item de menu.
        self.add_widget(self.trailing_text_obj)


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

MyApp().run()



#                               ----- Descrição da função MDNavigationDrawer -----

# O MDNavigationDrawer é o componente principal que representa o menu lateral (drawer) em um aplicativo KivyMD.
# Ele é usado para exibir opções de navegação de maneira acessível e elegante.

# Parâmetros importantes:
# id: Usado para identificar o drawer dentro do código, permitindo acesso direto a ele.
# radius: Define o raio da borda do drawer, criando um efeito arredondado nas bordas. O valor é uma tupla de 4 valores, representando os cantos superior-esquerdo, superior-direito, inferior-direito e inferior-esquerdo.
# drawer_type: Pode ser "standard" (drawer fixo) ou "modal" (drawer que aparece e desaparece ao ser aberto).
# anchor: Define de qual lado a gaveta aparece. Pode ser "left" (esquerda) ou "right" (direita).
# scrim_color: Define a cor do scrim (área sombreada) que aparece atrás do drawer quando ele é aberto. O valor é uma tupla RGBA.
# padding: Define o espaçamento interno do drawer, ou seja, a distância entre os elementos dentro do drawer e suas bordas.
# background_color: A cor de fundo do drawer, definida por uma tupla RGBA.
# theme_elevation_level: Controla o nível de elevação do drawer (sombra).
# elevation_level: Controla o nível de elevação do drawer, sendo um valor entre 0 e 5.


#                               ----- Descrição da função MDNavigationLayout -----

# O MDNavigationLayout é um layout que permite a criação de um layout de navegação responsivo,
# com um MDNavigationDrawer (menu lateral) e um MDScreenManager (gerenciador de telas) para
# alternar entre diferentes telas de navegação.
# O MDNavigationLayout organiza a disposição do drawer e da tela principal.

# Parâmetros importantes:
# MDNavigationDrawer: O menu lateral dentro do layout.
# MDScreenManager: A área principal onde as telas são exibidas, permitindo a navegação entre elas.


#                               ----- Descrição da função MDNavigationDrawerMenu -----

# MDNavigationDrawerMenu é um contêiner que agrupa todos os itens de menu dentro do MDNavigationDrawer.
# Ele agrupa todos os MDNavigationDrawerItem que serão usados para criar os itens dentro do menu lateral.

# Parâmetros importantes:
# Não possui parâmetros específicos próprios além de herdar os parâmetros do MDBoxLayout.


#                               ----- Descrição da função MDNavigationDrawerLabel -----

# MDNavigationDrawerLabel é um widget usado para exibir etiquetas de texto dentro do menu do drawer,
# muitas vezes usadas para dividir diferentes seções de itens de navegação.

# Parâmetros importantes:
# text: O texto a ser exibido na etiqueta.
# theme_text_color: Define a cor do texto.
# text_color: Permite definir uma cor personalizada para o texto.
# padding_y: Define o preenchimento vertical.
# pos_hint: Controla a posição do widget dentro do layout.


#                               ----- Descrição da função MDNavigationDrawerItem -----

# MDNavigationDrawerItem é um item de menu individual dentro do MDNavigationDrawer. Ele é utilizado para
# representar opções de navegação e geralmente contém um ícone e texto.

# Parâmetros importantes:
# icon: O ícone que será exibido ao lado do texto. Pode ser um nome de ícone (ex: "home") ou o caminho para o ícone.
# text: O texto que será exibido ao lado do ícone.
# on_release: Função ou metodo que será chamado quando o item for clicado.
# trailing_text: Texto adicional exibido à direita do item de menu.


#                               ----- Descrição da função MDNavigationDrawerItemLeadingIcon -----

# O MDNavigationDrawerItemLeadingIcon é o componente que exibe o ícone à esquerda de um item dentro
# do MDNavigationDrawerItem. Ele faz parte do item de menu, junto com o texto e o texto adicional.

# Parâmetros importantes:
# icon: O nome do ícone que será exibido.
# theme_icon_color: Define a cor do ícone.
# icon_color: Permite definir uma cor personalizada para o ícone.


#                               ----- Descrição da função MDNavigationDrawerItemText -----

# O MDNavigationDrawerItemText é o widget que exibe o texto principal dentro de um MDNavigationDrawerItem.

# Parâmetros importantes:
# text: O texto a ser exibido dentro do item de menu.
# theme_text_color: Define a cor do texto.
# text_color: Permite definir uma cor personalizada para o texto.


#                               ----- Descrição da função MDNavigationDrawerItemTrailingText -----

# O MDNavigationDrawerItemTrailingText exibe o texto à direita de um MDNavigationDrawerItem,
# geralmente usado para exibir informações complementares, como um contador ou status.

# Parâmetros importantes:
# text: O texto a ser exibido à direita do item.
# theme_text_color: Define a cor do texto.
# text_color: Permite definir uma cor personalizada para o texto.

#                               ----- Descrição da função MDNavigationDrawerDivider -----

# O MDNavigationDrawerDivider é um componente usado para adicionar uma linha divisória entre
# os itens do menu no drawer. Ele ajuda a organizar visualmente os itens e separar seções.

# Parâmetros importantes:
# Não tem parâmetros próprios além de herdar os parâmetros de layout.


#                               ----- Descrição do trecho "on_release: nav_drawer.set_state("toggle")" -----

# A linha on_release: nav_drawer.set_state("toggle") faz parte da interação com o MDNavigationDrawer no código fornecido,
# e é usada para alternar (abrir ou fechar) o drawer (menu lateral) quando o botão é pressionado.

# O que é on_release?
# on_release é um evento de interação do Kivy, que é disparado quando o usuário solta o botão (após pressioná-lo).
# Esse evento é comumente usado em botões para definir ações a serem realizadas quando o usuário clica no botão e o solta.

# O que é nav_drawer?
# nav_drawer é o identificador da instância do componente MDNavigationDrawer. Esse componente é responsável pelo menu lateral que pode ser aberto ou fechado.
# O MDNavigationDrawer geralmente contém um menu de navegação, que pode ser mostrado ou ocultado com base na interação do usuário, como deslizar ou clicar em um botão.

# O que é set_state("toggle")?
# set_state("toggle") é um metodo usado para alternar o estado do MDNavigationDrawer.
# "toggle" é um estado especial que alterna entre abrir e fechar o drawer.
# Quando você chama nav_drawer.set_state("toggle"), o KivyMD verifica o estado atual do drawer:
# Se ele estiver fechado, o metodo abre o drawer.
# Se ele estiver aberto, o metodo fecha o drawer.

# Exemplo do Fluxo:
# Vamos detalhar o fluxo de interação com o on_release: nav_drawer.set_state("toggle") no código:
# O botão (onde a linha on_release: nav_drawer.set_state("toggle") está configurada) é exibido na tela.
# Esse botão é um MDButton posicionado no centro da tela, com o texto "Open Drawer".
# Quando o usuário pressiona e solta o botão:
# O evento on_release é disparado.
# O nav_drawer.set_state("toggle") é chamado.
# O que acontece internamente com o MDNavigationDrawer?
# Se o drawer (menu lateral) estiver fechado, ele será aberto.
# Se o drawer estiver aberto, ele será fechado.

# Por que usar toggle?
# O estado "toggle" é útil porque ele automaticamente lida com a alternância do estado do drawer sem precisar
# saber se ele está aberto ou fechado previamente. Com apenas uma linha de código, o drawer alterna entre os
# dois estados (aberto/fechado), tornando o código mais simples e conciso.

# Conclusão:
# A linha on_release: nav_drawer.set_state("toggle") faz com que o MDNavigationDrawer (menu lateral) seja aberto
# ou fechado quando o botão é pressionado. Usando o estado "toggle", o MDNavigationDrawer alterna automaticamente
# entre aberto e fechado sem a necessidade de verificar o estado atual manualmente. Esse é um comportamento comum
# em interfaces de usuário, onde o menu lateral pode ser acessado e ocultado com um simples toque no botão.