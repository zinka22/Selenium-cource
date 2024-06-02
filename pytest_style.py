# Задание содержится в tasks/pytest_style.md

import subprocess

import pytest


def test_check_registration_form():
    result = subprocess.run(["python", "check_registration_form.py"])

    if result.returncode != 0:
        pytest.fail()


def test_check_registration_with_bugs():
    result = subprocess.run(["python", "check_registration_with_bugz.py"])

    if result.returncode != 0:
        pytest.fail()
