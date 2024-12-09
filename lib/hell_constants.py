# Dictionary of SRATAGEMS
from lib.adafruit_hid.keycode import Keycode

# COLORS
YELLOW = 0x302000
GREEN = 0x002000 
RED = 0x200000
BLUE = 0x3333FF
BLUETWO = 0x3399FF
ORANGE = 0xFF9714

START_INPUT_DELAY = 0.4
KEY_DELAY = 0.05
START_INPUT = Keycode.CONTROL

def stratagem(input_s) -> tuple:
    keys = [START_INPUT, START_INPUT_DELAY]

    for key in input_s:
        keys += [key, KEY_DELAY, -key, KEY_DELAY]

    return keys

def prepare_macro(input_dict) -> dict:
    key_series = stratagem(input_dict['keycode'])
    return_item = (input_dict['color'], input_dict['label'], key_series)
    return return_item

# BACKPACKS -- BLUE TWO   # COLOR           LABEL           KEY SEQUENCE
JUMP_PACK               = {'color':BLUETWO, 'label':'Jump', 'keycode':(Keycode.S, Keycode.W, Keycode.W, Keycode.S, Keycode.W)}
SUPPLY_PACK             = {'color':BLUETWO, 'label':'Suply', 'keycode':(Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.W, Keycode.S)}
BALLISTIC_SHIELD        = {'color':BLUETWO, 'label':'Balst', 'keycode':(Keycode.S, Keycode.A, Keycode.S, Keycode.S, Keycode.W, Keycode.A)}
SHIELD_GENERATOR        = {'color':BLUETWO, 'label':'Shild', 'keycode':(Keycode.S, Keycode.W , Keycode.A, Keycode.D, Keycode.A, Keycode.D)}
AR23_GUARD_DOG          = {'color':BLUETWO, 'label':'AR23', 'keycode':(Keycode.S, Keycode.W , Keycode.A, Keycode.W, Keycode.D, Keycode.S)}
LAS_5_GUARD_DOG         = {'color':BLUETWO, 'label':'Laz', 'keycode':(Keycode.S, Keycode.W, Keycode.A, Keycode.W, Keycode.D, Keycode.D)}
GAS_GUARD_DOG           = {'color':BLUETWO, 'label':'Gas', 'keycode':(Keycode.S, Keycode.W, Keycode.A, Keycode.W, Keycode.D, Keycode.W)}

# SUPPORT WEAPONS -- BLUE
MACHINE_GUN             = {'color':BLUE, 'label':'MaGun', 'keycode':(Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.D)}
ANTI_MATERIAL           = {'color':BLUE, 'label':'Anti', 'keycode':(Keycode.S, Keycode.A, Keycode.D, Keycode.W, Keycode.S)}
STALWART                = {'color':BLUE, 'label':'Stal', 'keycode':(Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.W, Keycode.A)}
EXPENDABLE_ANTI_T       = {'color':BLUE, 'label':'AntiT', 'keycode':(Keycode.S, Keycode.S, Keycode.A, Keycode.W, Keycode.D)}
COMMANDO                = {'color':BLUE, 'label':'Comdo', 'keycode':(Keycode.S, Keycode.A, Keycode.W, Keycode.S, Keycode.D)}
RECOILLESS              = {'color':BLUE, 'label':'Recol', 'keycode':(Keycode.S, Keycode.A, Keycode.D, Keycode.D, Keycode.A)}
FLAMETHROWER            = {'color':BLUE, 'label':'Flame', 'keycode':(Keycode.S, Keycode.A, Keycode.W, Keycode.S, Keycode.W)}
AUTOCANNON              = {'color':BLUE, 'label':'AutoC', 'keycode':(Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.W, Keycode.D)}
HEAVY_MACHINE_GUN       = {'color':BLUE, 'label':'HevyMa', 'keycode':(Keycode.S, Keycode.A, Keycode.W, Keycode.S, Keycode.S)}
RAILGUN                 = {'color':BLUE, 'label':'Railg', 'keycode':(Keycode.S, Keycode.D, Keycode.S, Keycode.W, Keycode.A, Keycode.D)}
SPEAR                   = {'color':BLUE, 'label':'Spear', 'keycode':(Keycode.S, Keycode.S, Keycode.W, Keycode.S, Keycode.S)}
GRENADE_LAUNCHER        = {'color':BLUE, 'label':'Grende', 'keycode':(Keycode.S, Keycode.A, Keycode.W, Keycode.A, Keycode.S)}
LASER_CANNON            = {'color':BLUE, 'label':'Lazer', 'keycode':(Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.A)}
ARC_THROWER             = {'color':BLUE, 'label':'Arc', 'keycode':(Keycode.S, Keycode.D, Keycode.S, Keycode.W, Keycode.A, Keycode.A)}
QUASAR_CANNON           = {'color':BLUE, 'label':'Quas', 'keycode':(Keycode.S, Keycode.S, Keycode.W, Keycode.A, Keycode.D)}
AIRBURST_ROCKET         = {'color':BLUE, 'label':'Airbur', 'keycode':(Keycode.S, Keycode.W, Keycode.W, Keycode.A, Keycode.D)}

