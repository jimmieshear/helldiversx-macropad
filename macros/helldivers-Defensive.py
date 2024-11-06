# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II
# Blue == 0x000020 
# Red == 0x200000
# Green == 0x002000  && 0x002000
# Yellow == 0x302000

from adafruit_hid.keycode import Keycode
import lib.hell_constants as h

START_INPUT_DELAY = 0.4
KEY_DELAY = 0.05

START_INPUT = Keycode.CONTROL

#def stratagem(*argv):
def stratagem(input_s):
    keys = [START_INPUT, START_INPUT_DELAY]

    for key in input_s:
        keys += [key, KEY_DELAY, -key, KEY_DELAY]

    return keys

app = {
    'name' : 'Defensive',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.GREEN, 'Gat',       stratagem(h.GATLING_SENTRY)),
        (h.GREEN, 'MacG',      stratagem(h.MACHINE_GUN_SENTRY)),
        (h.GREEN, 'AutoC',     stratagem(h.AUTOCANNON_SENTRY)),

        # 2nd row ----------
        (h.GREEN, 'Mort',      stratagem(h.MORTAR_SENTRY)),
        (h.GREEN, 'Rocket',    stratagem(h.ROCKET_SENTRY)),
        (h.GREEN, 'EMS',       stratagem(h.EMS_MORTAR_SENTRY)),

        # 3rd row ----------
        (h.GREEN, 'AntiT',     stratagem(h.ANTI_TANK_MINE)),
        (h.GREEN, 'Fire',      stratagem(h.INCENDIARY_MINE)),
        (h.GREEN, 'Persn',     stratagem(h.ANTI_PERSONNEL_MINE)),

        # 4th row ----------
        (h.GREEN, 'Shild',     stratagem(h.SHIELD_GENERATOR_RELAY)),
        (h.GREEN, 'Tesla',     stratagem(h.TESLA_TOWER)),
        (h.GREEN, 'Emplac',    stratagem(h.MG_101_EMPLACEMENT)),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}