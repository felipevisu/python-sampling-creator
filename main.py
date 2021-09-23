from sampling import get_sampling
import sampling

pop_size = 0
sample_size = 0

# simple random (1), systematic (2) or stratified (3)
sample_type = None

while True:
    try:
        pop_size = int(input("Informe o tamanho ta população\n-> "))
        if pop_size > 0:
            break
        else:
            print('O valor deve ser um inteiro positivo!')
    except:
        print('O valor informado é inválido!')


while True:
    try:
        sample_size = int(input("Informe o tamanho da amostra\n-> "))
        if sample_size > 0 and sample_size < pop_size:
            break
        else:
            print('O valor deve ser um inteiro positivo e menor que a população')
    except:
        print('O valor informado é inválido!')


while True:
    try:
        sample_type = int(input("Informe o tipo de amostragem: Simples (1), Sistemática (2) ou Estratificada (3)\n-> "))
        if sample_type in [1, 2, 3]:
            break
        else:
            print('O valor informado é inválido!')
    except:
        print('O valor informado é inválido!')


sampling = get_sampling(sample_type, pop_size, sample_size)
sampling.build_sample()
sampling.printter()