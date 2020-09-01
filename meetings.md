# Meetings

## 2020-09-01 (Linus and Christian)

* steps
    * write Java mock classes for GAEN 1.6
    * ignore 1.1 specific data structures for now

* questions
    * what about device-specific calibration values

## First meeting (Linus)

* Android: 
    * Google Play Services
    * Implement a library that is API compatible that relies on the Google / Bluetooth LE API
        * Creating daily keys
        * Rotating beacons
        * Metadata encryption
        * 2-3 full days of implementation
        * 2-3 days of testing
    * What to do with the background running? Just ignore it for the moment
    * 95% of the library is transparency
    * -> Offering an alternative
    * Setting up an activity of the
        * Regular scanning
        * Sending of beacons
    * Target 1.6 GAEN API
    * -> GAEN-lib channel on DP3T-slack
* iOS: 

- Track both the library and the app in one repo
- LGPL v3 or later

Create repo under DP-3T with different folders
- Python
- Documents
- Android-library
- Android-test-app
- Example backend (user fake backend)

Open Source GAEN implementation
