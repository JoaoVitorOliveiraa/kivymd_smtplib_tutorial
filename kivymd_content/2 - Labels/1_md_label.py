# Arquivo de exemplo da função MDLabel.

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        texto = "João"
        label = MDLabel(text = texto,                                        # Texto
                        font_style = DISPLAY_TEXT_STYLE,                     # Fonte do texto
                        role = SMALL_TEXT_ROLE,                              # Rótulo da fonte do texto
                        font_size = SIZE_36,                                 # Tamanho da fonte.
                        theme_text_color = CUSTOM,                           # Modo de cor personalizada
                        text_color = ROXO_CLARO,                             # Cor no padrão RGBA (valores de 0 a 1)
                        bold = True,                                         # Negrito.
                        italic = True,                                       # Itálico.
                        adaptive_size = True,
                        allow_selection = True,                              # Permite destacar texto clicando duas vezes no rótulo.
                        color_selection = VERMELHO,                          # A cor em (r, g, b, a) ou formato de string da seleção
                                                                             # de texto quando o valor do atributo allow_selection é True.
                        color_deselection = VERDE,                           # A cor em (r, g, b, a) ou formato de string da desseleção
                                                                             # de texto quando o valor do atributo allow_selection é True.
                        allow_copy = True,                                   # Permite que você copie texto para a área de
                                                                             # transferência clicando duas vezes no rótulo.
                        #halign = "center")                                  # Posiciona o texto no centro da tela (adaptive_size = False).
                        pos_hint = {"center_x": 0.5, "center_y": 0.5})       # Posiciona o texto no centro da tela (adaptive_size = True).

        return label  # Retorna a Label

MyApp().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDFLATLABEL -----

# A função MDFlatLabel no KivyMD é um widget que representa um rótulo de texto simples em uma interface gráfica,
# seguindo o estilo do Material Design. Ela permite personalizar o texto exibido e possui alguns parâmetros e
# propriedades que oferecem flexibilidade na apresentação visual, sendo geralmente usada para exibir
# informações de forma clara e legível.

# Abaixo, estão os parâmetros e propriedades mais importantes do MDFlatLabel:

# 1. text
# Descrição: Define o texto que será exibido no rótulo.
# Tipo: str (string).
# Padrão: "" (string vazia).
# Exemplo: text="Hello World!"

# 2. font_style
# Descrição: Especifica o estilo da fonte a ser usado no rótulo. Este estilo segue as diretrizes do Material Design.
# Tipo: str

# 3. theme_text_color
# Descrição: Define a cor do texto com base no tema atual do aplicativo.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Exemplo: theme_text_color="Primary"

# 4. text_color
# Descrição: Define uma cor personalizada para o texto. É usada apenas se theme_text_color estiver definido como "Custom".
# Tipo: List ou Tuple de quatro valores (RGBA).
# Exemplo: text_color=[1, 0, 0, 1] (cor vermelha).

# 5. halign
# Descrição: Alinha o texto horizontalmente.
# Tipo: str
# Opções: "left", "center", "right", "justify"
# Exemplo: halign="center"

# 6. valign
# Descrição: Alinha o texto verticalmente.
# Tipo: str
# Opções: "top", "center", "bottom"
# Exemplo: valign="center"

# 7. line_height
# Descrição: Define o espaçamento entre as linhas de texto.
# Tipo: float
# Padrão: 1.5
# Exemplo: line_height=1.2

# 9. markup
# Descrição: Habilita ou desabilita a utilização de marcações no texto, como tags de cor e formatação de fonte.
# Tipo: bool
# Padrão: False
# Exemplo: markup=True


# Funcionalidade Geral:

# O MDFlatLabel é usado para exibir texto estilizado, respeitando as diretrizes do Material Design, em aplicações
# feitas com KivyMD. Ele permite uma apresentação clara e flexível de texto, que pode ser usado em botões, títulos,
# subtítulos, entre outros. As opções de personalização de alinhamento, estilo de fonte, cor e tamanho tornam o
# MDFlatLabel uma escolha útil para aplicações que buscam uma interface visual moderna e acessível.
