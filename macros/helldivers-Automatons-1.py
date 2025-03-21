# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Automatons-Solo1',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.SEAF),
        h.prepare_macro(h.WASP_LAUNCHER),
        h.prepare_macro(h.ROCKET_SENTRY),

        # 2nd row ----------
        h.prepare_macro(h.AUTOCANNON),
        h.prepare_macro(h.AIRBURST_ROCKET),
        h.prepare_macro(h.GATLING_SENTRY),

        # 3rd row ----------
        h.prepare_macro(h.ANTI_MATERIAL),
        h.prepare_macro(h.EAGLE_NAPALM_STRIKE),
        h.prepare_macro(h.EAGLE_500KG),

        # 4th row ----------
        h.prepare_macro(h.AR23_GUARD_DOG),
        h.prepare_macro(h.ORBITAL_HE120_BARRAGE),
        h.prepare_macro(h.EAGLE_STRAFING_RUN),
    ]
}
