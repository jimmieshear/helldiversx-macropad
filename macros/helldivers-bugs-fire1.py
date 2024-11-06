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
    'name' : 'Bugs-Fire1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.YELLOW, 'Reinf',     stratagem(h.REINFORCE)),
        (h.YELLOW, 'SEAF',      stratagem(h.SEAF)),
        (h.GREEN,  'GatSen',    stratagem(h.GATLING_SENTRY)),

        # 2nd row ----------
        (h.BLUE,   'Gudog',     stratagem(h.AR23_GUARD_DOG)),
        (h.GREEN,  'Grenade',   stratagem(h.GRENADE_LAUNCHER)),        
        (h.GREEN,  'Stawl',     stratagem(h.STALWART)),

        # 3rd row ----------
        (h.ORANGE, 'Nape',      stratagem(h.EAGLE_NAPALM_STRIKE)),
        (h.RED,    'Barage',    stratagem(h.ORBITAL_NAPALM_BARRAGE)),
        (h.ORANGE, '500',       stratagem(h.EAGLE_500KG)),

        # 4th row ----------
        (h.RED,    'ORB120',    stratagem(h.ORBITAL_HE120_BARRAGE)),
        (h.RED,    'ORB380',    stratagem(h.ORBITAL_HE380_BARRAGE)),
        (h.RED,    'ORBLas',     stratagem(h.ORBITAL_LASER)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}