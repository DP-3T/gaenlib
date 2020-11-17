# Study of existing implementations (see [issue](https://github.com/DP-3T/gaenlib/issues/1))

## [microG](https://microg.org/)
Open-source project aiming to provide a free implementation of Google Play Services.

  - Requires an OS with a "Signature Spoofing" patch applied (or microG preinstalled, such as [LineageOS for microG](https://lineage.microg.org/)).
  - Provides a transparent "drop-in" replacement, allowing original apps to run unmodified on non-GMS phones. The app is linked with the GMS client library, and the "Signature Spoofing" allows to redirect to microG.
  - Appears to be 1 main developer (microG's author) + some others.
  - The GAEN implementation (`gms.nearby`) started about 1-2 months ago. It targets "v1 mode" only so far (as it seems to be what all existing apps use, including the current version of SwissCovid).
  - GAEN is fairly advanced, able to run existing corona apps (Germany's Corona-Warn-App, Italy's Immuni).
  - Without installing microG, there is a possibility for an "almost transparent" approach by bundling the EN-relevant part as a library, along with a client library, and packaging all together with an existing app. However, such an app would likely not be accepted on Google Play due to it not using the official lib, but it could possibly be made to be accepted on F-Droid. The client library has been started but is not yet complete and requires further work.

Interesting [issue](https://github.com/microg/android_packages_apps_GmsCore/issues/1057) with discussion regarding EN.

## [CoraLibre](https://github.com/CoraLibre/CoraLibre-android-sdk)
Open-souce project aiming to provide a free implementation of an EN SDK for corona contact-tracing apps

  - Started with a pre-GAEN version of the DP3T SDK, and is working to adapt it.
  - Wishes to also produce a [fork](https://github.com/CoraLibre/CoraLibre-android) of Germany's Corona-Warn-App using the SDK.
  - Aims to provide an API as close as possible to GAEN. It targets "v1 mode" only so far.
  - Applications will require some (hopefully minor) changes to adapt to the library.
  - Crypto and Bluetooth parts are fairly advanced, client API (along with some implementation of the Tasks API) is just at the beginning.

There is a Matrix [channel](https://app.element.io/#/room/#coralibre:matrix.org) for CoraLibre discussion. The microG main developer is also connected and participates to the discussion.

## [Google libraries](https://github.com/google/exposure-notifications-internals/pull/15)
Contains a snapshot of code from Google Play Services' Exposure Notifications module.

  - This is not a usable product, but is provided as a reference that can be used with the GAEN specs.
  - Doesn't build ([issue](https://github.com/google/exposure-notifications-internals/issues/13) opened) ([fixed](https://github.com/google/exposure-notifications-internals/commit/da29e8f8ec2a3e970e1a435d5e40013b1a0e6172) now).
  - Some parts (key matching) are implemented in C++ via JNI for performance reasons.
