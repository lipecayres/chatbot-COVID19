import menu

def survey():
    print("Está com sintomas da COVID-19 (febre, coriza, dor no corpo, cansaço, dor na garganta)?")
    print()
    print("1- Sim")
    print("2- Não")

    cursor = menu.intEntry()
    if cursor == 1:
        print()
        print("Há quanto tempo?")
        print()
        print("1- De 1 a 3 dias")
        print("2- Mais de 3 dias")

        cursor = menu.intEntry()
        if cursor == 1:
            print()
            print("Segundo o Ministério da Saúde, o adequado é realizar a testagem entre 3 a 7 dias.")
            print("Aguarda o prazo e fala comigo de novo!")
            menu.endChat()

        elif cursor == 2:
            print("Por favor, dirija-se para uma unidade de saúde e faça seu teste de COVID-19")
            print("Aqui você pode encontrar os locais disponíveis para testagem:")
            menu.places()

        else:
            print("Resposta inválida. Vamos tentar de novo!")
            survey()

    elif cursor == 2:
        print("Você teve contato com algum caso positivo de COVID-19 nos últimos 7 dias?")
        print()
        print("1- Sim")
        print("2- Não")


        cursor = menu.intEntry()     
        if cursor == 1:
            print("Por favor, dirija-se para uma unidade de saúde e faça seu teste de COVID-19")
            print("Aqui você pode encontrar os locais disponíveis para testagem:")
            menu.places()

        elif cursor == 2:
            print()
            print("Neste caso, continue se cuidando para prevenção da COVID-19.")
            print()
            print("Caso você apresente sintomas, procure a unidade de saúde mais próxima de você ou fale conosco novamente.")
            menu.endChat()

        else:
            print("Resposta inválida. Vamos tentar de novo!")
            survey()    

    else:
        print("Resposta inválida. Vamos tentar de novo!")
        survey()