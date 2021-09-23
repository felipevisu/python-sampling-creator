
from inputs import get_sample, get_n
from sample import Sample, resample


original = Sample(get_sample())
n = get_n()

resample(original, n)