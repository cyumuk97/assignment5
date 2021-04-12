#!/usr/bin/env python3
# test_my_io.py

"""
Test for module my_io.py
"""

import os
import pytest
from assignment5 import my_io

test = "test.txt"


def test_existing_get_fh_4_reading():
    """
    Checks if my_io opens correctly a file for reading
    """
    # Test file
    _create_test_file(test)

    test = my_io.get_fh(test, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(test)


def test_existing_get_fh_4_writing():
    """
    Checks if my_io opens correctly a file for writing
    """
    test = my_io.get_fh(test, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(test)


def test_get_fh_4_IOError():
    """
    Tests if my_io raises IOError
    """
    with pytest.raises(IOError):
        my_io.get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    """
    Tests if my_io raises ValueError
    """
    # Test file
    _create_test_file(test)

    with pytest.raises(ValueError):
        my_io.get_fh("does_not_exist.txt", "rrr")
    os.remove(test)


def test_get_fh_4_TypeError():
    """
    Tests if my_io raises TypeError
    """
    # Test file
    _create_test_file(test)

    with pytest.raises(TypeError):
        my_io.get_fh([], "r")
    os.remove(test)


def _create_test_file(file):
    """
    Creates test file
    """
    open(file, "w").close()
