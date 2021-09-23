def get_stratums(pop_size):
    while True:
        try:
            stratums = int(input("Informe a quantidade de estratos\n-> "))
            if stratums > 0 and stratums < pop_size:
                return stratums
            else:
                print(f'O número de estratos deve ser maior que 0 e menor que {pop_size}')
        except:
            print('O valor informado é inválido!')


def get_stratum_sizes(stratums):
    sizes = []
    print("Informe o tamanho de cada estrato em porcentagem. Ex.: 20")
    for i in range(0, stratums):
        while True:
            try:
                size = int(input(f"Informe o tamanho do estrado {i+1}\n-> "))
                if size > 0 and size <= 100:
                    sizes.append(size)
                    break
                else:
                    print('O tamanho deve ser maior que 0 e menor que 100')
            except:
                print('O valor informado é inválido!')
    
    total = 0
    for size in sizes:
        total += size
    if total == 100:
        return sizes

    print("Erro! A soma do tamanho de todos extratos deve ser 100%")
    return get_stratum_sizes(stratums)