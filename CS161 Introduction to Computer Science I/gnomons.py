"""Gnomon calculator for CS161 MWF 0800-0950."""
# by Brady Esplin
# Program will prompt user for a number, check it for square, exit if not
# square. If number is square, find two triangular numbers that sum to said
# square. Print the two triangular number and original square number

import math

INPUT_NUMBER = int(input("what square number are we using?"))

ROOT = math.sqrt(INPUT_NUMBER)

TRI_NUM_1 = (ROOT ** 2 - ROOT) / 2
TRI_NUM_2 = INPUT_NUMBER - TRI_NUM_1

if math.sqrt(INPUT_NUMBER) % 1 == 0:
    print(f"{INPUT_NUMBER} is a perfect square with a root of {ROOT}.")
    print(f"It is the sum of triagonal numbers {TRI_NUM_2} and {TRI_NUM_1}")

else:
    print(f"{INPUT_NUMBER} is not a perfect square. ERROR")
