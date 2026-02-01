from src.view.first_view import introduction_page


def start() -> None:
    while True:

        command = introduction_page()
        
        if command == "1": print("Inserindo Música")
        elif command == "2": print("Criando PlayList")
        elif command == "5": exit()
        else: print("\n Comando Inválido! Tente Novamente! \n \n")
