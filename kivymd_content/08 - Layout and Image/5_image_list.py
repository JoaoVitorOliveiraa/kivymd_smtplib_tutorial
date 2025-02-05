# Arquivo de exemplo da função MDSmartTile.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDSmartTile:
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        size: "320dp", "320dp"
        overlap: True
        overlay_mode: "footer"

        MDSmartTileImage:
            source: "../07 - List/Mel.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]

        MDSmartTileOverlayContainer:
            md_bg_color: (97/255, 74/255, 211/255, 1)
            radius: [0, 0, dp(24), dp(24)]
            adaptive_height: True
            padding: "8dp"
            spacing: "8dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": .5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            MDLabel:
                text: "Mel"
                theme_text_color: "Custom"
                text_color: "white"
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()



#                              ----- Descrição da função MDSmartTile -----

# MDSmartTile é um widget do KivyMD (Kivy Material Design) que funciona como um bloco interativo e elegante.
# Ele combina diferentes elementos de UI (interface do usuário) dentro de um único tile (bloco) e pode ser
# usado para exibir imagens, textos, ícones, entre outros, com estilo e funcionalidades avançadas.

# Características do MDSmartTile:
# Ele é projetado para ser flexível e interativo, permitindo a combinação de uma imagem de fundo (ou conteúdo visual), uma sobreposição (overlay)
# e outros componentes (como ícones e textos).
# A sobreposição (MDSmartTileOverlayContainer) é geralmente usada para criar uma camada sobre a imagem para exibir informações adicionais ou botões.
# MDSmartTile pode ser personalizado em termos de tamanho, forma, sobreposição e animações, tornando-o uma escolha popular para exibir cartões interativos ou blocos de conteúdo.


#                              ----- Descrição do código -----

# MDScreen:
# Define um MDScreen (tela) onde o conteúdo será exibido.
# O parâmetro md_bg_color: self.theme_cls.backgroundColor define a cor de fundo da tela para a cor de fundo do tema atual.

# MDSmartTile:
# O widget MDSmartTile é criado no centro da tela, usando pos_hint: {"center_x": .5, "center_y": .5}, o que o coloca centralizado.
# size_hint: None, None significa que o tamanho não é ajustado automaticamente com base no layout, e o tamanho será definido manualmente com a propriedade size.
# size: "320dp", "320dp" define o tamanho fixo do tile como 320x320 dp (density-independent pixels), garantindo uma boa escala em diferentes dispositivos.
# overlap = False: A sobreposição será parcial, ou seja, ela não cobrará toda a área da imagem. A imagem ainda será visível nas áreas não cobertas pela sobreposição.
# overlap = True: A sobreposição cobrirá toda a área do tile, fazendo com que o conteúdo da imagem fique oculto atrás da sobreposição, permitindo que apenas os elementos da sobreposição (como ícones, texto ou botões) sejam visíveis.
# overlay_mode: determina se a caixa de informações (overlay) se comporta como um cabeçalho (header) ou um rodapé (footer) da imagem no tile.

# MDSmartTileImage:
# A imagem dentro do MDSmartTile é definida com a propriedade source: "../07 - List/Mel.jpg", especificando o caminho da imagem a ser exibida.
# A propriedade radius: [dp(24), dp(24), dp(24), dp(24)] define o raio de arredondamento dos cantos da imagem, criando bordas arredondadas.

# MDSmartTileOverlayContainer:
# A sobreposição (overlay) é um contêiner dentro do MDSmartTile que cobre parte da imagem para exibir outros elementos.
# md_bg_color: (97/255, 74/255, 211/255, 1) define a cor de fundo da sobreposição, usando um valor RGBA (97/255, 74/255, 211/255, 1) para um tom roxo.
# radius: [0, 0, dp(24), dp(24)] cria bordas arredondadas nos cantos inferiores do container da sobreposição.
# adaptive_height: True faz com que a altura da sobreposição seja ajustada automaticamente conforme o conteúdo.
# padding: "8dp" e spacing: "8dp" adicionam espaçamento dentro do container para os itens (como ícones e texto) que estarão dentro da sobreposição.

# MDIconButton:
# Dentro da sobreposição, há um botão de ícone (MDIconButton) que exibe um ícone de coração.
# icon: "heart-outline" define o ícone inicial como "coração vazio".
# theme_icon_color: "Custom" e icon_color: 1, 0, 0, 1 definem a cor do ícone como vermelha.
# pos_hint: {"center_y": .5} posiciona o ícone verticalmente no centro da sobreposição.
# on_release: é um evento que ocorre quando o botão é pressionado. O código dentro da função on_release alterna o ícone entre "coração vazio" ("heart-outline") e "coração preenchido" ("heart"), criando um efeito de mudança de estado visual.

# MDLabel:
# A label dentro da sobreposição exibe o nome "Mel".
# theme_text_color: "Custom" permite personalizar a cor do texto.
# text_color: "white" define a cor do texto como branca.