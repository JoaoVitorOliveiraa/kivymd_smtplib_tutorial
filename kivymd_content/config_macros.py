# ----- TIPOS DE FONTE DE TEXTO - STYLE -----                                   ----- COMBINAÇÕES POSSÍVEIS -----

DISPLAY_TEXT_STYLE = "Display"                                               # DISPLAY_STYLE  | LARGE_ROLE  | SIZE_57
HEADLINE_TEXT_STYLE = "Headline"                                             # DISPLAY_STYLE  | MEDIUM_ROLE | SIZE_45
TITLE_TEXT_STYLE = "Title"                                                   # DISPLAY_STYLE  | SMALL_ROLE  | SIZE_36
BODY_TEXT_STYLE = "Body"                                                     # HEADLINE_STYLE | LARGE_ROLE  | SIZE_32
LABEL_TEXT_STYLE = "Label"                                                   # HEADLINE_STYLE | MEDIUM_ROLE | SIZE_28
                                                                             # HEADLINE_STYLE | SMALL_ROLE  | SIZE_24
# ----- TIPOS DE FONTE DE TEXTO - ROLE -----                                 # TITLE_STYLE    | LARGE_ROLE  | SIZE_22
                                                                             # TITLE_STYLE    | MEDIUM_ROLE | SIZE_16
LARGE_TEXT_ROLE = "large"                                                    # TITLE_STYLE    | SMALL_ROLE  | SIZE_14
MEDIUM_TEXT_ROLE = "medium"                                                  # BODY_STYLE     | LARGE_ROLE  | SIZE_16
SMALL_TEXT_ROLE = "small"                                                    # BODY_STYLE     | MEDIUM_ROLE | SIZE_14
                                                                             # BODY_STYLE     | SMALL_ROLE  | SIZE_12
# ----- TIPOS DE FONTE DE TEXTO - FONT_SIZE -----                            # LABEL_STYLE    | LARGE_ROLE  | SIZE_14
                                                                             # LABEL_STYLE    | MEDIUM_ROLE | SIZE_12
SIZE_11 = 11                                                                 # LABEL_STYLE    | SMALL_ROLE  | SIZE_11
SIZE_12 = 12
SIZE_14 = 14
SIZE_16 = 16
SIZE_22 = 22
SIZE_24 = 24
SIZE_28 = 28
SIZE_32 = 32
SIZE_36 = 36
SIZE_45 = 45
SIZE_57 = 57


# ----- TIPOS DE COR DE TEXTO DA FUNÇÃO MDLABEL -----

PRIMARY = "Primary"
SECONDARY = "Secondary"
HINT = "Hint"
ERROR = "Error"
CUSTOM = "Custom"


# ----- TIPOS DE ESTILO DE BOTÃO DAS FUNÇÕES MDBUTTON E MDICONBUTTON -----

TEXT_BUTTON_STYLE = "text"
OUTLINED_BUTTON_STYLE = "outlined"
TONAL_BUTTON_STYLE = "tonal"
FILLED_BUTTON_STYLE = "filled"
ELEVATED_BUTTON_STYLE =  "elevated"


# ----- TIPOS DE ESTILO DE BOTÃO DA FUNÇÂO MDFABBUTTON -----

STANDARD_FAB_ICON_BUTTON_STYLE = "standard"
LARGE_FAB_BUTTON_STYLED = "large"
SMALL_FAB_BUTTON_STYLE = "small"
SURFACE_FAB_BUTTON_COLOR_MAP = "surface"
SECONDARY_FAB_BUTTON_COLOR_MAP = "secondary"
TERTIARY_FAB_BUTTON_COLOR_MAP = "tertiary"

# ----- CORES DO MANUAL DA MARCA DA FOR_CODE (NO FORMATO RGBA) -----

BRANCO = (1, 1, 1, 1)
AMARELO = (1, 1, 0, 1)
ROXO_CLARO = (97/255, 74/255, 211/255, 1)
ROXO_ESCURO = (30/255, 22/255, 71/255, 1)


# ----- CORES DIVERSAS -----

PRETO = (0, 0, 0, 1)
AZUL = (0, 0, 1, 1)
VERDE = (0, 1, 0, 1)
VERMELHO = (1, 0, 0, 1)
MARROM = (102/255, 51/255, 0, 1)


# ----- CORES DA PRIMARY_PALETTE -----

