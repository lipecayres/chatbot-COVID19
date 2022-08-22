def intro():
    print()
    print("Olá, seja bem-vindo(a)")
    print("Eu sou a Cora, assistente virtual do projeto TQT Covid-19!")
    print("Como posso te ajudar hoje??")
    print()

def menu():

    print("Como posso te ajudar hoje??")
    print("1 - Informações sobre prevenção da COVID-19")    #news
    print("2- Precisa fazer o teste para COVID-19?")        #survey
    print("3- Locais de testagem / vacinação")              #places
    print("4- Resultado/Laudo do teste COVID-19")           #register
    print("5- Fale Conosco")                                #doubts
 
    print()
    
    cursor = intEntry()

    if cursor == 1:
        news()
    elif cursor == 2:
        survey()
    elif cursor == 3:
        places() 
    elif cursor == 4:
        register() 
    elif cursor == 5:
        doubts() 
    else:
        print()
        print("Entrada inválida, tente novamente.")
        print()        
        menu()

## NUMBER ENTRY VALIDATION

def intEntry():
    while True:
        n = input("Digite:")    
        try:
            n = int(n)
            break
        except ValueError:
            print("Entrada inválida, tente novamente.")
    return n
