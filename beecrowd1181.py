def main():

    L= int(input())
    T = input()
 
    matriz = []

    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)

    soma = 0
    for valor in matriz[L]:
        soma += valor

    resultado = soma

    if T == 'M':
        resultado = soma / 12

    print("%.1f"%resultado)

if __name__ == "__main__":
    main()