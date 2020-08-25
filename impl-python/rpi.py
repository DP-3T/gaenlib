"""
Rolling Proximity Identifier generation functions
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from constants import *


def gen_enin(timestamp):

    """ Generate ENIntervalNumber (ENIN)

    Generated every 10 minutes. 

    If multiple of TEKRollingPeriod then a new TEK should be used

    Encoded as a 32-bit (uint32_t) unsigned little-endian
    value.

    :timestamp: Unix epoch time in seconds
    :returns: enin_int, enin
    """
    assert type(timestamp) == int
    enin_int = timestamp // 600
    enin_hex_str = hex(enin_int)[2:]
    # NOTE: pad to 4 bytes
    if len(enin_hex_str) == 6:
        enin_hex_str = enin_hex_str + '00'
    elif len(enin_hex_str) == 7:
        enin_hex_str = enin_hex_str + '0'
    enin = bytearray.fromhex(enin_hex_str)
    enin.reverse()
    return enin_int, enin


def gen_padded_data(enin):

    """ Generate padded data

    :enin: ENIN bytearray
    :returns: padded_data
    """
    assert len(enin) == 4

    padded_data = bytearray(16)
    padded_data[0:5] = b"EN-RPI"
    padded_data[6:11] = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    padded_data[11:17] = enin

    assert len(padded_data) == 16

    return padded_data


def gen_rpi(rpik, padded_data):
    """rpi = AES-ECB(RPIKi,PaddedDataj)

    The spec indicates AES-ECB with AES or AES128

    BLE payload = rpi | aem

    """

    rpi = bytearray(16)

    encryptor = Cipher(
        algorithms.AES(rpik),
        modes.ECB(),
        backend=default_backend()
    ).encryptor()

    rpi = bytearray(encryptor.update(padded_data) + encryptor.finalize())

    return rpi


if __name__ == "__main__":

    key = os.urandom(16)
    pd = os.urandom(16)

    print(gen_rpi(key, pd))
