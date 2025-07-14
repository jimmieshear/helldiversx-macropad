# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Weapons',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.AUTOCANNON),
        h.prepare_macro(h.RAILGUN),
        h.prepare_macro(h.STALWART),

        # 2nd row ----------
        h.prepare_macro(h.FLAMETHROWER),
        h.prepare_macro(h.COMMANDO),
        h.prepare_macro(h.RECOILLESS),

        # 3rd row ----------
        h.prepare_macro(h.AIRBURST_ROCKET),
        h.prepare_macro(h.SPEAR),
        h.prepare_macro(h.HEAVY_MACHINE_GUN),

        # 4th row ----------
        h.prepare_macro(h.GRENADE_LAUNCHER),
        h.prepare_macro(h.QUASAR_CANNON),
        h.prepare_macro(h.ARC_THROWER),
    ]
}