[app]
title = LSL Streamer
package.name = lslstreamer
package.domain = org.lsl
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv,atlas,so
# (list) Application requirements
requirements = python3,kivy==2.3.0,pylsl

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 24

android.add_libs_arm64_v8a = liblsl.so

# CRITICAL FIX: Pin NDK to r25b (NDK r28 breaks C++ cross-compilation in p4a)
android.ndk = 25b
android.ndk_path = 

# (str) Supported architectures
android.archs = arm64-v8a

# (list) Permissions needed for LSL network sockets
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
