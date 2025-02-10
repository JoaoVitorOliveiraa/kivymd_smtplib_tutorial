# Arquivo de exemplo da função MDDivider.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDDivider:
        size_hint_x: 0.5            # Ativado somente com orientation: "horizontal"
        size_hint_y: 0.5            # Ativado somente com orientation: "vertical"
        orientation: "vertical"
        divider_width: 3
        color: (97/255, 74/255, 211/255, 1)
        pos_hint: {'center_x': .5, 'center_y': .5}
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

MyApp().run()



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

# screen_string = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDDivider:
#         id: divider
#         size_hint_x: 0.5
#         size_hint_y: 0.5
#         orientation: "vertical"
#         divider_width: 3
#         color: (97/255, 74/255, 211/255, 1)
#         pos_hint: {'center_x': .5, 'center_y': .5}
#         on_orientation: print("for_code")                           # Imprime
#
#     MDButton:
#         text: "Alternar Orientação"
#         pos_hint: {"center_x": .5, "center_y": .2}
#         on_release: app.change_orientation(divider.orientation)
#
#         MDButtonText:
#             text: "Mudar orientação"
# '''
#
# class MyApp(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         self.screen = Builder.load_string(screen_string)
#         return self.screen
#
#     def change_orientation(self, orientation):
#         "Função que alterna a orientação entre horizontal e vertical."
#
#         divider = self.screen.ids.divider
#         divider.orientation = "horizontal" if orientation == "vertical" else "vertical"
#
#         if divider.orientation == "horizontal":
#             divider.size_hint_x = 0.5
#             divider.size_hint_y = None
#         else:
#             divider.size_hint_x = None
#             divider.size_hint_y = 0.5
#
# MyApp().run()


# 1. on_release
# on_release → Este evento é acionado quando o botão é solto (clicado e liberado).
# app.alternar_orientacao(divider.orientation) → Chama o metodo alternar_orientacao() dentro da classe MyApp,
# passando como argumento o valor atual da propriedade orientation do MDDivider.

# Fluxo do evento:
# O usuário clica no botão "Mudar orientação".
# O evento on_release dispara a função app.alternar_orientacao(), enviando o valor da orientation atual do divisor (divider.orientation).
# O metodo alternar_orientacao() é executado para modificar a orientação do divisor.

# 2. on_orientation
# on_orientation é um evento disparado automaticamente sempre que a propriedade orientation do MDDivider mudar.
# Quando a orientation muda de "vertical" para "horizontal" ou vice-versa, on_orientation imprime "for_code" no console.

# 3. Metodo alternar_orientacao()
# Obtém a referência ao divisor → divider = self.screen.ids.divider
# Alterna a orientação
# Se a orientation atual for "vertical", muda para "horizontal".
# Se for "horizontal", muda para "vertical".
# Ajusta o tamanho (size_hint_x e size_hint_y) com base na nova orientação
# "horizontal" → Define size_hint_x = 0.5 e size_hint_y = None
# "vertical" → Define size_hint_x = None e size_hint_y = 0.5
# Resumo:
# O metodo troca a orientação e ajusta o tamanho do divisor conforme necessário.
# Ele é chamado pelo on_release do botão quando o usuário clica.

# Fluxo Completo do Código
# O usuário clica no botão "Mudar orientação".
# on_release chama app.alternar_orientacao(divider.orientation).
# alternar_orientacao() alterna a orientação e ajusta os tamanhos do divisor.
# on_orientation imprime "for_code" no console sempre que a propriedade muda.