PALETA_VERMELHO = "Red"
PALETA_ROSA = "Pink"
PALETA_ROXO = "Purple"
PALETA_ROXO_ESCURO = "DeepPurple"
PALETA_INDIGO = "Indigo"
PALETA_AZUL = "Blue"
PALETA_AZUL_CLARO = "LightBlue"
PALETA_CIANO = "Cyan"
PALETA_AZUL_PETROLEO = "Teal"
PALETA_VERDE = "Green"
PALETA_VERDE_CLARO = "LightGreen"
PALETA_VERDE_LIMA = "Lime"
PALETA_AMARELO = "Yellow"
PALETA_AMBAR = "Amber"
PALETA_LARANJA = "Orange"
PALETA_LARANJA_ESCURO = "DeepOrange"
PALETA_MARROM = "Brown"
PALETA_CINZA = "Gray"
PALETA_AZUL_ACINZENTADO = "BlueGray"

#['Aliceblue', 'Antiquewhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanchedalmond', 'Blue',
# 'Blueviolet', 'Brown', 'Burlywood', 'Cadetblue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflowerblue', 'Cornsilk',
# 'Crimson', 'Cyan', 'Darkblue', 'Darkcyan', 'Darkgoldenrod', 'Darkgray', 'Darkgrey', 'Darkgreen', 'Darkkhaki',
# 'Darkmagenta', 'Darkolivegreen', 'Darkorange', 'Darkorchid', 'Darkred', 'Darksalmon', 'Darkseagreen',
# 'Darkslateblue', 'Darkslategray', 'Darkslategrey', 'Darkturquoise', 'Darkviolet', 'Deeppink', 'Deepskyblue',
# 'Dimgray', 'Dimgrey', 'Dodgerblue', 'Firebrick', 'Floralwhite', 'Forestgreen', 'Fuchsia', 'Gainsboro', 'Ghostwhite',
# 'Gold', 'Goldenrod', 'Gray', 'Grey', 'Green', 'Greenyellow', 'Honeydew', 'Hotpink', 'Indianred', 'Indigo', 'Ivory',
# 'Khaki', 'Lavender', 'Lavenderblush', 'Lawngreen', 'Lemonchiffon', 'Lightblue', 'Lightcoral', 'Lightcyan',
# 'Lightgoldenrodyellow', 'Lightgreen', 'Lightgray', 'Lightgrey', 'Lightpink', 'Lightsalmon', 'Lightseagreen',
# 'Lightskyblue', 'Lightslategray', 'Lightslategrey', 'Lightsteelblue', 'Lightyellow', 'Lime', 'Limegreen',
# 'Linen', 'Magenta', 'Maroon', 'Mediumaquamarine', 'Mediumblue', 'Mediumorchid', 'Mediumpurple', 'Mediumseagreen',
# 'Mediumslateblue', 'Mediumspringgreen', 'Mediumturquoise', 'Mediumvioletred', 'Midnightblue', 'Mintcream',
# 'Mistyrose', 'Moccasin', 'Navajowhite', 'Navy', 'Oldlace', 'Olive', 'Olivedrab', 'Orange', 'Orangered', 'Orchid',
# 'Palegoldenrod', 'Palegreen', 'Paleturquoise', 'Palevioletred', 'Papayawhip', 'Peachpuff', 'Peru', 'Pink', 'Plum',
# 'Powderblue', 'Purple', 'Red', 'Rosybrown', 'Royalblue', 'Saddlebrown', 'Salmon', 'Sandybrown', 'Seagreen', 'Seashell',
# 'Sienna', 'Silver', 'Skyblue', 'Slateblue', 'Slategray', 'Slategrey', 'Snow', 'Springgreen', 'Steelblue', 'Tan', 'Teal',
# 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'Whitesmoke', 'Yellow', 'Yellowgreen']


# ----- TONALIDADES DE COR DA PRIMARY_HUE -----

TOM_1 = "50"
TOM_2 = "100"
TOM_3 = "200"
TOM_4 = "300"
TOM_5 = "400"
TOM_6 = "500"
TOM_7 = "600"
TOM_8 = "700"
TOM_9 = "800"
TOM_10 = "900"
TOM_DESTAQUE_1 = "A100"
TOM_DESTAQUE_2 = "A200"
TOM_DESTAQUE_3 = "A400"
TOM_DESTAQUE_4 = "A700"


# ----- ESTILOS DE TEMA DA THEME_STYLE -----

TEMA_CLARO = "Light"
TEMA_ESCURO = "Dark"