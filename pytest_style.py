# Задание содержится в tasks/pytest_style.md


import subprocess

import pytest

from check_registration_form import check_registration_form


def test_check_registration_form_link1():
    check_registration_form()


def test_check_registration_form_link2():
    result = subprocess.run(["python", "check_registration_with_bugz.py"])

    if result.returncode != 0:
        pytest.fail()
