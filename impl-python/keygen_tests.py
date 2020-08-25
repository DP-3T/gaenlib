"""
Test key generation functions
"""

from keygen import *
from test_vectors import *


def test_rpik():
    ComptedRPIK = gen_rpik(TemporaryTracingKey)
    assert ComptedRPIK == RPIK


def test_aemk():
    ComptedAEMK = gen_aemk(TemporaryTracingKey)
    assert ComptedAEMK == AEMK


if __name__ == "__main__":
    test_rpik()
    test_aemk()
