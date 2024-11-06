# https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad
# MACROPAD Hotkeys: Helldiver II

import lib.hell_constants as h

app = {
    'name' : 'Defensive',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (h.GREEN, 'Gat',       h.stratagem(h.GATLING_SENTRY)),
        (h.GREEN, 'MacG',      h.stratagem(h.MACHINE_GUN_SENTRY)),
        (h.GREEN, 'AutoC',     h.stratagem(h.AUTOCANNON_SENTRY)),

        # 2nd row ----------
        (h.GREEN, 'Mort',      h.stratagem(h.MORTAR_SENTRY)),
        (h.GREEN, 'Rocket',    h.stratagem(h.ROCKET_SENTRY)),
        (h.GREEN, 'EMS',       h.stratagem(h.EMS_MORTAR_SENTRY)),

        # 3rd row ----------
        (h.GREEN, 'AntiT',     h.stratagem(h.ANTI_TANK_MINE)),
        (h.GREEN, 'Fire',      h.stratagem(h.INCENDIARY_MINE)),
        (h.GREEN, 'Persn',     h.stratagem(h.ANTI_PERSONNEL_MINE)),

        # 4th row ----------
        (h.GREEN, 'Shild',     h.stratagem(h.SHIELD_GENERATOR_RELAY)),
        (h.GREEN, 'Tesla',     h.stratagem(h.TESLA_TOWER)),
        (h.GREEN, 'Emplac',    h.stratagem(h.MG_101_EMPLACEMENT)),
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}