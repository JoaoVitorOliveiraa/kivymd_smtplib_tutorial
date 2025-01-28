# Arquivo de exemplo da função MDTopAppBar.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = '''
MDScreenManager:
    id: screen_manager
    
    MDScreen:
        name: "tela_1"
        md_bg_color: "blue"

        MDLabel:
            text: "Tela 1"
            halign: "center"

        MDButton:
            on_release: app.trocar_tela("tela_2")
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            
            MDButtonText:
                text: "Ir para Tela 2"
                
    MDScreen:
        name: "tela_2"
        md_bg_color: "red"

        MDLabel:
            text: "Tela 2"
            halign: "center"

        MDButton:
            on_release: app.trocar_tela("tela_1")
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            
            MDButtonText:
                text: "Voltar para Tela 1"
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

    def trocar_tela(self, nome_tela):
        "Função que troca a tela usando o nome registrado."

        self.screen.current = nome_tela

MyApp().run()