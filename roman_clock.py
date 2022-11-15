#!/usr/bin/python3

import logging
import os
import sys
import time

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import random

working_dir = os.path.dirname(os.path.realpath(__file__))
path_lib_epd = os.path.join(working_dir, 'lib')
if os.path.exists(path_lib_epd):
    sys.path.append(path_lib_epd)

import waveshare_epd.epd4in2b_V2

def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError("expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

def time_in_roman():
    """ Convert a time to roman """
    """ Return hour, minute as string """

    now = time.localtime()
    if now.tm_hour == 0:
        hour = " "
    else:
        hour = int_to_roman(now.tm_hour)
    if now.tm_min == 0:
        minute = " "
    else:
        minute = int_to_roman(now.tm_min)

    return hour, minute

def output_roman(LBlackimage, LRYimage):

    drawblack = PIL.ImageDraw.Draw(LBlackimage)
    drawry = PIL.ImageDraw.Draw(LRYimage)

    font60 = PIL.ImageFont.truetype('FreeMonoBold.ttf', 60)
    font40 = PIL.ImageFont.truetype('FreeMonoBold.ttf', 20  )

    output_move = random.randint(0, 100)

    hour, minute = time_in_roman()

    drawblack.text((15, 0 + output_move), "Time is:", font = font40, fill = 0)
    drawblack.text((320, 60 + output_move), "hour", font = font40, fill = 0)
    drawblack.text((320, 120 + output_move), "minute", font = font40, fill = 0)

    drawry.text((20, 60 + output_move), '{:>8}'.format(hour), font = font60, fill = 0)
    drawry.text((20, 120 + output_move), '{:>8}'.format(minute), font = font60, fill = 0)

    return LBlackimage, LRYimage

def main():

    epd = waveshare_epd.epd4in2b_V2.EPD()
    epd.init()
    epd.Clear()

    # Color:
    #     0 = black
    #   255 = white

    while True:

        epd.init()

        LBlackimage = PIL.Image.new('1', (epd.width, epd.height), 255)  # 400*300
        LRYimage = PIL.Image.new('1', (epd.width, epd.height), 255)  # 400*300

        LBlackimage, LRYimage = output_roman(LBlackimage, LRYimage)

        epd.display(epd.getbuffer(LBlackimage), epd.getbuffer(LRYimage))
        epd.sleep()
        time.sleep(45)
        # epd.Clear()

if __name__ == '__main__':
        main()