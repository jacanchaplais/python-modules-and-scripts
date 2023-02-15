import click

import signals


@click.command()
@click.option("--noise/--no-noise", default=False, help="adds noise to output")
@click.argument("output", type=click.File("w"))
def main(noise, output):
    """Outputs a sine wave form as csv data to OUTPUT."""
    phases = signals.degree_range_to_radians(0, 360)
    wave_data = signals.sine_wave(phases, amplitude=1.0)
    if noise is True:
        wave_data = signals.add_noise(wave_data, scale=0.5)
    for x, y in zip(phases, wave_data):
        output.write(f"{x},{y}\n")


if __name__ == "__main__":
    main()
