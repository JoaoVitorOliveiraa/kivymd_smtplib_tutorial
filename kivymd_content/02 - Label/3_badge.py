# Arquivo de exemplo da função MDBadge.

from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivymd.uix.badge import MDBadge
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        icon_label = MDIcon(MDBadge(text = "12", bold = True),
                            icon = "gmail",                                     # Seleciona o ícone.
                            icon_color = ROXO_CLARO,                            # Cor do ícone em (r, g, b, a) ou formato de string.
                            pos_hint = {"center_x": 0.5, "center_y": 0.5})      # Posiciona o ícone na tela, neste caso no meio.

        return  icon_label  # Retorna o ícone.

MyApp().run()



#                               ----- DESCRIÇÃO DA FUNÇÃO MDBADGE -----

# MDBadge é um widget da biblioteca KivyMD que exibe uma pequena etiqueta,
# geralmente usada para mostrar contadores ou notificações sobre ícones ou botões.