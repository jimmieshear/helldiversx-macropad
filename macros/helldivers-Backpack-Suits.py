# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Backpacks-Suits',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.BLUE, 'GD-Laz',    h.stratagem(h.LAS_5_GUARD_DOG)),
        (h.BLUE, 'GD-Gun',    h.stratagem(h.AR23_GUARD_DOG)),
        (h.BLUE, 'GD-Gas',    h.stratagem(h.GAS_GUARD_DOG)),

        # 2nd row ----------
        (h.BLUE, 'Suply',     h.stratagem(h.SUPPLY_PACK)),
        (h.BLUE, 'Sheld',     h.stratagem(h.SHIELD_GENERATOR)),
        (h.BLUE, 'BalShi',    h.stratagem(h.BALLISTIC_SHIELD)),

        # 3rd row ----------
        (h.BLUE, 'Jump',      h.stratagem(h.JUMP_PACK)),
        (h.BLUE, 'Patr',      h.stratagem(h.EX045_PATRIOT)),
        (h.BLUE, 'Eman',      h.stratagem(h.EXO49_EMANCIPATOR)),

        # 4th row ----------
        (h.YELLOW, '',          []),
        (h.YELLOW, '',          []),
        (h.YELLOW, '',          []),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}