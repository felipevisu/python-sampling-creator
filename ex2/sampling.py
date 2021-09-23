from random import randint


class Sample:
    def __init__(self, items):
        self.items = items
        self.size = len(items)

    def get_item(self, index):
        return self.items[index]

    def mean(self):
        mean = sum(self.items)/self.size
        return round(mean, 2)

    def average(self):
        items = self.items.copy()
        items.sort()
        if self.size % 2 == 0:
            index_1 = int(self.size/2)
            index_2 = index_1 + 1
            average = (items[index_1] + items[index_2])/2
            return round(average, 2)
        else:
            index = int(self.size/2)
            average = items[index]
            return round(average, 2)

    def deviation(self):
        mean = self.mean()
        total = 0
        for item in self.items:
            total += (item - mean)**2
        return round(total/self.size, 2)

    def printter(self, i):
        print(f"Amostragem {i}")
        print(f"Média: {self.mean()}")
        print(f"Mediana: {self.average()}")
        print(f"Desvio Padrão: {self.deviation()}")
        print()


class Resample:
    def __init__(self, samples):
        self.samples = samples

    def add_sample(self, sample):
        self.samples.append(sample)

    def mean(self):
        mean = sum([sample.mean() for sample in self.samples])/len(self.samples)
        return round(mean, 2)

    def average(self):
        mean = sum([sample.average() for sample in self.samples])/len(self.samples)
        return round(mean, 2)

    def deviation(self):
        mean = sum([sample.deviation() for sample in self.samples])/len(self.samples)
        return round(mean, 2)

    def printter(self):
        print("Resultados gerais")
        print(f"Média das médias: {self.mean()}")
        print(f"Média das medianas: {self.average()}")
        print(f"Média dos desvios: {self.deviation()}")
        print()


def resample(original, n):
    resample = Resample([])
    original.printter("original")
    
    for i in range(0, n):
        sample_vector = []
        size = original.size
        
        for _ in range(0, n):
            index = randint(0, size-1)
            item = original.get_item(index)
            sample_vector.append(item)

        sample = Sample(sample_vector)
        sample.printter(i+1)
        resample.add_sample(sample)

    resample.printter()

    