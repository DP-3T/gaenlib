"""
Associated Metadata generation functions
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from constants import *


def gen_aem(aemk, rpi, metadata):
    """aem = AES128−CTR(key=AEMKi,iv=RPIi,j,data=Metadata)

    BLE payload = rpi | aem

    """

    aem = bytearray(4)

    encryptor = Cipher(
        algorithms.AES(aemk),
        modes.CTR(rpi),
        backend=default_backend()
    ).encryptor()

    aem = bytearray(encryptor.update(metadata) + encryptor.finalize())

    return aem

