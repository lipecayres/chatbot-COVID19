import menu

def places():
    print()
    print("Você quer saber sobre testagem ou vacinação?")
    print()
    print("1- Testagem")
    print("2- Vacinação")
    print()

    cursor = menu.intEntry()

    if cursor == 1:
        print()
        print("Você consegue acompanhar diariamente no card da Secretaria de Saúde e da Prefeitura no instagram!")
        print("Confere lá:")
        print()
        print("Secretaria @smssalvador")
        print("Prefeitura: @prefsalvador")
        print()
        print()
        menu.endChat()

    elif cursor == 2:
        print()
        print("Aqui o link de acompanhamento de vacinação em Salvador")
        print("Fique atento ao filômetro, vai te ajudar muito a evitar aglomerações")
        print()
        print("http://www.saude.salvador.ba.gov.br/vacinacao-covid/")
        print()
        print()
        menu.endChat()

    else:
        print()
        print("Resposta inválida. Vamos tentar de novo!")
        places()