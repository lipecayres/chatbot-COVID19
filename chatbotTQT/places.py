from chatbotCOVID19.chatbotTQT.menu import intEntry
import menu

def places():
    print()
    print("Você quer saber sobre testagem ou vacinação?")
    print()
    print()
    print("1- Testagem")
    print("2- Vacinação")

    cursor = intEntry()

    if cursor == 1:
        print()
        print("Você consegue acompanhar diariamente no card da Secretaria de Saúde e da Prefeitura no instagram!")
        print("Confere lá:")
        print("Secretaria @smssalvador")
        print("Prefeitura: @prefsalvador")
        print()
        menu.endChat()

    elif cursor == 2:
        print()
        print("Aqui o link de acompanhamento de vacinação em Salvador")
        print("Fique atento ao filômetro, vai te ajudar muito a evitar aglomerações")
        print()
        print("http://www.saude.salvador.ba.gov.br/vacinacao-covid/")
        print()
        menu.endChat()

    else:
        print("Resposta inválida. Vamos tentar de novo!")
        places()