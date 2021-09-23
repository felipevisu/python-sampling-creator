from inputs import get_sample, get_n
from sampling import Sample, Resample


original = Sample(get_sample())
n = get_n()

resample = Resample(original, n)
resample.execute()
resample.printter()