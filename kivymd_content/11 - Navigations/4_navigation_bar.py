# Arquivo de exemplo da função MDNavigationBar.

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
#
#             MDNavigationItemLabel:
#                 text: "Screen 1"
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