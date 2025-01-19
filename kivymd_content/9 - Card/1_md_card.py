# # Arquivo de exemplo da função MDCard.
#
# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivymd_smtplib_tutorial.kivymd_content.config_macros import *
#
# KV = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDBoxLayout:
#         pos_hint: {"center_x": 0.5, "center_y": 0.5}
#
#         MDCard:
#             style: "elevated"
#             padding: "4dp"
#             size_hint: None, None
#             size: "240dp", "100dp"
#             theme_shadow_color: "Custom"                    # Valores: 'Primary' e 'Custom'
#             shadow_color: "green"
#             theme_bg_color: "Custom"                        # Valores: 'Primary' e 'Custom'
#             md_bg_color: (30/255, 22/255, 71/255, 1)
#             md_bg_color_disabled: "grey"
#             theme_shadow_offset: "Custom"                   # Valores: 'Primary' e 'Custom'
#             shadow_offset: (1, 0)
#             theme_shadow_softness: "Custom"                 # Valores: 'Primary' e 'Custom'
#             shadow_softness: 1
#             theme_elevation_level: "Primary"                # Valores: 'Primary' e 'Custom'
#             elevation_level: 5                              # Valores: 1 a 5
#
#         MDIconButton:
#             icon: "dots-vertical"
#             pos_hint: {"top": 1, "right": 1}
#
#         MDLabel:
#             text: "Elevated"
#             adaptive_size: True
#             color: "grey"
#             pos: "12dp", "12dp"
#             bold: True
# '''
#
#
# class MainApp(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         self.theme_cls.primary_palette = PALETA_AZUL
#         self.theme_cls.theme_style = TEMA_CLARO
#
#         screen = Builder.load_string(KV)
#         return screen
#
# MainApp().run()



#                               ----- Descrição da função MDCard -----

# O componente MDCard é um widget do KivyMD que cria um contêiner estilizado, frequentemente usado para exibir
# informações organizadas em blocos. Ele suporta personalizações diversas, como sombras, cores e elevação.
# Abaixo está uma explicação dos parâmetros usados:

# 1. style
# Descrição: Define o estilo do card.
# Valores:
# "elevated": Adiciona uma sombra ao card para criar um efeito de "elevação" (parece estar acima do plano de fundo).
# "filled": Preenche o card com a cor de fundo sem sombra.
# "outlined": Adiciona uma borda ao card, mas sem sombra ou elevação.

# 2. pos_hint
# Descrição: Posiciona o card na tela, usando valores relativos.
# Valores:
# "center_x": .5: Centraliza o card horizontalmente.
# "center_y": .5: Centraliza o card verticalmente.
# Funcionamento: Esses valores são proporcionais, onde 1.0 representa o lado direito/inferior da tela e 0.0 representa o lado esquerdo/superior.

# 3. padding
# Descrição: Define o espaçamento interno entre o conteúdo do card e suas bordas.
# Valores: "4dp":
# Adiciona um espaçamento de 4 unidades de densidade independente de pixel (dp).

# 4. size_hint
# Descrição: Controla como o card deve ajustar seu tamanho com base no layout pai.
# Valores:
# None, None: Define que o tamanho será fixo e especificado manualmente, sem depender do layout pai.
# Observação: Quando None é usado, é obrigatório especificar o tamanho exato usando o parâmetro size.

# 5. size
# Descrição: Especifica a largura e altura do card.
# Valores:
# "240dp": Largura do card.
# "100dp": Altura do card.

# 6. theme_shadow_color
# Descrição: Permite customizar a cor da sombra do card.
# Valores:
# "Primary": Define como a cor primária do app.
# "Custom": Habilita o uso de uma cor personalizada para a sombra (especificada em shadow_color).

# 7. shadow_color
# Descrição: Define a cor personalizada da sombra do card.
# Valores:
# "green": A sombra será verde.
# Requisito: O valor de theme_shadow_color deve ser "Custom" para que essa configuração funcione.

# 8. theme_bg_color
# Descrição: Permite customizar a cor de fundo do card.
# Valores:
# "Primary": Define como a cor primária do app.
# "Custom": Habilita o uso de uma cor personalizada para o fundo (definida em md_bg_color).

# 9. md_bg_color
# Descrição: Define a cor de fundo personalizada do card.
# Valores:
# "white": O fundo do card será branco.

