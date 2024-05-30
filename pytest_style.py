# Задание содержится в tasks/pytest_style.md


import subprocess

import pytest


def test_check_registration_form_link1():
    result = subprocess.run(["python", "check_registration_form.py"])

    if result.returncode != 0:
        pytest.fail()


def test_check_registration_form_link2():
    result = subprocess.run(["python", "check_registration_with_bugz.py"])

    if result.returncode != 0:
        pytest.fail()