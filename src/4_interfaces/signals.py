"""
``signals``
===========

Routines for creating signals.
"""
import random
import math


def linspace(start, stop, size=20):
    """Generate a range of equally spaced values within given interval.

    Parameters
    ----------
    start, stop : float
        Interval of values to span.
    size : int
        Number of values to produce within this interval. Default is 20.

    Returns
    -------
    values : list[float]
        A list of equally spaced values in the given range.
    """
    step = (stop - start) / size
    return [step * i for i in range(size)]


def degree_range_to_radians(start, stop, size=20):
    """Generate a range of equally spaced phases within given interval.
    Input is given in degrees, output is in radians.

    Parameters
    ----------
    start, stop : float
        Interval of phases to span, in degrees.
    size : int
        Number of values to produce within this interval. Default is 20.
    
    Returns
    -------
    phase_range : list[float]
        A list of equally spaced phases in the given range, converted
        from degrees to radians.
    """
    deg_range = linspace(start, stop, size)
    return [math.radians(deg) for deg in deg_range]


def sine_wave(phases, amplitude=1.0):
    """Takes a list of phases in radians, and produces a list
    of the corresponding values of a sine function.

    Parameters
    ----------
    phases : list[float]
        Angles to pass to the sine function.
    amplitude : float
        Amplitude of the sine function.

    Returns
    -------
    sine_values : list[float]
        Sine function evaluated at the given phase values.
    """
    return [amplitude * math.sin(rad) for rad in phases]


def add_noise(signal, scale=1.0):
    """Adds uniformly distributed noise to an input signal.

    Parameters
    ----------
    signal : list[float]
        Clean input signal, given as a list of numbers.
    scale : float
        Magnitude of the noise added to the signal. Default is 1.0.

    Returns
    -------
    noisy_signal : list[float]
        Input signal with noise.
    """
    return [x + scale * random.random() for x in signal]
