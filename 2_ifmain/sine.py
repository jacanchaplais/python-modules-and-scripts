import math


NUM_VALS = 20
PHASE_FACTOR = 2.0 * math.pi / NUM_VALS


def wave_function(x, amplitude):
    return amplitude * math.sin(x)


def main():
    with open("out-data.csv", "w") as f:
        for i in range(NUM_VALS):
            x = PHASE_FACTOR * i
            y = wave_function(x, 1.0)
            f.write(f"{x},{y}\n")


if __name__ == "__main__":
    main()
