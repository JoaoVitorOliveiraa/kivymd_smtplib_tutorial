# Arquivo de exemplo da função MDList.

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_smtplib_tutorial.kivymd_content.config_macros import *

screen_string = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    
    MDList:
        size_hint_x: 0.9
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        MDListItem:
            on_release: print("Primeiro Item da Lista")

            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho one-line e ícone na esquerda"
                font_style: "Label"
                role: "large"
                font_size: 14
                theme_text_color: "Custom"
                text_color: (0, 0, 1, 1)
            
            MDListItemLeadingIcon:
                icon: "account"
                theme_icon_color: "Custom"
                icon_color: (1, 0, 0, 1)
                pos_hint: {"center_y": 0.5}
        
        
        MDListItem:
            on_release: print("Segundo Item da Lista")
            
            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho one-line e ícone na direita"
                font_style: "Label"
            
            MDListItemTrailingIcon:
                icon: "timer-remove"
                theme_icon_color: "Custom"
                icon_color: (0, 0, 0, 1)
        
        
        MDListItem:
            on_release: print("Terceiro Item da Lista")
        
            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho one-line e checkbox na direita"
                font_style: "Label"
                            
            MDListItemTrailingCheckbox:


        MDListItem:
            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho one-line e texto na direita"
                font_style: "Label"
                            
            MDListItemTrailingSupportingText:
                text: "Este é o texto da direita"
                
        
        MDListItem:
            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho one-line e avatar na esquerda"
                font_style: "Label"
                            
            MDListItemLeadingAvatar:
                source: "Mel.jpg"
                size_hint_y: 1
                radius: "36dp"

                
        MDListItem:
            line_color: (97/255, 74/255, 211/255, 1)
            
            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho two-line e cor nas bordas"
                font_style: "Label"
            
            MDListItemSupportingText:
                text: "Este é o texto de suporte"
                
                
        MDListItem:
            divider: True
            theme_divider_color: "Custom"
            divider_color: (1, 0, 1, 1)
            
            MDListItemHeadlineText:
                text: "Utilização da MDListItem com tamanho three-line e linha de divisão colorida"
                font_style: "Label"
            
            MDListItemSupportingText:
                text: "Este é o texto de suporte"
            
            MDListItemTertiaryText:
                text: "Este é o terceiro texto"
