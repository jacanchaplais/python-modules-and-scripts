import random
import math


def linspace(start, stop, size=20):
    step = (stop - start) / size
    return [step * i for i in range(size)]


def degree_range_to_radians(start, stop, size=20):
    deg_range = linspace(start, stop, size)
    return [math.radians(deg) for deg in deg_range]


def sine_wave(phases, amplitude=1.0):
    return [amplitude * math.sin(rad) for rad in phases]


def add_noise(signal, scale=1.0):
    return [x + scale * random.random() for x in signal]
