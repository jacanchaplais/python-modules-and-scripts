import click
import matplotlib.pyplot as plt


@click.command()
@click.argument("input-data", type=click.File())
@click.argument("output", type=click.File("wb"))
def main(input_data, output):
    """Takes a csv file INPUT-DATA, and produces a plot at OUTPUT."""
    x = []
    y = []
    for line in input_data:
        pair = line.split(",")
        x.append(float(pair[0]))
        y.append(float(pair[1]))
    plt.plot(x, y)
    plt.savefig(output)


if __name__ == '__main__':
    main()
