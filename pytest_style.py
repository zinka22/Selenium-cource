# Задание содержится в tasks/pytest_style.md

from helpers import run_py_file


def test_check_registration_form_link1():
    run_py_file("check_registration_form.py")


def test_check_registration_form_link2():
    run_py_file("check_registration_with_bugz.py")
