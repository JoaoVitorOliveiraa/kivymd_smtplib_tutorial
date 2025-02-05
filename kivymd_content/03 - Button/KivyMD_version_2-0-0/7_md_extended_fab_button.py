# Arquivo de exemplo da função MDExtendedFabButton.

from kivymd.app import MDApp
from kivy.lang import Builder

screen_string = """
MDScreen:
    MDExtendedFabButton:
        id: btn
        theme_bg_color: "Custom"
        md_bg_color: (1, 0, 0, 1)
        size_hint: None, None
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        fab_state: "expand"

        MDExtendedFabButtonIcon:
            icon: "pencil-outline"
            theme_icon_color: "Custom"
            icon_color: (1, 1, 0, 1)

        MDExtendedFabButtonText:
            text: "Aperte"
"""
        # radius: [self.height / 2]     Arredonda o botão.

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()


# from kivy.lang import Builder
#
# from kivymd.app import MDApp
#
# KV = '''
# MDScreen:
#     md_bg_color: app.theme_cls.surfaceColor
#     on_touch_down:
#         if not btn.collide_point(*args[1].pos): \
#         btn.fab_state = "expand" \
#         if btn.fab_state == "collapse" else "collapse"
#
#         MDExtendedFabButton:
#             id: btn
#             pos_hint: {"center_x": .5, "center_y": .5}
#
#             MDExtendedFabButtonIcon:
#                 icon: "pencil-outline"
#
#             MDExtendedFabButtonText:
#                 text: "Compose"
# '''
#
#
# class Example(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Green"
#         return Builder.load_string(KV)
#
#
# Example().run()