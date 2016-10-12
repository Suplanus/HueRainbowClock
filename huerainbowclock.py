#############################################################################
# HueRainbowClock
#############################################################################

import os
import datetime
import time

from phue import Bridge

import colorama
from colorama import Fore, Back, Style

from rgb_cie import Converter

HUEBRIDGEIP = "192.168.178.79"
LIGHTNAME = "Buro"

LAMP = ""

# Executes hour changed
def DingDong():
	global hourBefore

	# Turn lamp on
	LAMP.brightness = 254

	# Change color
	converter = Converter()

	if hour == 1 or hour == 13:
		xy = converter.rgbToCIE1931(255,0,0)

	if hour == 2 or hour == 14:
		xy = converter.rgbToCIE1931(255,128,0)

	if hour == 3 or hour == 15:
		xy = converter.rgbToCIE1931(255,255,0)

	if hour == 4 or hour == 16:
		xy = converter.rgbToCIE1931(128,255,0)

	if hour == 5 or hour == 17:
		xy = converter.rgbToCIE1931(0,255,0)

	if hour == 6 or hour == 18:
		xy = converter.rgbToCIE1931(0,255,128)

	if hour == 7 or hour == 19:
		xy = converter.rgbToCIE1931(0,255,255)

	if hour == 8 or hour == 20:
		xy = converter.rgbToCIE1931(0,128,255)

	if hour == 9 or hour == 21:
		xy = converter.rgbToCIE1931(0,0,255)

	if hour == 10 or hour == 22:
		xy = converter.rgbToCIE1931(128,0,255)

	if hour == 11 or hour == 23:
		xy = converter.rgbToCIE1931(255,0,255)

	if hour == 12 or hour == 24:
		xy = converter.rgbToCIE1931(255,0,128)

	LAMP.xy = xy

	# Log
	text = "==> " + str(hour) + " ==> " + str(xy)
	print(Fore.LIGHTBLUE_EX + text + Style.RESET_ALL)

	# Save for check later
	hourBefore = hour

# Init hue
print(Fore.LIGHTBLUE_EX + 'Init hue' + Style.RESET_ALL)
Bridge = Bridge(HUEBRIDGEIP)
Bridge.connect() # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
Bridge.get_api() # Get the bridge state (This returns the full dictionary that you can explore)

# Get a dictionary with the light name as the key
light_names = Bridge.get_light_objects('name')

# Get light object
LAMP = light_names[LIGHTNAME]

# Do it to the end of time
print(Fore.LIGHTBLUE_EX + 'Read time' + Style.RESET_ALL)
hourBefore = ""

while(True):
	# Check time
	now = datetime.datetime.now()
	hour = int(now.strftime("%H"))

	# Test
	#for i in range(1,12):
	#	hour = i
	#	DingDong()
	#	time.sleep(2)

	# Check if already set
	if hour == hourBefore:
		continue # do nothing

	# Doit
	DingDong()
