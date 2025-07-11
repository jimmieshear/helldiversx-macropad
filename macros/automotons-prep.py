# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Automatons-Prep',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.AUTOCANNON),
        h.prepare_macro(h.QUASAR_CANNON),
        h.prepare_macro(h.RECOILLESS),

        # 2nd row ----------
        h.prepare_macro(h.AR23_GUARD_DOG),
        h.prepare_macro(h.LAS_5_GUARD_DOG),
        h.prepare_macro(h.SPEAR),

        # 3rd row ----------
        h.prepare_macro(h.WASP_LAUNCHER),
        h.prepare_macro(h.STALWART),
        h.prepare_macro(h.HEAVY_MACHINE_GUN),

        # 4th row ----------
        h.prepare_macro(h.HELLBOMB),
        h.prepare_macro(h.SUPPLY_PACK),
        h.prepare_macro(h.EX045_PATRIOT),
    ]
}