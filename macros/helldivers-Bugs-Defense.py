# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Bug-TowerDefense',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.BLUE,    'AutoCan',  h.stratagem(h.AUTOCANNON)),
        (h.BLUE,    'Recoil',   h.stratagem(h.RECOILLESS)),
        (h.BLUE,    'Airbur',   h.stratagem(h.AIRBURST_ROCKET)),

        # 2nd row ----------
        (h.BLUE,    'Expend',   h.stratagem(h.EXPENDABLE_ANTI_TANK)),
        (h.BLUE,    '4-shot',   h.stratagem(h.COMMANDO)),
        (h.GREEN,   'MG101Em',  h.stratagem(h.MG_101_EMPLACEMENT)),

        # 3rd row ----------
        (h.RED,     '500',      h.stratagem(h.EAGLE_500KG)),
        (h.RED,     'Staf',     h.stratagem(h.EAGLE_STRAFING_RUN)),
        (h.RED,     'HeavyM',   h.stratagem(h.HEAVY_MACHINE_GUN)),

        # 4th row ----------
        (h.GREEN,   'Mortr',    h.stratagem(h.MORTAR_SENTRY)),
        (h.GREEN,   'GatSen',   h.stratagem(h.GATLING_SENTRY)),
        (h.GREEN,   'TeslaT',   h.stratagem(h.TESLA_TOWER)),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}