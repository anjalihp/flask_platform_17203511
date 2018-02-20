#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from flask_platform_17203511.skeleton import fib

__author__ = "Anjali Gowda"
__copyright__ = "Anjali Gowda"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
