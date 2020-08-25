"""
Test vectors from test_vector/TestVectors.h
"""

from rpi import *
from test_vectors import *

# NOTE: testing only the int representation
def test_enin():
    ComptedENIN, _ = gen_enin(secondsSince1970)
    # print('test_enin ComptedENIN: {}'.format(ComptedENIN))
    # print('test_enin        ENIN: {}'.format(ENIntervalNumberOfGeneratedKey))
    assert ComptedENIN == ENIntervalNumberOfGeneratedKey


def test_rpi():

    for i in range(0, 144):
        # print(ENIN)
        enin_int, enin = gen_enin(secondsSince1970 + i*10*60)
        padded_data = gen_padded_data(enin)
        ComputedRPI = gen_rpi(RPIK, padded_data)
        print('test_rpi {} ComptedRPI: {}'.format(i, ComputedRPI))
        print('test_rpi {}        RPI: {}'.format(i, RPI[i]))
        assert len(ComputedRPI) == 16
        assert ComputedRPI == RPI[i]


if __name__ == "__main__":
    test_enin()
    test_rpi()

