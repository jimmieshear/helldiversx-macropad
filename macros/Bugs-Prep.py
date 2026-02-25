# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Bugs-Prep',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.LAS_5_GUARD_DOG),
        h.prepare_macro(h.HOVER_PACK),
        h.prepare_macro(h.GAS_GUARD_DOG),

        # 2nd row ----------
        h.prepare_macro(h.SPEAR),
        h.prepare_macro(h.GRENADE_WALL),
        h.prepare_macro(h.FLAMETHROWER),

        # 3rd row ----------
        h.prepare_macro(h.ARC_THROWER),
        h.prepare_macro(h.AIRBURST_ROCKET),
        h.prepare_macro(h.STALWART),

        # 4th row ----------
        h.prepare_macro(h.TX_STERILIZER),
        h.prepare_macro(h.ARC3_GUARD_DOG),
        h.prepare_macro(h.HEAVY_MACHINE_GUN),
    ]
}
