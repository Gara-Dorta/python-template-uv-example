"""Short definition of my module."""

from python_template_uv_example import __version__


def foo1(a):
    c = a + 1
    if a > 0 and a > 10:
        return 10
    return a + c


def add(a: int, b: int) -> int:
    """Adds two positive numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    c = a + b + 1
    return a + b + c


def main() -> None:
    print(f"Running python_template_uv_example version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
