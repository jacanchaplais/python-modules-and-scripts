import click

from . import sine_wave, degree_range_to_radians, add_noise


@click.command()
@click.option("--noise/--no-noise", default=False)
@click.argument("output", type=click.File("w"))
def main(noise, output):
    """Outputs a sine wave form as CSV data to OUTPUT."""
    phases = degree_range_to_radians(0, 360)
    wave_data = sine_wave(phases, amplitude=1.0)
    if noise is True:
        wave_data = add_noise(wave_data, scale=0.5)
    for x, y in zip(phases, wave_data):
        output.write(f"{x},{y}\n")


if __name__ == "__main__":
    main()
