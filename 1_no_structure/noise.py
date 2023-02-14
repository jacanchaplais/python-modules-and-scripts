import random


NUM_VALS = 20


def noise_function(x, amplitude):
    """Adds noise with a given amplitude to the input."""
    return x + amplitude * random.random()


with open("out-data.csv", "w") as f:
    for x in range(NUM_VALS):
        y = noise_function(x, 10.0)
        f.write(f"{x},{y}\n")
