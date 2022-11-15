#!/usr/bin/python3

# import logging
import os
import sys
# import time
# import datetime

working_dir = os.path.dirname(os.path.realpath(__file__))
path_lib_epd = os.path.join(working_dir, 'lib')
if os.path.exists(path_lib_epd):
    sys.path.append(path_lib_epd)

import waveshare_epd.epd4in2b_V2

epd = waveshare_epd.epd4in2b_V2.EPD()
epd.init()
epd.Clear()
epd.sleep()