# 10. md_bg_color_disabled
# Descrição: Define a cor de fundo do card quando ele estiver desabilitado.
# Valores:
# "grey": O fundo do card será cinza caso ele esteja desativado.

# 11. theme_shadow_offset
# Descrição: Permite customizar o deslocamento da sombra do card.
# Valores:
# "Primary": Deslocamento padrão.
# "Custom": Habilita o uso de valores personalizados para o deslocamento da sombra (definido em shadow_offset).

# 12. shadow_offset
# Descrição: Controla o deslocamento da sombra em relação ao card. É um tupla de dois valores (x, y), onde
# x: deslocamento horizontal.
# Valores positivos movem a sombra para a direita.
# Valores negativos movem a sombra para a esquerda.
# y: deslocamento vertical.
# Valores positivos movem a sombra para baixo.
# Valores negativos movem a sombra para cima.
# Valores possíveis:
# Qualquer tupla de números inteiros ou de ponto flutuante, como (0, 0), (1, -2), ou (10, 10).
# Padrão: (0, 2) (caso não especificado).

# 13. theme_shadow_softness: "Custom"
# Descrição: Permite personalizar a suavidade da sombra.
# Valores:
# "Primary": Suavidade padrão.
# "Custom": Habilita o uso de um valor personalizado para a suavidade (definido em shadow_softness).

# 14. shadow_softness: 1
# Descrição: Define o nível de suavidade da sombra.
# Valores: Quanto maior, mais difusa será a sombra.
# Padrão: 2 (caso não especificado).

# 15. theme_elevation_level: "Custom"
# Descrição: Permite definir um nível personalizado de elevação para o card.
# Valor:
# "Primary": Elevação padrão.
# "Custom": Habilita o uso de valores definidos manualmente para a elevação (definido em elevation_level).

# 16. elevation_level: 2
# Descrição: Define o nível de elevação do card, que afeta a aparência da sombra.
# Valores entre 1 a 5.
# Observação: Valores maiores aumentam a distância percebida do card em relação ao fundo.


from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

screen_string = '''

# Define o design do widget de cartão.
<MyCard>
    padding: "4dp"
    size_hint: None, None
    size: "240dp", "100dp"

    MDRelativeLayout:
        
        # Exibe um botão de ícone no canto superior direito.
        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}

        # Mostra o texto do cartão.
        MDLabel:
            
            # O termo 'root' se refere à classe base na qual o widget foi definido. 
            # No caso de <MyCard>, o root é a instância da classe MyCard.
            # O termo 'root.text' refere-se à propriedade text da classe MyCard.
        
            text: root.text         
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True

MDScreen:
    theme_bg_color: "Custom"
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        id: box
        adaptive_size: True
        spacing: "12dp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

# Criação de uma classe que herda de MDCard para criar cartões personalizados.
class MyCard(MDCard):

    # Adiciona a propriedade text como uma StringProperty.
    # StringProperty é reativa: qualquer alteração no valor atualiza automaticamente os widgets vinculados.
    text = StringProperty()

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)
        return screen

    def on_start(self):
        "Função que é chamada automaticamente após o aplicativo iniciar."

        # Adiciona os Cards no id do MDBoxLayout.
        for style in ("elevated", "filled", "outlined"):
            self.root.ids.box.add_widget(
                MyCard(style=style,
                       text=style.capitalize(),
                       pos_hint={"center_x": .5, "center_y":.5},
                       padding="4dp",
                       size_hint=(None, None),
                       size=(200, 300),
                       theme_bg_color=CUSTOM,
                       md_bg_color=BRANCO,              # Cor de preenchimento.
                       theme_shadow_color=CUSTOM,
                       shadow_color=AMARELO,            # Cor de fundo.
                       theme_shadow_offset="Custom",    # Define o deslocamento da shadow_color em relação ao widget que a projeta.
                       shadow_offset=(5, 5),            # Valores positivos (x ou y): Movem a sombra para a direita (x) ou para cima (y).
                                                        # Valores negativos (x ou y): Movem a sombra para a esquerda (x) ou para cima (y).
                                                        # Valores negativos (x ou y): Movem a sombra para a esquerda (x) ou para cima (y).
                       md_bg_color_disabled=VERMELHO,
                       theme_shadow_softness=CUSTOM,
                       shadow_softness=1,               # Suavidade da cor de fundo.
                       theme_elevation_level=CUSTOM,
                       elevation_level=5)               # Elevação da cor de fundo.
            )


MyApp().run()