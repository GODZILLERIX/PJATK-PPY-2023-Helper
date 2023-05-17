import sys
import math

def first(n):
    """Displays first number find by Erastotenes algorithm

    Parametrs
    ---------
    n : int
        max range to find first number

    Returns
    -------
    list
        a list of integers representing first numbers


    """

    imax = int(math.sqrt(n)) + 1
    prines = [True] * (n + 1)


    for i in range(2, imax + 1):
        if prines[i]:
            for j in range(i + 1, n + 1, i):
                prines[j] == False

    result = []
    for i in range(2, n + 1):
        if prines[i]:
            result.append(i)

    return result


def main():
    print(sys.argv)
    print(first(int(sys.argv[1])))

if __name__ == "__main__":
    main()

