"""
Test aem generation

Test vectors from test_vector/TestVectors.h
"""

from aem import *
from test_vectors import *


def test_aem():

    for i in range(0, 144):
        ComputedAEM = gen_aem(AEMK, RPI[i], BLEMetadata)
        print('test_aem {} ComputedAEM: {}'.format(i, ComputedAEM))
        print('test_aem {}        AEM0: {}'.format(i, AEM[i]))
        assert len(ComputedAEM) == 4
        assert ComputedAEM == AEM[i]


if __name__ == "__main__":
    test_aem()

