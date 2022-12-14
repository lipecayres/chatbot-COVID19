import news
import places
import doubts
import register
import survey


def menu():

    print("Como posso te ajudar hoje??")
    print()
    print("1- Boletim de notícias")                         #news
    print("2- Precisa fazer o teste para COVID-19?")        #survey
    print("3- Locais de testagem / vacinação")              #places
    print("4- Resultado/Laudo do teste COVID-19")           #register
    print("5- Fale Conosco")                                #doubts
 
    print()
    
    cursor = intEntry()

    if cursor == 1:
        news.news()
    elif cursor == 2:
        survey.survey()
    elif cursor == 3:
        places.places() 
    elif cursor == 4:
        register.register() 
    elif cursor == 5:
        doubts.doubts() 
    else:
        print()
        print("Entrada inválida, tente novamente.")
        print()        
        menu()

## NUMBER ENTRY VALIDATION

def intEntry():
    while True:
        n = input("Digite: ")    
        try:
            n = int(n)
            break
        except ValueError:
            print()
            print("Entrada inválida, tente novamente.")
    return n


def endChat():
    print("O que você quer fazer agora?")
    print()
    print("1- Ver de novo as opções de ajuda")
    print("2- Encerrar nosso papo")
    print()

    cursor = intEntry()
    if cursor == 1:
        menu()
    
    elif cursor == 2:
        print()
        print("Obrigado pela nossa conversa, se precisar pode me chamar de novo!")
        print()

    else:
        print()
        print("Entrada inválida, tente novamente.")
        endChat()