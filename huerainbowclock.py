#############################################################################
# HueRainbowClock
#############################################################################

import os
import datetime
import time

from phue import Bridge

import colorama
from colorama import Fore, Back, Style

HUEBRIDGEIP = "192.168.178.79"
LIGHTNAME = "Buro"

# Executes hour changed
def DingDong():
	global hourBefore

	# Set lamp
	Bridge.set_light(LIGHTNAME,'bri', 254) # turn light on

	# Calc the saturation https://en.wikipedia.org/wiki/Hue
	saturation = int(round((254/24) * hour))
	Bridge.set_light(LIGHTNAME,'sat', saturation) # turn light on

	# Log
	text = "==> " + str(hour) + " ==> " + str(saturation)
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

# Set the birghtness of the bulb named "Kitchen"
light_names[LIGHTNAME].brightness = 100

# Do it to the end of time
print(Fore.LIGHTBLUE_EX + 'Read time' + Style.RESET_ALL)
hourBefore = ""

while(True):
	# Check time
	now = datetime.datetime.now()
	hour = int(now.strftime("%H"))

	# Check if already set
	if hour == hourBefore:
		continue # do nothing

	# Only display from 7am to 6pm
	if hour >= 7 or hour <= 18:
		DingDong()
	else:
		print("==> " + str(hour) + " ==> Sleeping")
		Bridge.set_light(LIGHTNAME,'on', False) # turn light off