# SUPPORT MECH -- BLUE
EX045_PATRIOT           = {'color':BLUE, 'label':'Patriot', 'keycode':(Keycode.A, Keycode.S, Keycode.D, Keycode.W, Keycode.A, Keycode.S, Keycode.S)}
EXO49_EMANCIPATOR       = {'color':BLUE, 'label':'Emanc', 'keycode':(Keycode.A, Keycode.S, Keycode.D, Keycode.W, Keycode.A, Keycode.S, Keycode.W)}

# MISSION -- YELLOW
REINFORCE               = {'color':YELLOW, 'label':'Rein', 'keycode':(Keycode.W, Keycode.S, Keycode.D, Keycode.A, Keycode.W)}
SOS                     = {'color':YELLOW, 'label':'SOS', 'keycode':(Keycode.W, Keycode.S, Keycode.D, Keycode.W)}
RESUPPLY                = {'color':YELLOW, 'label':'Resup', 'keycode':(Keycode.S, Keycode.S, Keycode.W, Keycode.D)}
HELLBOMB                = {'color':YELLOW, 'label':'Hellb', 'keycode':(Keycode.S, Keycode.W, Keycode.A, Keycode.S, Keycode.W, Keycode.D, Keycode.S, Keycode.W)}
SSSD                    = {'color':YELLOW, 'label':'SSSD', 'keycode':(Keycode.S, Keycode.S, Keycode.S, Keycode.W, Keycode.W)}
SIESMIC_PROBE           = {'color':YELLOW, 'label':'SiesP', 'keycode':(Keycode.W, Keycode.W, Keycode.A, Keycode.D, Keycode.S, Keycode.S)}
UPLOAD_DATA             = {'color':YELLOW, 'label':'Upload', 'keycode':(Keycode.A, Keycode.D, Keycode.W, Keycode.W, Keycode.W)}
EAGLE_REARM             = {'color':YELLOW, 'label':'EgRarm', 'keycode':(Keycode.W, Keycode.W, Keycode.A, Keycode.W, Keycode.D)}
SEAF                    = {'color':YELLOW, 'label':'SEAF', 'keycode':(Keycode.D, Keycode.W, Keycode.W, Keycode.S)}
FLAG                    = {'color':YELLOW, 'label':'Flag', 'keycode':(Keycode.S, Keycode.W, Keycode.S, Keycode.W)}

# DEFENSIVE -- GREEN
MG_101_EMPLACEMENT      = {'color':GREEN, 'label':'Emplac', 'keycode':(Keycode.S, Keycode.W, Keycode.A, Keycode.D, Keycode.D, Keycode.A)}
MACHINE_GUN_SENTRY      = {'color':GREEN, 'label':'MacSen', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.D, Keycode.W)}
GATLING_SENTRY          = {'color':GREEN, 'label':'GatSen', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.A)}
MORTAR_SENTRY           = {'color':GREEN, 'label':'MortSe', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.D, Keycode.S)}
AUTOCANNON_SENTRY       = {'color':GREEN, 'label':'AutoSe', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.W, Keycode.A, Keycode.W)}
ROCKET_SENTRY           = {'color':GREEN, 'label':'RockeS', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.D, Keycode.A)}
EMS_MORTAR_SENTRY       = {'color':GREEN, 'label':'EMSSen', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.S, Keycode.D)}
ANTI_PERSONNEL_MINE     = {'color':GREEN, 'label':'AntiPer', 'keycode':(Keycode.S, Keycode.A, Keycode.W, Keycode.D)}
INCENDIARY_MINE         = {'color':GREEN, 'label':'FireMin', 'keycode':(Keycode.S, Keycode.A, Keycode.A, Keycode.S)}
ANTI_TANK_MINE          = {'color':GREEN, 'label':'AntiTan', 'keycode':(Keycode.S, Keycode.A, Keycode.W, Keycode.W)}
GAS_MINE                = {'color':GREEN, 'label':'GasMin', 'keycode':(Keycode.S, Keycode.A, Keycode.A, Keycode.D)}
TESLA_TOWER             = {'color':GREEN, 'label':'TeslaT', 'keycode':(Keycode.S, Keycode.W, Keycode.D, Keycode.W, Keycode.A, Keycode.D)}
SHIELD_GENERATOR_RELAY  = {'color':GREEN, 'label':'Shild', 'keycode':(Keycode.S, Keycode.S, Keycode.A, Keycode.D, Keycode.A, Keycode.D)}

