# Bluetooth analysis (see [issue](https://github.com/DP-3T/gaenlib/issues/11#issuecomment-715442353))

Tools used:
* Logcat traces
* HCI snoop debug traces on the phones
* Bluetooth sniffer device (TI CC1352R1 dev kit)
* Nordic nRF Connect app

The devices analyzed are:
* Google Pixel4 (Bluetooth 5.0), LineageOS 17.1, SwissCovid app bundled with microG EN libraries (v0.2.13.203915)
* Sony Z3 (Bluetooth 4.0), LineageOS 17.1, SwissCovid app bundled with microG EN libraries (v0.2.13.203915)

# Advertisement: sequence of  HCI commands
Every 10 minutes, aligned on a 10-minute boundary:
## Pixel4
* `LE Rand`
* `LE Set Extended Advertising Parameters` handle 0, legacy PDUs, ADV_NONCONN_IND, interval 250-281.25 msec, channels 37,38,39, random device address
* `LE Set Advertising Set Random Address` handle 0
* `LE Set Extended Advertising Data` handle 0
* `LE Set Extended Scan Response Data` handle 0
* `LE Set Extended Advertising Enable` handle 0, on
[10min]
* `LE Set Extended Advertising Enable` handle 0, off
* `LE Remove Advertising Set` handle 0
## Z3
* `LE Rand`
* `LE Set Advertising Parameters` ADV_NONCONN_IND, interval 250-281.25 msec, channels 37,38,39, random device address
* `LE Set Random Address`
* `LE Set Advertising Data`
* `LE Set Scan Response Data`
* `LE Set Advertise Enable` on
[10min]
* `LE Set Advertise Enable` off

# Scanning: sequence of HCI commands
Every 3 minutes (not aligned):
## Pixel4
* Vendor command 0x0157 (4x)
* `LE Set Extended Scan Parameters` active, random device address, accept all adv (except direct not addressed here)
* `LE Set Extended Scan Enable` on
* `LE Set Extended Scan Enable` off
* `LE Set Extended Scan Parameters` active, random device address, accept all adv (except direct not addressed here)
* `LE Set Extended Scan Parameters` active, random device address, accept all adv (except direct not addressed here)
* `LE Set Extended Scan Enable` on
[20s]
* `LE Set Extended Scan Enable` off
## Z3
* `LE Set Scan Parameters` active, random device address, accept all adv (except direct not addressed here)
* `LE Set Scan Enable` on
* `LE Set Scan Enable` off
* `LE Set Scan Parameters` active, random device address, accept all adv (except direct not addressed here)
* `LE Set Scan Parameters` active, random device address, accept all adv (except direct not addressed here)
* `LE Set Scan Enable` on
[20s]
* `LE Set Scan Enable` off

# Scanning events received
## Pixel4
`LE Meta` -- `LE Extended Advertising Report` legacy, ADV_NONCONN_IND, random device address, 
## Z3
`LE Meta` -- `LE Advertising Report` ADV_NONCONN_IND, random device address, 

# Advertisements recorded from the sniffer, channel 37
Interval distribution over an RPI value (10 min):
## Pixel4
mean: 287.21ms, median: 286,25ms
## Z3
mean: 287.80ms, median: 286.26ms

# Other
Every 15 minutes (not aligned):
## Pixel4
* `LE Set Random Address`
## Z3
* `LE Set Random Address`

**NOTE**: On the Z3, this has the effect of also changing the advertising random address in the middle of a 10-minute RPI cycle, without changing the RPI. This is probably due to it having an older Bluetooth HW and using legacy commands, which do not distinguish between setting the random address for advertising and for scanning.

# RPI / BD Address overlap

* The same BD address used with different advertised RPIs was never observed.
* The same RPI value advertised with two different BD addresses was observed on the Z3, as indicated in the previous note.

In other words, whenever the RPI changes, the BD address changes as well, on both devices. On the Z3 however, sometimes the BD address will change while broadcasting a given RPI.

This behaviour is [expected](https://github.com/google/exposure-notifications-internals/blob/main/README.md#ble-mac-and-rpi-rotation) from GAEN as well.
