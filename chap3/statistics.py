#!/usr/bin/env python3

import collections
import math
import sys


Statistics = collections.namedtuple("Statistics",
                                    "mean mode median std_dev")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    numbers = []
    frequencies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print("no numbers found")


def read_data(filename, numbers, frequencies):
    with open(filename, encoding="ascii") as file:
        for lino, line in enumerate(file, start=1):
            for x in line.split():
                try:
                    number = float(x)
                    numbers.append(number)
                    frequencies[number] += 1
                except ValueError as err:
                    print(f"{filename}:{lino}: skipping {x}: {err}")


def calculate_statistics(numbers, frequencies):
    mean = sum(numbers) / len(numbers)
    mode = calculate_mode(frequencies, 3)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers, mean)
    return Statistics(mean, mode, median, std_dev)


def calculate_mode(frequencies, maximum_modes):
    highest_frequency = max(frequencies.values())
    mode = [number for number, frequency in frequencies.items()
            if frequency == highest_frequency]
    if not (1 <= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode


def calculate_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    median = numbers[middle]
    if len(numbers) % 2 == 0:
        median = (median + numbers[middle - 1]) / 2
    return median


def calculate_std_dev(numbers, mean):
    total = 0
    for number in numbers:
        total += ((number - mean) ** 2)
    variance = total / (len(numbers) - 1) # variance is n-1
    return math.sqrt(variance)# std. dev.


def print_results(count, statistics):
    real = "9.2f"

    if statistics.mode is None:
        modeline = ""
    elif len(statistics.mode) == 1:
        modeline = f"mode      = {statistics.mode[0]:{real}}\n"
    else:
        modeline = f"mode      = [{', '.join(f'{m:.2f}' for m in statistics.mode)}]\n"

    print(f"""\
count     = {count:6}
mean      = {statistics.mean:{real}}
median    = {statistics.median:{real}}
{modeline}\
std. dev. = {statistics.std_dev:{real}}""")


if __name__ == "__main__":
    main()
