from circulo import mainCircle
from triangulo import mainTriangle
from quadrados import mainSquares

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
            mainTriangle()
        elif choice == "q" or choice == 'Q':
            mainSquares()
        else:
            print("Não existe essa opção.")
            return

if __name__ == "__main__":
    main()
