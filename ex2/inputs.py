def get_sample():
    sample = []
    print("Cadastre os valores de sua amostra")
    print("Para sair informe qualquer valor que não seja um número inteiro")

    while True:
        try:
            value = int(input("Digite um valor:\n-> "))
            sample.append(value)
        except:
            break

    return sample


def get_n():
    while True:
        try:
            n = int(input("Informe o número de reamostragens:\n-> "))
            if n > 0:
                return n
            else:
                print("O número deve ser maior que 0")
        except:
            print("O valor deve ser um número inteiro")