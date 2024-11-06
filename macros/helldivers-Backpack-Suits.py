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
    'name' : 'Backpacks-Suits',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.BLUE, 'GD-Laz',      stratagem(h.LAS_5_GUARD_DOG)),
        (h.BLUE, 'GD-Gun',      stratagem(h.AR23_GUARD_DOG)),
        (h.BLUE, 'GD-Gas',      stratagem(h.GAS_GUARD_DOG)),

        # 2nd row ----------
        (h.BLUE, 'Suply',     stratagem(h.SUPPLY_PACK)),
        (h.BLUE, 'Sheld',     stratagem(h.SHIELD_GENERATOR)),
        (h.BLUE, 'BalShi',    stratagem(h.BALLISTIC_SHIELD)),

        # 3rd row ----------
        (h.BLUE, 'Jump',      stratagem(h.JUMP_PACK)),
        (h.BLUE, 'Patr',      stratagem(h.EX045_PATRIOT)),
        (h.BLUE, 'Eman',      stratagem(h.EXO49_EMANCIPATOR)),

        # 4th row ----------
        (h.YELLOW, '',          []),
        (h.YELLOW, '',          []),
        (h.YELLOW, '',          []),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}