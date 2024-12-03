# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Backpacks-Suits',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.LAS_5_GUARD_DOG),
        h.prepare_macro(h.AR23_GUARD_DOG),
        h.prepare_macro(h.GAS_GUARD_DOG),

        # 2nd row ----------
        h.prepare_macro(h.SUPPLY_PACK),
        h.prepare_macro(h.SHIELD_GENERATOR),
        h.prepare_macro(h.BALLISTIC_SHIELD),

        # 3rd row ----------
        h.prepare_macro(h.JUMP_PACK),
        h.prepare_macro(h.EX045_PATRIOT),
        h.prepare_macro(h.EXO49_EMANCIPATOR),
    ]
}
