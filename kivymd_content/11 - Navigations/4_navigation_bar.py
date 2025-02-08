# Arquivo de exemplo da função MDNavigationBar.
# Obs: No final do arquivo, há uma versão do código que não utiliza orientação a objetos.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem

screen_string = '''
<BaseMDNavigationItem>
    MDNavigationItemIcon:
        icon: root.icon

    MDNavigationItemLabel:
        text: root.text


<BaseScreen>
    FitImage:
        source: f"https://picsum.photos/{root.image_size}/{root.image_size}"
        size_hint: .9, .9
        pos_hint: {"center_x": .5, "center_y": .5}
        radius: dp(24)


MDBoxLayout:
    orientation: "vertical"
    md_bg_color: self.theme_cls.backgroundColor

    MDScreenManager:
        id: screen_manager

        BaseScreen:
            name: "Screen 1"
            image_size: "1024"

        BaseScreen:
            name: "Screen 2"
            image_size: "800"

        BaseScreen:
            name: "Screen 3"
            image_size: "600"


    MDNavigationBar:
        on_switch_tabs: app.on_switch_tabs(*args)

        BaseMDNavigationItem
            icon: "gmail"
            text: "Screen 1"
            active: True

        BaseMDNavigationItem
            icon: "twitter"
            text: "Screen 2"

        BaseMDNavigationItem
            icon: "linkedin"
            text: "Screen 3"
'''

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()
    indicator_color = (1, 1, 0, 1)
    indicator_duration = 0.5

class BaseScreen(MDScreen):
    image_size = StringProperty()

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.screen = Builder.load_string(screen_string)
        return self.screen

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text


MyApp().run()



#                               ----- Descrição do código acima -----

# --> Criando um item de navegação reutilizável
# BaseMDNavigationItem é uma subclasse de MDNavigationItem que pode ser reutilizada.
# MDNavigationItemIcon define o ícone do item.
# MDNavigationItemLabel define o texto do item.
# O código root.icon e root.text indica que os valores serão definidos dinamicamente na classe Python BaseMDNavigationItem.

# --> Criando uma tela reutilizável
# BaseScreen é uma subclasse de MDScreen.
# FitImage exibe uma imagem dinâmica da internet.
# source usa o valor de image_size definido na classe Python BaseScreen.

# --> Criando a estrutura principal do aplicativo
# MDBoxLayout organiza os elementos verticalmente.
# md_bg_color: self.theme_cls.backgroundColor usa a cor do tema do app.

# --> Criando o gerenciador de telas (MDScreenManager)
# MDScreenManager gerencia as telas do app.
# Ele contém três telas (BaseScreen), cada uma com um tamanho de imagem diferente.
# name: "Screen 1" define o nome da tela, que será usado para alternar entre elas.

# --> Criando a barra de navegação (MDNavigationBar)
# MDNavigationBar adiciona a barra de navegação na parte inferior.
# on_switch_tabs: app.on_switch_tabs(*args) → Chama a função on_switch_tabs quando um botão for pressionado.
# BaseMDNavigationItem é usado para criar os botões da barra de navegação:
# icon: "gmail" → Ícone do Gmail para a Tela 1
# text: "Screen 1" → Nome da tela associada ao botão
# active: True → Define este item como ativo por padrão

# --> Criando a classe do item de navegação
# BaseMDNavigationItem é uma subclasse de MDNavigationItem.
# StringProperty() permite definir os valores de icon e text diretamente no KV Language.
# indicator_color = (1, 1, 0, 1) define a cor do indicador ativo (amarelo).
# indicator_duration = 0.5 define a duração da animação do indicador.

# --> Criando a classe de tela reutilizável
# BaseScreen herda de MDScreen.
# image_size = StringProperty() permite que o tamanho da imagem seja definido dinamicamente.

# --> Criando a classe principal do aplicativo
# MyApp herda de MDApp (classe base para apps KivyMD).
# build(self) constrói a interface carregando screen_string com Builder.load_string()

# --> Criando a função para trocar de tela
# Essa função é chamada automaticamente quando um botão da MDNavigationBar é pressionado.
# bar: MDNavigationBar → Representa a barra de navegação.
# item: MDNavigationItem → Representa o botão pressionado.
# item_text: str → Contém o nome da tela associada ao botão.
# self.root.ids.screen_manager.current = item_text → Muda para a tela correspondente.



#                               ----- Descrição da função MDNavigationBar -----

# MDNavigationBar
# Função: Cria uma barra de navegação inferior com itens interativos.
# Uso: Permite a navegação entre telas ou seções do aplicativo.
# Principais Propriedades:
# on_switch_tabs: Aciona uma função ao trocar de item.

