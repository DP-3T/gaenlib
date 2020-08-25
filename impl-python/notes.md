# Notes

## Exposure Notification

### BT Spec

* Contact Tracing -> Exposure Notification

* Rolling period: 15 minutes

* Rolling Proximity Identifier (RPI)
    * 16 bytes
    * 1 key / day
    * 1 rpi / 15 minutes

* Associated Encrypted Metadata (AEM)
    * 4 bytes
        * B0: 7:6 major ver, 5:4 minor ver, 3:0 reserved
        * B1: measured tx-power, [-127, 127] dBm
        * B2: reserved
        * B3: reserved
    * Tx power, protocol version
    * Synch with the proximity identifier

* Exposure Notification UUID
    * 16-bit `0xFD6F`
    * Device advertise and scan filtering by this UUID
    * Associated data: AEM

* BLE Advertising 
    * payload
        * See figure
    * adv type
        * `ADV_NONCONN_IND`
    * addr type
        * RANDOM, non resolvable
    * addr rotation (when supported)
        * rand btw 10 and 20 minutes
    * synchronized rotations
        * addr, rpi, aem
    * adv interval (might change)
        * 200-270 msec

* BLE Scanning
    * scan payload 
        * should be kept in the device
        * should be timestamped and RSSI-captured
    * scan interval and window
        * not set
    * recommended scan strategy
        * `OPPORTUNISTC` with min periodic sampling every 5 minutes


### Crypto Spec

* Keys
    * Temporary Exposure  Key (TEK)
        * generated every `EKRollingPeriod`
    * Rolling Proximity Identifier Key (RPIK)
        * HKDF-derived from TEK and discrete time
    * Associated Encrypted Metadata Key (AEMK)
        * HKDF-derived from TEK and discrete time

* Values (rotate with MAC address change)
    * Rolling Proximity Identifier (RPI)
    * Associated Encrypted Metadata (AEM)
    * Tx/rx/storage is encrypted 
    * Decrypted only when user tested positive

* Time discrete cation
    * 10-min intervals
    * starting from Unix epoch time

* Key generation
    * `kg.py`
    * `kg_tests.py`


* RPI gen
    * `rpi.py`
    * `rpi_tests.py`

### Android API

* BLE implemented in the Google Play Services (GPS)

* Permissions
    * required: `BLUETOOTH`
    * not required: `BLUETOOTH_ADMIN` and `ACCESS_*_LOCATION`

* Min versions
    * API 21
    * Android 5.0

* GPS handles (no UI)
    * daily TEKs
    * rotating RPIs
    * secure storage
    * interface with the backend
    * scanning
    * advertising
    * calculate exposure risk score
    * provide exposure risk score to the app
    * ask users for permissions

* App (UI)
    * let user accept permissions
    * start/stop scanning

* App (logic)
    * manage risk scores
    * provides keys, start numbers, key transmission risk level to GPS

* medical provider auth
    * app must authenticate that the holder of the device has been positively
        diagnosed

* Internet accessible server
    * sends to the app diagnosis keys

* `ExposureConfiguration`
    * `erl.py`


### Apple API

TODO


### 2020-05-06 DA Recommendations

* Bluetooth spec
    * What values are you going to put into AEM's B2 and B3?
    * What happens if a device does not support random private address?
    * Better explanation of synchronization btw BTADD, RPI and AEM?
        * If BTADD rotation is a random value, why don't we use it as a global
        ROTATION_PERIOD variable to set also RPI and AEM rotations?
    * Scan power consideration
        * Add also AEM as a required value to be rotated

* Crypto spec
    * Not clear from the HKDF diagram that RPIK is different from AEDK

* Android API
    * keep the key terminology consistent across Bluetooth, Crypto, and Android


### Crypto Spec

Bla
