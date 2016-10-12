# HueRainbowClock
### Python script which change the color of Hue lamp every hour 🦄

# Installing
* Install [colorama](https://pypi.python.org/pypi/colorama)
* Set your IP address of your hue bridge to variable HUEBRIDGEIP
* Set your light name to variable LIGHTNAME
* Register your script to the hue bridge: Press the button and run the script
* Startup
    - Open crontab: `export VISUAL=nano; crontab -e`
    - Set your script to run on reboot: `@reboot python3 "/my/path/huerainbowclock.py"`
