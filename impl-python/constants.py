"""
GAEN constants
"""

PADDED_DATA_BYTES = 16
TEK_BYTES = 16
RPI_BYTES = 16
AEM_BYTES = 4
ENIN_BYTES = 4

TEKKeysPerDay = 14
TEKRollingPeriod = 144  # 144 * 10 * 60 = 24 hours

INFO = {
    'rpik': b'EN-RPIK',
    'aemk': b'EN-AEMK',
}
