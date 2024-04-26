from math import log, sin


def solve_captcha(number: int):
    """this function helps to calculate math expression,
    witch value will be used to solve captcha
    """
    return str(log(abs(12 * sin(number))))
