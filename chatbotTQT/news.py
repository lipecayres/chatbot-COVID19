## NEWS Function ## 
import menu

def news():
    print()
    print()
    print("Vi que você deseja ter mais informações. Vou te dar duas opções.")
    print("Você deseja ter mais informações sobre a pandemia ou sobre o projeto?") 
    print()
    print("1- Informações e noticias sobre a pandemia")
    print("2- Quero saber mais sobre o projeto!")
  
    print()

    cursor = menu.intEntry()

    if cursor == 1:
        print()
        print("Aqui você pode ver as noticias no mundo:")
        print()
        print("https://www.google.com/search?rlz=1C1FCXM_pt-PTBR993BR993&source=lnms&tbm=nws&sa=X&ved=2ahUKEwj00eW1itv5AhWwhJUCHee8An0Q_AUoAXoECAIQAw&q=coronav%C3%ADrus&biw=1536&bih=656&dpr=1.25")
        print()
        print("No site da SMS Salvador você acompanha todas as noticias pelo site da Secretaria de saúde:")
        print("http://www.saude.salvador.ba.gov.br/")
        print()
        print("Você pode também acompanhar pelo instagram: @smssalvador")
        print()
        print()

        menu.endChat()

    elif cursor == 2:
        print()
        print("Navegue pelo site do TQT Covid-19 e aproveite para fazer seu cadastro")
        print()
        print("http://www.tqtcovid.com/")
        print()
        print()
        
        menu.endChat()
        

  