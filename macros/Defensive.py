# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Defensive',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.MACHINE_GUN_SENTRY),
        h.prepare_macro(h.GATLING_SENTRY),
        h.prepare_macro(h.AUTOCANNON_SENTRY),

        # 2nd row ----------
        h.prepare_macro(h.MORTAR_SENTRY),
        h.prepare_macro(h.ROCKET_SENTRY),
        h.prepare_macro(h.EMS_MORTAR_SENTRY),

        # 3rd row ----------
        h.prepare_macro(h.ANTI_TANK_MINE),
        h.prepare_macro(h.INCENDIARY_MINE),
        h.prepare_macro(h.ANTI_PERSONNEL_MINE),

        # 4th row ----------
        h.prepare_macro(h.SHIELD_GENERATOR_RELAY),
        h.prepare_macro(h.TESLA_TOWER),
        h.prepare_macro(h.MG_101_EMPLACEMENT),
    ]
}