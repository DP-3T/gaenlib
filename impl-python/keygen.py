"""
Key Generation functions

All devices sharing the same TEKRollingPeriod roll TEKs at the same time — at
the beginning of an interval whose ENIntervalNumber is a multiple of
TEKRollingPeriod.

"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

from constants import *

def gen_tek():
    """tel = CRNG(16)"""
    return os.urandom(16)


def gen_rpik(tek):
    """Generate rolling proximity identifier key (rpik)

    In the spec HKDF(Key=tek, Salt=NULL, Info="EN-RPIK", OutputLength=16)

    :returns: rpik

    """
    rpik = b""

    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=16,
        salt=None,
        info=INFO['rpik'],
        backend=default_backend())

    rpik = hkdf.derive(tek)

    return rpik


def gen_aemk(tek):
    """Generate aemk.

    In the spec HKDF(Key=tek, Salt=NULL, Info="EN-AEMK", OutputLength=16)

    :returns: aemk

    """
    aemk = b""

    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=16,
        salt=None,
        info=INFO['aemk'],
        backend=default_backend())

    aemk = hkdf.derive(tek)

    return aemk

