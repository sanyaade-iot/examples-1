################################################################################
# Digital Read Basics
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams

streams.serial()

pinMode(D5, INPUT_PULLUP)

while True:
    print(digitalRead(D5))
    sleep(500)  