# MDNavigationItem
# Função: Representa um item dentro do MDNavigationBar.
# Uso: Cada item pode ter um ícone e um rótulo.
# Principais Propriedades:
# id: Cria uma referência única para o item dentro do arquivo KV.
# name: Define o nome do item no MDNavigationBar.
# indicator_color: Define a cor do indicador (barra ou marcação que aparece no item ativo).
# indicator_duration: Define o tempo de animação (duração) da transição do indicador ao trocar de item.

# MDNavigationItemIcon
# Função: Define o ícone dentro de um MDNavigationItem.
# Uso: Personaliza a aparência do ícone no menu inferior.
# Principais Propriedades: As mesmas da função MDIcon

# MDNavigationItemLabel
# Função: Define o texto do item de navegação.
# Uso: Exibe um rótulo abaixo do ícone.
# Principais Propriedades: As mesmas da função MDLabel.



#                               ----- Exemplo de código que não utiliza orientação a objetos -----

# screen_string = '''
# MDBoxLayout:
#     id: box
#     orientation: "vertical"
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDScreenManager:
#         id: screen_manager
#
#         MDScreen:
#             name: "Screen 1"
#
#             FitImage:
#                 source: f"https://picsum.photos/{1024}/{1024}"
#                 size_hint: (0.9, 0.9)
#                 pos_hint: {"center_x": 0.5, "center_y": 0.5}
#                 radius: dp(24)
#
#
#         MDScreen:
#             name: "Screen 2"
#
#             FitImage:
#                 source: f"https://picsum.photos/{800}/{800}"
#                 size_hint: (0.9, 0.9)
#                 pos_hint: {"center_x": 0.5, "center_y": 0.5}
#                 radius: dp(24)
#
#
#         MDScreen:
#             name: "Screen 3"
#
#             FitImage:
#                 source: f"https://picsum.photos/{600}/{600}"
#                 size_hint: (0.9, 0.9)
#                 pos_hint: {"center_x": 0.5, "center_y": 0.5}
#                 radius: dp(24)
#
#     MDNavigationBar:
#         on_switch_tabs: app.on_switch_tabs(*args)
#
#         MDNavigationItem:
#             id: item1
#             name: "Screen 1"
#             indicator_color: (1, 1, 0, 1)
#             indicator_duration: 0.5
#
#             MDNavigationItemIcon:
#                 icon: "gmail"
#                 icon_color: (0, 1, 0, 1)
#
#             MDNavigationItemLabel:
#                 text: "Screen 1"
#                 bold: True
#                 italic: True
#
#         MDNavigationItem:
#             id: item2
#             name: "Screen 2"
#             indicator_color: (1, 1, 0, 1)
#             indicator_duration: 0.5
#
#             MDNavigationItemIcon:
#                 icon: "twitter"
#
#             MDNavigationItemLabel:
#                 text: "Screen 2"
#                 font_style: "Title"
#                 role: "large"
#                 font_size: 22
#
#         MDNavigationItem:
#             id: item3
#             name: "Screen 3"
#             indicator_color: (1, 1, 0, 1)
#             indicator_duration: 0.5
#
#             MDNavigationItemIcon:
#                 icon: "linkedin"
#
#             MDNavigationItemLabel:
#                 text: "Screen 3"
#                 theme_text_color: "Custom"
#                 text_color: (97/255, 74/255, 211/255, 1)
# '''
#
#
# class MyApp(MDApp):
#     def build(self):
#         "Função que cria o App."
#
#         self.screen = Builder.load_string(screen_string)
#         return self.screen
#
#     def on_switch_tabs(self, instance_navigation_bar, instance_item, *args):
#         """Muda para a tela correspondente ao item do Navigation Bar."""
#         screen_name = instance_item.name  # Usa a propriedade 'name' do item de navegação
#         self.root.ids.screen_manager.current = screen_name  # Define a tela ativa
#
# MyApp().run()


# Barra de navegação (MDNavigationBar)
# MDNavigationBar: adiciona uma barra de navegação na parte inferior.
# on_switch_tabs: app.on_switch_tabs(*args)
# Isso define uma ação para quando um botão for pressionado.
# app.on_switch_tabs(*args) chama a função on_switch_tabs da classe MyApp.
# O *args permite que todos os argumentos necessários sejam passados corretamente.

# Função on_switch_tabs
# Essa função troca de tela quando um botão da MDNavigationBar é pressionado.
# instance_navigation_bar → Representa a MDNavigationBar.
# instance_item → Representa o botão pressionado (MDNavigationItem).
# instance_item.name → Obtém o nome da tela associada ao botão.
# self.root.ids.screen_manager.current = screen_name → Define a tela ativa no MDScreenManager.
# O *args permite que todos os argumentos necessários sejam passados corretamente.