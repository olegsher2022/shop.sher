import app
import pytest


def test_main_page():
    rv = app.app.get('/')

    print(rv)
    assert rv
