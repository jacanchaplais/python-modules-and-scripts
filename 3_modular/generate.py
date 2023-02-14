import signals


def main():
    phases = signals.degree_range_to_radians(0, 360)
    wave_data = signals.sine_wave(phases, 1.0)
    with open("out-data.csv", "w") as f:
        for x, y in zip(phases, wave_data):
            f.write(f"{x},{y}\n")


if __name__ == "__main__":
    main()
