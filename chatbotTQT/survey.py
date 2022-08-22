import menu

def survey():
    print("Está com sintomas da COVID-19 (febre, coriza, dor no corpo, cansaço, dor na garganta)?")
    print()
    print("1- Sim")
    print("2- Não")

    cursor = menu.intEntry()
    if cursor == 1:


    elif cursor == 2:


    else:
        print("Resposta inválida. Vamos tentar de novo!")
        survey()