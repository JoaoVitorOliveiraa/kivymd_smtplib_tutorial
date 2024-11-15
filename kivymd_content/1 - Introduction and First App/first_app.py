# Arquivo de exemplo de como criar um App.

# Importação da Classe MDApp, que é uma extensão da classe App do Kivy.
from kivymd.app import MDApp

# O aplicativo BatComputer herda de MDApp.
class MyApp(MDApp):

    # Metodo build é um especial e obrigatório para qualquer aplicativo, e ele define a interface principal da aplicação.
    # Esse metodo é chamado automaticamente pelo Kivy (ou KivyMD) assim que o aplicativo é iniciado, e seu propósito
    # é criar e retornar o layout principal do aplicativo, que será exibido na tela.
    def build(self):
        "Função que cria o App."

        return

# Roda o App.
MyApp().run()