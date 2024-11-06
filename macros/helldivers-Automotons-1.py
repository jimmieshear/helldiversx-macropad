# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Automotons-1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.YELLOW, 'Reinf',     h.stratagem(h.REINFORCE)),
        (h.YELLOW, 'SEAF',      h.stratagem(h.SEAF)),
        (h.GREEN, 'GatSen',     h.stratagem(h.GATLING_SENTRY)),

        # 2nd row ----------
        (h.BLUE, 'Gudog',       h.stratagem(h.AR23_GUARD_DOG)),
        (h.BLUE, 'AutoCa',      h.stratagem(h.AUTOCANNON)),        
        (h.GREEN,'AUTOSEN',     h.stratagem(h.AUTOCANNON_SENTRY)),

        # 3rd row ----------
        (h.RED,     'Nape',     h.stratagem(h.EAGLE_NAPALM_STRIKE)),
        (h.ORANGE, 'Barage',    h.stratagem(h.ORBITAL_NAPALM_BARRAGE)),
        (h.RED,     '500',      h.stratagem(h.EAGLE_500KG)),

        # 4th row ----------
        (h.ORANGE, 'ORB120',    h.stratagem(h.ORBITAL_HE120_BARRAGE)),
        (h.ORANGE, 'ORB380',    h.stratagem(h.ORBITAL_HE380_BARRAGE)),
        (h.GREEN,  'EXOPAT',    h.stratagem(h.EX045_PATRIOT)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}