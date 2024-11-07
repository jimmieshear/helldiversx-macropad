# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Bugs-Fire1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.YELLOW, 'Reinf',     h.stratagem(h.REINFORCE)),
        (h.YELLOW, 'SEAF',      h.stratagem(h.SEAF)),
        (h.GREEN,  'GatSen',    h.stratagem(h.GATLING_SENTRY)),

        # 2nd row ----------
        (h.BLUE,   'Gudog',     h.stratagem(h.AR23_GUARD_DOG)),
        (h.GREEN,  'Grenade',   h.stratagem(h.GRENADE_LAUNCHER)),        
        (h.GREEN,  'Stawl',     h.stratagem(h.STALWART)),

        # 3rd row ----------
        (h.ORANGE, 'Nape',      h.stratagem(h.EAGLE_NAPALM_STRIKE)),
        (h.RED,    'Barage',    h.stratagem(h.ORBITAL_NAPALM_BARRAGE)),
        (h.ORANGE, '500',       h.stratagem(h.EAGLE_500KG)),

        # 4th row ----------
        (h.RED,    'ORB120',    h.stratagem(h.ORBITAL_HE120_BARRAGE)),
        (h.RED,    'ORB380',    h.stratagem(h.ORBITAL_HE380_BARRAGE)),
        (h.RED,    'ORBLas',    h.stratagem(h.ORBITAL_LASER)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}
