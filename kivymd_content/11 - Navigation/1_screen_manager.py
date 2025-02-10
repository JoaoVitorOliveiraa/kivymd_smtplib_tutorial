# Arquivo de exemplo da função MDScreenManager.

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



#                               ----- Descrição do código -----

# A classe MDScreenManager é um gerenciador de telas do KivyMD que permite a troca dinâmica de diferentes telas dentro
# de um aplicativo, facilitando a navegação entre elas. Ela funciona de maneira semelhante a um gerenciador de layouts,
# mas com a adição de funcionalidades específicas para alternar entre diferentes "páginas" ou "telas" dentro da interface.

# Principais componentes e funcionalidades:

# MDScreenManager:
# É o contêiner principal que mantém o controle das telas. Ele permite que você alterne entre várias telas registradas.
# A troca entre telas é feita com base no valor da propriedade current, que indica qual tela está ativa.
# A mudança de tela pode ser realizada de forma programática, como no exemplo com a função trocar_tela().

# MDScreen:
# Cada tela dentro do MDScreenManager é representada por um MDScreen.
# Cada MDScreen tem propriedades como:
# name: Nome único da tela, que será utilizado para identificar e alternar entre telas.
# md_bg_color: Cor de fundo da tela.

# MDLabel:
# Usado para exibir texto na tela.
# A propriedade halign é utilizada para centralizar o texto, como no exemplo em que as telas têm a legenda "Tela 1" e "Tela 2".

# MDButton:
# Um botão que pode acionar ações. No exemplo, ele chama a função trocar_tela() ao ser pressionado, permitindo alternar entre "tela_1" e "tela_2".
# A propriedade pos_hint é usada para posicionar o botão no centro da tela.

# trocar_tela():
# Função definida na classe MyApp, responsável por alterar a tela ativa no MDScreenManager usando o nome da tela.
# Quando um botão é pressionado, ele chama essa função para alterar o valor da propriedade current do MDScreenManager, fazendo com que a tela muda.

# Resumo do Código:
# O código fornecido é um exemplo simples de um aplicativo KivyMD que usa MDScreenManager para alternar entre duas telas:
# Tela 1 (fundo azul) com um botão que alterna para a Tela 2.
# Tela 2 (fundo vermelho) com um botão que alterna de volta para a Tela 1.
# A troca de telas é realizada com a função trocar_tela(), que altera a tela ativa com base no nome da tela especificado.


#                               ----- Descrição do trecho "self.screen.current = nome_tela" -----

# No contexto do código fornecido, a linha self.screen.current = nome_tela é um ponto crucial para a troca dinâmica de
# telas dentro do MDScreenManager. Vamos analisar como ela funciona e qual o seu papel no processo de navegação:

# Objetivo da Linha:
# A linha self.screen.current = nome_tela altera a tela ativa exibida no MDScreenManager para aquela cujo nome foi
# passado como parâmetro na função trocar_tela(nome_tela).

# Passo a Passo do Funcionamento:
# O que é self.screen?
# self.screen é uma referência ao MDScreenManager carregado pela função Builder.load_string(screen_string).
# Este é o contêiner principal que mantém o controle de todas as telas definidas dentro dele (no caso, tela_1 e tela_2).

# O que é current?
# A propriedade current do MDScreenManager define qual tela está visível no momento.
# Ela armazena o nome da tela ativa, ou seja, o nome da tela que o MDScreenManager deve exibir.
# Por exemplo, se current for igual a "tela_1", o MDScreenManager exibirá a tela chamada tela_1.

# Por que self.screen.current = nome_tela funciona?
# Quando um botão é pressionado e a função trocar_tela(nome_tela) é chamada, o parâmetro nome_tela (como "tela_1" ou "tela_2") é passado para a função.
# Dentro da função, a linha self.screen.current = nome_tela define qual tela será exibida com base no valor de nome_tela.
# Se nome_tela for "tela_2", então a tela 2 será exibida, e o MDScreenManager vai trocar para essa tela.

# Como isso afeta a navegação?
# O current do MDScreenManager é uma maneira simples de alternar entre telas, já que ela automaticamente
# gerencia a troca de conteúdo visual dentro do seu contêiner. Ao definir o current para "tela_1", o MDScreenManager
# renderiza MDScreen(name="tela_1"), e quando ele é alterado para "tela_2", ele renderiza MDScreen(name="tela_2").

# Exemplo de Funcionamento no Código:

# Quando a tela_1 é exibida e o botão "Ir para Tela 2" é pressionado:
# O metodo on_release: app.trocar_tela("tela_2") é chamado.
# Na função trocar_tela(nome_tela), nome_tela é igual a "tela_2".
# A linha self.screen.current = nome_tela faz com que a tela ativa seja alterada para tela_2.

# Quando a tela_2 é exibida e o botão "Voltar para Tela 1" é pressionado:
# O metodo on_release: app.trocar_tela("tela_1") é chamado.
# Na função trocar_tela(nome_tela), nome_tela é igual a "tela_1".
# A linha self.screen.current = nome_tela faz com que a tela ativa seja alterada para tela_1.

# Conclusão:
# A linha self.screen.current = nome_tela é responsável por alterar a tela visível no MDScreenManager de forma dinâmica,
# ]utilizando o nome da tela como identificador. Esse mecanismo torna a navegação entre telas simples e eficiente dentro
# de um aplicativo que usa múltiplas telas, permitindo a troca de conteúdo com base nas ações do usuário.