from abc import ABCMeta, abstractmethod
from random import randint

from utils import get_stratums, get_stratum_sizes


class SamplingInterface(metaclass=ABCMeta):
    def __init__(self, pop_size, sample_size):
        self.pop_size = pop_size
        self.sample_size = sample_size
        self.population = [i+1 for i in range(0, pop_size)]
        self.sample = []

    @abstractmethod
    def build_sample(self):
        pass

    @abstractmethod
    def printter(self):
        pass


class SimpleSampling(SamplingInterface):

    def build_sample(self):
        for _ in range(0, self.sample_size):
            index = randint(0, self.pop_size-1)
            self.sample.append(self.population[index])

    def printter(self):
        print(self.sample)


class SystematicSampling(SamplingInterface):

    def build_sample(self):
        k = int(self.pop_size/self.sample_size)
        index = randint(0, self.sample_size-1)
        for _ in range(0, self.sample_size):
            self.sample.append(self.population[index])
            index += k

    def printter(self):
        print(self.sample)


class StratifiedSampling(SamplingInterface):

    def build_sample(self):
        stratums = get_stratums(self.pop_size)
        sizes = get_stratum_sizes(stratums)
        begin = 0
        
        for id, size in enumerate(sizes):
            stratum = []
            end = int(self.pop_size*size/100) + begin
            for index in range(begin, end):
                stratum.append(self.population[index])
            begin = end

            n = int(self.sample_size*size/100)
            for _ in range(0, n):
                index = randint(0, size-1)
                self.sample.append((id, stratum[index]))

    def printter(self):
        print(self.sample)


def get_sampling(type, pop_size, sample_size):
    if type == 1:
        return SimpleSampling(pop_size, sample_size)
    elif type == 2:
        return SystematicSampling(pop_size, sample_size)
    elif type == 3:
        return StratifiedSampling(pop_size, sample_size)
    
    return None