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
        deviation = sum([(item - mean)**2 for item in self.items])/self.size
        return round(deviation, 2)

    def printter(self, i):
        print(f"Amostragem {i}")
        print(f"Média: {self.mean()}")
        print(f"Mediana: {self.average()}")
        print(f"Desvio Padrão: {self.deviation()}")
        print()


class Resample:
    def __init__(self, original, n):
        self.samples = []
        self.original = original
        self.n = n

    def mean(self):
        mean = sum([sample.mean() for sample in self.samples])/self.n
        return round(mean, 2)

    def average(self):
        mean = sum([sample.average() for sample in self.samples])/self.n
        return round(mean, 2)

    def deviation(self):
        mean = sum([sample.deviation() for sample in self.samples])/self.n
        return round(mean, 2)

    def execute(self):
        self.original.printter("original")
        for i in range(0, self.n):
            sample_vector = []
            size = self.original.size
            
            for _ in range(0, self.n):
                index = randint(0, size-1)
                item = self.original.get_item(index)
                sample_vector.append(item)

            sample = Sample(sample_vector)
            sample.printter(i+1)
            self.samples.append(sample)

    def printter(self):
        print("Resultados gerais")
        print(f"Média das médias: {self.mean()}")
        print(f"Média das medianas: {self.average()}")
        print(f"Média dos desvios: {self.deviation()}")
        print()