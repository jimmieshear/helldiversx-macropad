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
    'name' : 'Weapons',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.GREEN, 'AutoCan',   stratagem(h.AUTOCANNON)),
        (h.GREEN, 'RailGun',   stratagem(h.RAILGUN)),
        (h.GREEN, 'Stalwar',   stratagem(h.STALWART)),

        # 2nd row ----------
        (h.GREEN, 'Expend',    stratagem(h.EXPENDABLE_ANTI_TANK)),
        (h.GREEN, '4-shot',    stratagem(h.COMMANDO)),
        (h.GREEN, 'Recoil',    stratagem(h.RECOILLESS)),

        # 3rd row ----------
        (h.GREEN, 'Airbur',    stratagem(h.AIRBURST_ROCKET)),
        (h.GREEN, 'Spear',     stratagem(h.SPEAR)),
        (h.GREEN, 'HeavyM',    stratagem(h.HEAVY_MACHINE_GUN)),

        # 4th row ----------
        (h.GREEN, 'Grenad',    stratagem(h.GRENADE_LAUNCHER)),
        (h.GREEN, 'Quasar',    stratagem(h.QUASAR_CANNON)),
        (h.GREEN, 'Arc',       stratagem(h.ARC_THROWER)),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}