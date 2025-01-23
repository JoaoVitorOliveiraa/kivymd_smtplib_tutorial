# Arquivo de exemplo da função MDTopAppBar.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = '''
MDScreen:
    md_bg_color: (1, 0.8, 0, 1)
    
    MDFloatLayout:
        id: float_layout
        
        MDTopAppBar:
            type: "small"                                   # Define o tipo de barra. Valores: "small", "medium" e "large".
            size_hint_x: 0.95                               # Largura relativa da barra em relação ao contêiner pai.
            size_hint_y: 0.1                                # Altura relativa da barra em relação ao contêiner pai.
            pos_hint: {"center_x": 0.5, "center_y": 0.94}   # Define a posição da barra no contêiner pai.
    
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "menu"                            # Define o ícone exibido no botão.
                    theme_icon_color: 'Custom'              # Define a cor do ícone como 'customizada'.
                    icon_color: (0.4, 1, 0.6, 1)            # Define a cor do ícone (quando theme_icon_color é "Custom").
                    theme_bg_color: "Custom"                # Define a cor de fundo como 'customizada'.
                    md_bg_color: (1, 0.5, 0.2, 1)           # Cor de fundo do botão.
                    on_release: app.add_card()              # Função chamada ao clicar no botão.
    
            MDTopAppBarTitle:
                text: "Arquivo de exemplo da função MDTopAppBar"    # Define o texto exibido no título.
                font_style: "Title"                                 # Estilo da fonte.
                role: "medium"                                      # Define o rótulo da fonte do texto do título.
                font_size: 14                                       # Tamanho da fonte do título.
                pos_hint: {"center_x": 0.5}                         # Define a posição do título no contêiner da barra.
    
            MDTopAppBarTrailingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "account-circle-outline"
                    theme_icon_color: 'Custom'
                    icon_color: (1, 0, 0, 1)
                
                MDActionTopAppBarButton:
                    icon: "attachment"
                    theme_bg_color: "Custom"
                    md_bg_color: (0, 1, 0, 1)
    
                MDActionTopAppBarButton:
                    icon: "calendar"
            
                MDActionTopAppBarButton:
                    icon: "dots-vertical"
'''

card_string = '''
MDCard:
    size_hint: 0.4, 0.6
    pos_hint: {"x": 0.028, "y": 0.287}
    radius: (0, 0, 0, 0)
    
    MDFloatLayout:
        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}

        MDLabel:
            text: 'Card'        
            adaptive_size: True
            color: "grey"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            bold: True
'''


class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

    def add_card(self):
        "Função que adiciona um card na tela."

        card = Builder.load_string(card_string)
        self.screen.ids.float_layout.add_widget(card)

MyApp().run()



#                               ----- Descrição da função MDTopAppBar -----

# A MDTopAppBar é um componente do KivyMD que cria uma barra superior (AppBar ou Toolbar) em conformidade
# com as diretrizes de Material Design. Essa barra é usada para exibir o título do aplicativo, ícones de
# ação (como menu, busca, configurações), ou qualquer outro elemento interativo necessário no topo da tela.

# Estrutura Geral da MDTopAppBar
# 1. MDTopAppBar: A barra principal.
# 2. MDTopAppBarTitle: O título exibido na barra.
# 3. MDTopAppBarLeadingButtonContainer: Área reservada para botões à esquerda.
# 4. MDTopAppBarTrailingButtonContainer: Área reservada para botões à direita.
# 5. MDActionTopAppBarButton: Botões de ação exibidos nas áreas esquerda ou direita.