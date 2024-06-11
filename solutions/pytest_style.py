# Задание содержится в tasks/pytest_style.md

from runpy import run_path


def test_check_registration_form():
    run_path("check_registration_form.py")


def test_check_registration_with_bugs():
    run_path("check_registration_with_bugs.py")
