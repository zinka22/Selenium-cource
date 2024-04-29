from math import log, sin


def solve_captcha(number: int):
    """Calculate math expression, which value
    will be used to solve captcha
    """
    return str(log(abs(12 * sin(number))))
