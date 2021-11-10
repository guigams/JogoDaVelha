lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]
lista_3 = [6, 7, 8]

def select():
    print(lista_1)
    print(lista_2)
    print(lista_4)

tela_inicial = '''Quando for sua vez, digite o seu caracter (X ou O) e o número correspondente à posição no tabuleiro para realizar sua jogada.

     |     |     
  0  |  1  |  2  
_____|_____|_____
     |     |     
  3  |  4  |  5  
_____|_____|_____
     |     |     
  6  |  7  |  8  
     |     |

QUE COMECEM OS JOGOS!!!

     '''

print(tela_inicial)

for x in range(0,9):
    print(' ')
    select()
    print(' ')

    icon = str(input("SELECT: [X] ou [O]?? "))
    print(' ')
    posicao = input("Selecione a posição: ")

    if posicao == '0':
        lista_1[0] = icon
        select()

    if posicao == '1':
        lista_1[1] = icon
        select()

    if posicao == '2':
        lista_1[2] = icon
        select()

    if posicao == '3':
        lista_2[0] = icon
        select()

    if posicao == '4':
        lista_2[1] = icon
        select()

    if posicao == '5':
        lista_2[2] = icon
        select()

    if posicao == '6':
        lista_3[0] = icon
        select()

    if posicao == '7':
        lista_3[1] = icon
        select()

    if posicao == '8':
        lista_3[2] = icon
        select()

# ---------------------------------------------------------------------------- #

    if lista_1[0] == lista_2[0] == lista_3[0]:
        print("FIM DE JOGO!")
        break

    if lista_1[1] == lista_2[1] == lista_3[1]:
        print("FIM DE JOGO!")
        break

    if lista_1[2] == lista_2[2] == lista_3[2]:
        print("FIM DE JOGO!")
        break

    if lista_1[0] == lista_2[1] == lista_3[2]:
        print("FIM DE JOGO!")
        break

    if lista_2[0] == lista_2[1] == lista_2[2]:
        print("FIM DE JOGO!")
        break

    if lista_3[0] == lista_3[1] == lista_3[2]:
        print("FIM DE JOGO!")
        break

    if lista_1[2] == lista_2[1] == lista_3[0]:
        print("FIM DE JOGO!")
        break

    if lista_3[2] == lista_2[1] == lista_1[0]:
        print("FIM DE JOGO!")
        break

    if x == 7:
        print("Princesa Elisabeth.")
        break
