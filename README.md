# oxygen
CircuitPython script to translate Atlas Scientific Dissolved Oxygen Probe [[https://www.atlas-scientific.com/product_pages/kits/do_kit.html]] data into pretty colors on an RGB LED strip

It is easiest to run this off of a Metro M0 Express [[https://www.adafruit.com/product/3505t]] what with the LED strip wanting 12V power anyway.

An i2c 7 segment display [[https://www.adafruit.com/product/3140]] is super useful as well for live troubleshooting (you won't know what the actual DO value is unless your color perception is extraordinary).

# TODO

- Hook up a button for air calibration, since the Atlas Scientific probe drifts a tiny bit over time
- Same for the Temp and Salinity compensation, if it turns out to be an issue in the creek
- 600ms is the response time for the probe, which is pretty fast you but you still see it update. Fade-in steps on each cycle would be dope.
