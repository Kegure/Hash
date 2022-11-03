from HashTable import HashTable_Chained,HashTable_Open_Address


def menu():
    print("[1] Inserir")
    print("[2] Procurar")
    print("[3] Deletar")
    print("[4] Mostrar a HashTable")
    print("[0] Encerrar Programa")

def is_date(date):
    if len(date) != 8:
        return "error"
    elif int(str(date)[:2]) == 0 or int(str(date)[:2]) > 31:
        return "error"
    elif int(str(date)[2:4]) == 0 or int(str(date)[2:4]) > 12:
        return "error"
    elif int(str(date)[4:8]) >= 2022:
        return "error"
    else:
        return date



def escolha_hash():
    print("[1] Endereçamento Aberto")
    print("[2] Encadeamento (Separado)")
    print("[3] Encadeamento (Coalesivo)")
    option = int(input("Qual Hash você deseja?"))
    match option:
        case 1:
            H = HashTable_Open_Address
        case 2:
            H = HashTable_Chained
        # case 3:
        # console_Encadeamento_Coalesivo()
        case _:
            print("Não é uma opção válida")
            console()
    console(H)

def console(H):
    menu()
    try:
        option = int(input("Digite sua escolha :"))
        while option != 0:
            if option == 1:
                H.insert_hash(int(is_date(input("Qual a Data deseja inserir?\nDigite no formato DDMMAAAA :"))))
            elif option == 2:
                H.search_hash(int(input("Qual a Data deseja buscar?")))
            elif option == 3:
                H.delete_hash(int(input("Qual a Data deseja deletar?")))
            elif option == 4:
                H.print_hash()
            else:
                print("Opção inválida!, por favor insirir uma opção valida do Menu\n")
                menu()
            option = int(input("Deseja Continuar?,Digite sua nova escolha :"))
    except ValueError:
        print("Isso não é um valor numérico ou data inválida ,Tente Novamente\n")
        console()


escolha_hash()




