# Arquivo de exemplo da função MDDivider.

from kivymd.app import MDApp
from kivy.lang import Builder

# screen_string = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDDivider:
#         size_hint_x: 0.5            # Ativado somente com orientation: "horizontal"
#         size_hint_y: 0.5            # Ativado somente com orientation: "vertical"
#         orientation: "vertical"
#         divider_width: 3
#         color: (97/255, 74/255, 211/255, 1)
#         pos_hint: {'center_x': .5, 'center_y': .5}
# '''
#
# class MyApp(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         self.screen = Builder.load_string(screen_string)
#         return self.screen
#
# MyApp().run()



#                               ----- Descrição da função MDDivider -----

# O MDDivider é um componente da biblioteca KivyMD que adiciona uma linha divisória horizontal ou vertical para
# separar elementos visuais em uma interface gráfica. Ele é útil para melhorar a organização e a estética do layout,
# separando seções dentro de um menu, lista ou qualquer outro conteúdo.

# Parâmetros:
# size_hint_x: Define a largura do divisor como uma fração da largura total da tela. Ativado apenas quando orientation for "horizontal".
# size_hint_y: Define a altura do divisor como uma fração da altura total da tela. Ativado apenas quando orientation for "vertical".
# orientation: Define a direção do divisor. Pode ser "horizontal" (linha na horizontal) ou "vertical" (linha na vertical).
# divider_width: Define a espessura (largura ou altura) do divisor em pixels.
# color: Define a cor do divisor no formato RGBA (Red, Green, Blue, Alpha).
# pos_hint: Define a posição do divisor na tela.
# on_orientation: metodo que é acionado automaticamente sempre que o valor do atributo orientation é alterado.


#                               ----- Código de exemplo para o teste do parâmetro "on_orientation" -----

screen_string = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDDivider:
        id: divider
        size_hint_x: 0.5            
        size_hint_y: 0.5            
        orientation: "vertical"
        divider_width: 3
        color: (97/255, 74/255, 211/255, 1)
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_orientation: print("for_code")                           # Imprime 

    MDButton:
        text: "Alternar Orientação"
        pos_hint: {"center_x": .5, "center_y": .2}
        on_release: app.alternar_orientacao(divider.orientation)
        
        MDButtonText:
            text: "Mudar orientação"
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

    def alternar_orientacao(self, orientation):
        "Função que alterna a orientação entre horizontal e vertical."

        divider = self.screen.ids.divider
        divider.orientation = "horizontal" if orientation == "vertical" else "vertical"

        if divider.orientation == "horizontal":
            divider.size_hint_x = 0.5
            divider.size_hint_y = None
        else:
            divider.size_hint_x = None
            divider.size_hint_y = 0.5

MyApp().run()