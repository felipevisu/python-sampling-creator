from sampling import get_sampling
from inputs import get_pop_size, get_sample_size, get_sample_type


pop_size = get_pop_size()
sample_size = get_sample_size(pop_size)
sample_type = get_sample_type()

sampling = get_sampling(sample_type, pop_size, sample_size)
sampling.build_sample()
sampling.printter()