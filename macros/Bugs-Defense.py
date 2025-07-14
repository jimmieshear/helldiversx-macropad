# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Bug-TowerDefense',
    'macros' : [
        # 1st row ----------
        h.prepare_macro(h.AUTOCANNON),
        h.prepare_macro(h.RECOILLESS),
        h.prepare_macro(h.AIRBURST_ROCKET),

        # 2nd row ----------
        h.prepare_macro(h.EXPENDABLE_ANTI_T),
        h.prepare_macro(h.COMMANDO),
        h.prepare_macro(h.MG_101_EMPLACEMENT),

        # 3rd row ----------
        h.prepare_macro(h.EAGLE_500KG),
        h.prepare_macro(h.EAGLE_STRAFING_RUN),
        h.prepare_macro(h.HEAVY_MACHINE_GUN),

        # 4th row ----------
        h.prepare_macro(h.MORTAR_SENTRY),
        h.prepare_macro(h.GATLING_SENTRY),
        h.prepare_macro(h.TESLA_TOWER),
    ]
}