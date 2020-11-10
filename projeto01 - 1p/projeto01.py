from circulo import mainCircle

def main():
    choice = '0'
    while choice == '0':
        print("C/c para Circulo")
        print("T/t para Triangulo")
        print("Q/q para 2 quadrados")
        choice = input("Escolha uma das opções: ")
        if choice == "c" or choice == 'C':
            mainCircle()
        elif choice == "t" or choice == 'T':
            print("triangulo")
        elif choice == "q" or choice == 'Q':
            print("quadrados")
        else:
            print("Não existe essa opção.")
            return

if __name__ == "__main__":
    main()
