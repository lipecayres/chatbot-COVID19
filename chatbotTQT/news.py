## NEWS Function ## 
import menu

def news():
    print("Vi que você deseja ter mais informações. Vou te dar duas opções.")

    print("Você deseja ter mais informações sobre a pandemia ou sobre o projeto?") 
    print("1- Informações e noticias sobre a pandemia")
    print("2- Quero saber mais sobre o projeto!")
  
    print()

    cursor = menu.intEntry()

    if cursor == 1:
        news()
    elif cursor == 2:
        survey()
  