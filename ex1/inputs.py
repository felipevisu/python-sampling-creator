def get_pop_size():
    while True:
        try:
            pop_size = int(input("Informe o tamanho ta população\n-> "))
            if pop_size > 0:
                return pop_size
            else:
                print('O valor deve ser um inteiro positivo!')
        except Exception:
            print('O valor informado é inválido!')


def get_sample_size(pop_size):
    while True:
        try:
            sample_size = int(input("Informe o tamanho da amostra\n-> "))
            if sample_size > 0 and sample_size < pop_size:
                return sample_size
            else:
                print('O valor deve ser um inteiro positivo e menor que a população')
        except Exception:
            print('O valor informado é inválido!')


# simple random (1), systematic (2) or stratified (3)
def get_sample_type():
    while True:
        try:
            sample_type = int(input("Informe o tipo de amostragem: Simples (1), Sistemática (2) ou Estratificada (3)\n-> "))
            if sample_type in [1, 2, 3]:
                return sample_type
            else:
                print('O valor informado é inválido!')
        except Exception:
            print('O valor informado é inválido!')


def get_stratums(pop_size):
    while True:
        try:
            stratums = int(input("Informe a quantidade de estratos\n-> "))
            if stratums > 0 and stratums < pop_size:
                return stratums
            else:
                print(f'O número de estratos deve ser maior que 0 e menor que {pop_size}')
        except Exception:
            print('O valor informado é inválido!')


def get_stratum_sizes(stratums, sample_size):
    sizes = []
    print("Informe o tamanho de cada estrato, a soma de todos deve ser o tamanho da amostra")
    for i in range(0, stratums): # define one size for each statrum
        while True:
            try:
                size = int(input(f"Informe o tamanho do estrado {i+1}\n-> "))
                if size > 0 and size <= sample_size:
                    sizes.append(size)
                    break
                else:
                    print(f'O tamanho deve ser maior que 0 e menor ou igual a {sample_size}')
            except Exception:
                print('O valor informado é inválido!')
    
    # verify if sizes sum is equal to 100%
    if sum(sizes) == sample_size:
        return sizes

    print(f"Erro! A soma do tamanho de todos extratos deve ser {sample_size}")
    return get_stratum_sizes(stratums, sample_size)