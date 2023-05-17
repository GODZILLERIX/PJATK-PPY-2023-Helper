import sys

def fibb(n):
    """Displays the nth fibonacci number

    Parameters
    ----------
    n : int
        The nth number from fibonacci sequence


    Returns
    -------
    number
        a number representing the nth Fibonacci number



    """

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)

def main():
    print(sys.argv)
    print(fibb(int(sys.argv[1])))

if __name__ == "__main__":
    main()