# OFFENSIVE ORBITAL -- RED
ORBITAL_GATLING_BARRAGE = {'color':RED, 'label':'Gatlin', 'keycode':(Keycode.D, Keycode.S, Keycode.A, Keycode.W, Keycode.W)}
ORBITAL_AIRBURST_STRIKE = {'color':RED, 'label':'Airbur', 'keycode':(Keycode.D, Keycode.D, Keycode.D)}
ORBITAL_HE120_BARRAGE   = {'color':RED, 'label':'120Bar', 'keycode':(Keycode.D, Keycode.D, Keycode.S, Keycode.A, Keycode.D, Keycode.S)}
ORBITAL_HE380_BARRAGE   = {'color':RED, 'label':'380Bar', 'keycode':(Keycode.D, Keycode.S, Keycode.W, Keycode.W, Keycode.A, Keycode.S, Keycode.S)}
ORBITAL_WALKING         = {'color':RED, 'label':'Walkin', 'keycode':(Keycode.D, Keycode.S, Keycode.D, Keycode.S, Keycode.D, Keycode.S)}
ORBITAL_LASER           = {'color':RED, 'label':'OrbLas', 'keycode':(Keycode.D, Keycode.S, Keycode.W, Keycode.D, Keycode.S)}
ORBITAL_RAILCANNON      = {'color':RED, 'label':'Railcan', 'keycode':(Keycode.D, Keycode.W, Keycode.S, Keycode.S, Keycode.D)}
ORBITAL_PRECISION       = {'color':RED, 'label':'Precis', 'keycode':(Keycode.D, Keycode.D, Keycode.W)}
ORBITAL_GAS_STRIKE      = {'color':RED, 'label':'GasStr', 'keycode':(Keycode.D, Keycode.D, Keycode.S, Keycode.D)}
ORBITAL_EMS_STRIKE      = {'color':RED, 'label':'EMSStr', 'keycode':(Keycode.D, Keycode.D, Keycode.A, Keycode.S)}
ORBITAL_SMOKE_STRIKE    = {'color':RED, 'label':'Smoke', 'keycode':(Keycode.D, Keycode.D, Keycode.S, Keycode.W)}
ORBITAL_NAPALM_BARRAGE  = {'color':RED, 'label':'Naplm', 'keycode':(Keycode.D, Keycode.D, Keycode.S, Keycode.A, Keycode.D, Keycode.W)}

# OFFENSIVE EAGLE -- ORANGE
EAGLE_STRAFING_RUN      = {'color':ORANGE, 'label':'straf', 'keycode':(Keycode.W, Keycode.D, Keycode.D)}
EAGLE_AIRSTRIKE         = {'color':ORANGE, 'label':'airstr', 'keycode':(Keycode.W, Keycode.D, Keycode.S, Keycode.D)}
EAGLE_CLUSTER_BOMB      = {'color':ORANGE, 'label':'Clust', 'keycode':(Keycode.W, Keycode.D, Keycode.S, Keycode.S, Keycode.D)}
EAGLE_NAPALM_STRIKE     = {'color':ORANGE, 'label':'Naplm', 'keycode':(Keycode.W, Keycode.D, Keycode.S, Keycode.W)}
EAGLE_SMOKE             = {'color':ORANGE, 'label':'Smoke', 'keycode':(Keycode.W, Keycode.D, Keycode.W, Keycode.S)}
EAGLE_110               = {'color':ORANGE, 'label':'110', 'keycode':(Keycode.W, Keycode.D, Keycode.W, Keycode.A)}
EAGLE_500KG             = {'color':ORANGE, 'label':'500KG', 'keycode':(Keycode.W, Keycode.D, Keycode.S, Keycode.S, Keycode.S)}
