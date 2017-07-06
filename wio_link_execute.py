#!/usr/bin/env python
# copyright 2015 seeed, wangtengoo7@gmail.com
import sys
import requests
import threading

#red_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital0/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
#red_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital0/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
#orange_led_on_api = "https:/red_led_off_api, blue_led_on_api, green_led_off_api/cn.iot.seeed.cc/v1/node/GroveRelayDigital1/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
#orange_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital1/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
#green_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital2/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
#green_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital2/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"

red_led_on_api = "https://us.wio.seeed.io/v1/node/GroveLedWs2812D1/clear/30/ff0000?access_token=7f2a22a2023ea0989834636ac779fcb4"
blue_led_on_api = "https://us.wio.seeed.io/v1/node/GroveLedWs2812D1/clear/30/0000ff?access_token=7f2a22a2023ea0989834636ac779fcb4"
green_led_on_api = "https://us.wio.seeed.io/v1/node/GroveLedWs2812D1/clear/30/00ff00?access_token=7f2a22a2023ea0989834636ac779fcb4"
led_reset_api = "https://us.wio.seeed.io/v1/node/GroveLedWs2812D1/clear/30/000000?access_token=7f2a22a2023ea0989834636ac779fcb4"


def post_url(url):
    r = requests.post(url)
    print r.status_code
    if r.status_code != 200:
        requests.post(url)


def main(argv):
    status = argv
    if status == "success":
        urls =[green_led_on_api]
    elif status == "failure":
        urls =[red_led_on_api]
    elif status == "building":
        urls =[blue_led_on_api]

    for url in urls:
        threading.Thread(target=post_url, args=(url,)).start()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python wio_link_execute [success/failure/building]'
        exit(1)
    main(sys.argv[1])