'''

class MyApp(MDApp):
    def build(self):
        "Função que cria o App."

        self.theme_cls.primary_palette = PALETA_AZUL
        self.theme_cls.theme_style = TEMA_CLARO

        screen = Builder.load_string(screen_string)
        return screen

MyApp().run()



#                               ----- Descrição das funções -----

# MDList: Um container usado para criar listas verticais seguindo os padrões do Material Design.
# Uso: Agrupa itens de lista como MDListItem para criar uma estrutura ordenada.

# MDListItem: Um item básico de lista com texto principal e suporte para widgets adicionais.
# Uso: Base para criar elementos clicáveis ou não em uma lista.

# MDListItemLeadingIcon: Um ícone posicionado no início de um item de lista.
# Uso: Adiciona contexto visual ao item.

# MDListItemTrailingIcon: Um ícone posicionado no final de um item de lista.
# Uso: Pode indicar ações ou estados do item.

# MDListItemHeadlineText: Texto principal destacado no item de lista.
# Uso: Utilizado para enfatizar o conteúdo principal.

# MDListItemTertiaryText: Um terceiro nível de texto no item de lista (menos destacado).
# Uso: Complementa o texto principal com informações adicionais.

# MDListItemLeadingAvatar: Adiciona um avatar (imagem ou ícone) na posição inicial do item.
# Uso: Representa visualmente o item com uma imagem associada.

# MDListItemSupportingText: Texto de suporte que aparece abaixo do texto principal no item de lista.
# Uso: Fornece informações detalhadas sobre o item.

# MDListItemTrailingCheckbox: Checkbox posicionado no final do item de lista.
# Uso: Permite interatividade como seleção ou marcação.

# MDListItemTrailingSupportingText: Texto de suporte posicionado no final do item de lista.
# Uso: Adiciona contexto ou informações extras alinhadas à direita.


#                           ----- Parâmetros da função MDListItem -----

# ['_background_origin', '_background_x', '_background_y', '_doing_ripple', '_fading_out', '_finishing_ripple',
# '_md_bg_color', '_ripple_rad', '_round_rad', 'always_release', 'angle', 'background', 'background_origin',
# 'button_elevated_opacity_value_disabled_container', 'button_elevated_opacity_value_disabled_icon',
# 'button_elevated_opacity_value_disabled_text', 'button_filled_opacity_value_disabled_container',
# 'button_filled_opacity_value_disabled_icon', 'button_filled_opacity_value_disabled_text',
# 'button_outlined_opacity_value_disabled_container', 'button_outlined_opacity_value_disabled_icon',
# 'button_outlined_opacity_value_disabled_line', 'button_outlined_opacity_value_disabled_text',
# 'button_text_opacity_value_disabled_icon', 'button_text_opacity_value_disabled_text',
# 'button_tonal_opacity_value_disabled_container', 'button_tonal_opacity_value_disabled_icon',
# 'button_tonal_opacity_value_disabled_text', 'card_filled_opacity_value_disabled_state_container',
# 'card_opacity_value_disabled_state_elevated_container', 'card_outlined_opacity_value_disabled_state_container',
# 'center', 'center_x', 'center_y', 'checkbox_opacity_value_disabled_container', 'children',
# 'chip_opacity_value_disabled_container', 'chip_opacity_value_disabled_icon', 'chip_opacity_value_disabled_text',
# 'cls', 'detect_visible', 'device_ios', 'disabled', 'divider', 'divider_color', 'enter_point',
# 'fab_button_opacity_value_disabled_container', 'fab_button_opacity_value_disabled_icon', 'focus_behavior',
# 'focus_color', 'height', 'hover_visible', 'hovering', 'icon_button_filled_opacity_value_disabled_container',
# 'icon_button_filled_opacity_value_disabled_icon', 'icon_button_outlined_opacity_value_disabled_container',
# 'icon_button_outlined_opacity_value_disabled_icon', 'icon_button_outlined_opacity_value_disabled_line',
# 'icon_button_standard_opacity_value_disabled_icon', 'icon_button_tonal_opacity_value_disabled_container',
# 'icon_button_tonal_opacity_value_disabled_icon', 'id', 'ids', 'label_opacity_value_disabled_text', 'last_touch',
# 'line_color', 'line_width', 'list_opacity_value_disabled_container', 'list_opacity_value_disabled_leading_avatar',
# 'md_bg_color', 'md_bg_color_disabled', 'min_state_time', 'minimum_height', 'minimum_size', 'minimum_width',
# 'motion_filter', 'opacity', 'orientation', 'padding', 'parent', 'pos', 'pos_hint', 'radius', 'right', 'ripple_alpha',
# 'ripple_canvas_after', 'ripple_color', 'ripple_duration_in_fast', 'ripple_duration_in_slow', 'ripple_duration_out',
# 'ripple_effect', 'ripple_func_in', 'ripple_func_out', 'ripple_rad_default', 'ripple_scale',
# 'segmented_button_opacity_value_disabled_container', 'segmented_button_opacity_value_disabled_container_active',
# 'segmented_button_opacity_value_disabled_icon', 'segmented_button_opacity_value_disabled_line',
# 'segmented_button_opacity_value_disabled_text', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x',
# 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'spacing',
# 'state', 'state_drag', 'state_hover', 'state_layer_color', 'state_press', 'switch_opacity_value_disabled_container',
# 'switch_opacity_value_disabled_icon', 'switch_opacity_value_disabled_line', 'switch_thumb_opacity_value_disabled_container',
# 'text_field_filled_opacity_value_disabled_state_container', 'text_field_opacity_value_disabled_helper_text_label',
# 'text_field_opacity_value_disabled_hint_text_label', 'text_field_opacity_value_disabled_leading_icon',
# 'text_field_opacity_value_disabled_line', 'text_field_opacity_value_disabled_max_length_label',
# 'text_field_opacity_value_disabled_trailing_icon', 'text_field_outlined_opacity_value_disabled_state_container',
# 'theme_bg_color', 'theme_cls', 'theme_divider_color', 'theme_elevation_level', 'theme_focus_color', 'theme_font_name',
# 'theme_font_size', 'theme_height', 'theme_icon_color', 'theme_line_color', 'theme_line_height', 'theme_shadow_color',
# 'theme_shadow_offset', 'theme_shadow_softness', 'theme_text_color', 'theme_width', 'top', 'unfocus_color', 'width', 'x', 'y']