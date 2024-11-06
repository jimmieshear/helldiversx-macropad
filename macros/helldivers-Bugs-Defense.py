# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Weapons',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.GREEN, 'AutoCan',   h.stratagem(h.AUTOCANNON)),
        (h.GREEN, 'RailGun',   h.stratagem(h.RAILGUN)),
        (h.GREEN, 'Stalwar',   h.stratagem(h.STALWART)),

        # 2nd row ----------
        (h.GREEN, 'Expend',    h.stratagem(h.EXPENDABLE_ANTI_TANK)),
        (h.GREEN, '4-shot',    h.stratagem(h.COMMANDO)),
        (h.GREEN, 'Recoil',    h.stratagem(h.RECOILLESS)),

        # 3rd row ----------
        (h.GREEN, 'Airbur',    h.stratagem(h.AIRBURST_ROCKET)),
        (h.GREEN, 'Spear',     h.stratagem(h.SPEAR)),
        (h.GREEN, 'HeavyM',    h.stratagem(h.HEAVY_MACHINE_GUN)),

        # 4th row ----------
        (h.GREEN, 'Grenad',    h.stratagem(h.GRENADE_LAUNCHER)),
        (h.GREEN, 'Quasar',    h.stratagem(h.QUASAR_CANNON)),
        (h.GREEN, 'Arc',       h.stratagem(h.ARC_THROWER)),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}