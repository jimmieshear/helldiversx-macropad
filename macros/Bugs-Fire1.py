# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Bugs-Fire1',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.REINFORCE),
        h.prepare_macro(h.SEAF),
        h.prepare_macro(h.GATLING_SENTRY),

        # 2nd row ----------
        h.prepare_macro(h.AR23_GUARD_DOG),
        h.prepare_macro(h.GRENADE_LAUNCHER),
        h.prepare_macro(h.STALWART),

        # 3rd row ----------
        h.prepare_macro(h.EAGLE_NAPALM_STRIKE),
        h.prepare_macro(h.ORBITAL_NAPALM_BARRAGE),
        h.prepare_macro(h.EAGLE_500KG),

        # 4th row ----------
        h.prepare_macro(h.ORBITAL_HE120_BARRAGE),
        h.prepare_macro(h.ORBITAL_HE380_BARRAGE),
        h.prepare_macro(h.ORBITAL_LASER),
    ]
}
