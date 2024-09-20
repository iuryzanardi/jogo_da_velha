matriz = [['','',''],
          ['','',''],
          ['','','']]

class Jogo():
    def exibir_tela():
        contador = 0
        for lista in matriz:
            for elemento in lista:
                contador += 1
                print('|', elemento, '|', end='')
                if contador == 3:
                    print('')
                    contador = 0

    def verifica_todos_preenchidos():
        for linha in matriz:
            for elemento in linha:
                if elemento == '':
                    return False
                else:
                    return True

    def verifica_vitoria(simbolo):
        for linha in matriz:
            if all(celula == simbolo for celula in linha):
                return True
            
            for col in range(3):
                if all(matriz[linha][col] == simbolo for linha in range(3)):
                    return True

            if all(matriz[i][i] == simbolo for i in range(3)):
                return True

            if all(matriz[i][2 - i] == simbolo for i in range(3)):
                return True

            return False
        
    def verificar_entrada(linha, coluna):
        while True:
            if matriz[linha][coluna] == '':
                return True
            else:
                print('Deve ser em um espaço em branco!')
                linha = int(input('Digite a coluna: '))
                coluna = int(input('Digite a linha: '))

                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print('Coordenadas inválidas! Tente novamente.')

    def iniciar_jogo():
        while True:
            Jogo.exibir_tela()
            x_linha = int(input('Digite a linha: '))
            x_coluna = int(input('Digite a coluna: '))

            if Jogo.verificar_entrada(x_linha, x_coluna) == True:
                matriz[x_linha][x_coluna] = 'X'
            if Jogo.verifica_vitoria('X'):
                Jogo.exibir_tela()
                print("X ganhou!")
                break

            Jogo.exibir_tela()
            o_linha = int(input('Digite a linha: '))
            o_coluna = int(input('Digite a coluna: '))
            
            if Jogo.verificar_entrada(o_linha, o_coluna) == True:
                matriz[o_linha][o_coluna] = 'O'
            if Jogo.verifica_vitoria('O'):
                Jogo.exibir_tela()
                print("O ganhou!")
                break
            

Jogo.iniciar_jogo()