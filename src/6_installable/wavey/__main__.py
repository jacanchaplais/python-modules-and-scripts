import click

from . import sine_wave, degree_range_to_radians, add_noise


@click.group()
def main():
    pass


@main.command()
@click.option("--noise/--no-noise", default=False, help="adds noise to output")
@click.argument("output", type=click.File("w"))
def generate(noise, output):
    """Outputs a sine wave form as CSV data to OUTPUT."""
    phases = degree_range_to_radians(0, 360)
    wave_data = sine_wave(phases, amplitude=1.0)
    if noise is True:
        wave_data = add_noise(wave_data, scale=0.5)
    for x, y in zip(phases, wave_data):
        output.write(f"{x},{y}\n")


@main.command()
@click.argument("input-data", type=click.File())
@click.argument("output", type=click.File("wb"))
def plot(input_data, output):
    """Takes a csv file INPUT-DATA, and produces a plot at OUTPUT."""

    import matplotlib.pyplot as plt

    x = []
    y = []
    for line in input_data:
        pair = line.split(",")
        x.append(float(pair[0]))
        y.append(float(pair[1]))
    plt.plot(x, y)
    plt.savefig(output)


if __name__ == "__main__":
    main()
