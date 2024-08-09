import math
from decimal import Decimal, getcontext


def calculate_pi(precision):
    """
    This function calculates Pi to the given precision using
    the Gauss-Legendre Algorithm.
    """
    getcontext().prec = precision + 1  # Set precision
    a = Decimal(1)  # Initialize a, b, t, p
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in range(10):  # Perform iterations
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    return str(pi)[:precision + 1]  # Return Pi to the specified precision


def main():
    precision = input("Enter the number of decimal places for Pi calculation (up to 50): ")

    if not precision.isdigit():
        print("Please enter a valid number.")
        return

    precision = int(precision)

    if precision > 50:
        print("Limit exceeded. Please enter a number up to 50.")
        return

    pi_value = calculate_pi(precision)
    print(f"Pi to {precision} decimal places: {pi_value}")


if __name__ == "__main__":
    main()
