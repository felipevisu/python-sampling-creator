from abc import ABCMeta, abstractmethod
from random import randint

from inputs import get_stratums, get_stratum_sizes


# interface to create the ideal sampling
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
        population = self.population.copy()
        for i in range(0, self.sample_size):
            index = randint(0, self.pop_size-1-i)
            item = population.pop(index)
            self.sample.append(item)

    def printter(self):
        print(self.sample)


class SystematicSampling(SamplingInterface):

    def build_sample(self):
        k = int(self.pop_size/self.sample_size)
        index = randint(0, self.sample_size-1)
        for _ in range(0, self.sample_size):
            if index > self.pop_size: # make a circular iterator
                index = index - self.pop_size
            item = self.population[index]
            self.sample.append(item)
            index += k

    def printter(self):
        print(self.sample)


class StratifiedSampling(SamplingInterface):

    def build_sample(self):
        stratums = get_stratums(self.pop_size)
        sizes = get_stratum_sizes(stratums, self.sample_size)
        begin = 0
        
        # split the population in stratums
        for id, size in enumerate(sizes):
            stratum = []
            end = size + begin
            for index in range(begin, end):
                stratum.append(self.population[index])
            begin = end # go to the next stratum

            # apply the simple sampling for the current stratum
            for i in range(0, size):
                index = randint(0, size-1-i)
                item = stratum.pop(index)
                self.sample.append((id, item))

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