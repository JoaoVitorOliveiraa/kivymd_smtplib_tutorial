# Arquivo de exemplo da função MDIcon.

from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        icon_label = MDIcon(icon = "language-python",                           # Seleciona o ícone.
                            icon_color = ROXO_CLARO,                            # Cor do ícone em (r, g, b, a) ou formato de string.
                            pos_hint = {"center_x": 0.5, "center_y": 0.5})      # Posiciona o ícone na tela, neste caso no meio.

        return  icon_label  # Retorna o ícone.

MyApp().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDICON -----

# O MDIcon no KivyMD é um widget utilizado para exibir ícones de acordo com o padrão Material Design. Ele é ideal para
# ícones estilizados e facilmente personalizáveis que se integram com outros componentes de uma interface, como botões
# e rótulos. Este widget usa ícones de uma coleção chamada "Material Design Icons" (MDI), que inclui uma grande
# variedade de ícones prontos para uso.

# Aqui estão os principais parâmetros e propriedades de MDIcon:

# 1. icon
# Descrição: Define o nome do ícone a ser exibido. Esse nome deve corresponder a um ícone existente na coleção de ícones MDI.
# Tipo: str
# Padrão: "android"
# Exemplo: icon="home"

# 2. theme_text_color
# Descrição: Define a cor do ícone com base no tema atual da aplicação, alinhado com o Material Design.
# Tipo: str
# Opções: "Primary", "Secondary", "Hint", "Error", "Custom"
# Padrão: "Primary"
# Exemplo: theme_text_color="Secondary"

# 3. text_color
# Descrição: Define uma cor personalizada para o ícone. Este valor é aplicado apenas quando theme_text_color está definido como "Custom".
# Tipo: Lista ou tupla de quatro valores (RGBA).
# Exemplo: text_color=[0.2, 0.6, 0.8, 1] (um tom de azul).

# 4. font_size
# Descrição: Define o tamanho do ícone.
# Tipo: int ou float
# Padrão: 24 (tamanho padrão em pixels, definido pelo Material Design)
# Exemplo: font_size=36

# 5. halign
# Descrição: Alinha o ícone horizontalmente dentro de seu contêiner.
# Tipo: str
# Opções: "left", "center", "right"
# Padrão: "center"
# Exemplo: halign="right"

# 6. opposite_colors
# Descrição: Alterna automaticamente entre o tema escuro e claro para o ícone com base no tema
# de fundo. Se o tema do aplicativo for claro, opposite_colors faz o ícone escuro, e vice-versa.
# Tipo: bool
# Padrão: False
# Exemplo: opposite_colors=True

# 7. disabled
# Descrição: Desabilita a exibição do ícone, tornando-o visualmente opaco e inacessível.
# Tipo: bool
# Padrão: False
# Exemplo: disabled=True


# Funcionalidade Geral:

# O MDIcon é ideal para exibir ícones estilizados de acordo com o padrão Material Design e pode ser utilizado em uma
# variedade de contextos, como em botões de navegação, indicações de status e outros elementos da interface gráfica.
# Com opções para personalização de cor, alinhamento e tamanho, MDIcon permite que você mantenha a consistência do
# design da aplicação, garantindo uma integração suave com outros elementos visuais.
