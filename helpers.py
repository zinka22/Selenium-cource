from math import log, sin


def solve_captcha(number: int):
    """this function helps to calculate math expression with the value of an argument"""
    return str(log(abs(12 * sin(number))))
