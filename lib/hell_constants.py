# List of helldivers 2 strats. 
from lib.adafruit_hid.keycode import Keycode

# BACKPACKS
JUMP_PACK = (Keycode.S, Keycode.W, Keycode.W, Keycode.S, Keycode.W)
SUPPLY_PACK = (Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.W, Keycode.S)
BALLISTIC_SHIELD = (Keycode.S, Keycode.A, Keycode.S, Keycode.S, Keycode.W, Keycode.A)
SHIELD_GENERATOR = (Keycode.S, Keycode.W , Keycode.A, Keycode.D, Keycode.A, Keycode.D)
AR23_GUARD_DOG = (Keycode.S, Keycode.W , Keycode.A, Keycode.W, Keycode.D, Keycode.S)
LAS_5_GUARD_DOG = (Keycode.S, Keycode.W, Keycode.A, Keycode.W, Keycode.D, Keycode.D)
GAS_GUARD_DOG = (Keycode.S, Keycode.W, Keycode.A, Keycode.W, Keycode.D, Keycode.W)

# SKeycode.WPORT WEAPONS
MACHINE_GUN = (Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.D)
ANTI_MATERIAL = (Keycode.S, Keycode.A, Keycode.D, Keycode.W, Keycode.S)
STALWART = (Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.W, Keycode.A)
EXPENDABLE_ANTI_TANK = (Keycode.S, Keycode.S, Keycode.A, Keycode.W, Keycode.D)
COMMANDO = (Keycode.S, Keycode.A, Keycode.W, Keycode.S, Keycode.D)
RECOILLESS = (Keycode.S, Keycode.A, Keycode.D, Keycode.D, Keycode.A)
FLAMETHROWER = (Keycode.S, Keycode.A, Keycode.W, Keycode.S, Keycode.W)
AUTOCANNON = (Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.W, Keycode.D)
HEAVY_MACHINE_GUN = (Keycode.S, Keycode.A, Keycode.W, Keycode.S, Keycode.S)
RAILGUN = (Keycode.S, Keycode.D, Keycode.S, Keycode.W, Keycode.A, Keycode.D)
SPEAR = (Keycode.S, Keycode.S, Keycode.W, Keycode.S, Keycode.S)
GRENADE_LAUNCHER = (Keycode.S, Keycode.A, Keycode.W, Keycode.A, Keycode.S)
LASER_CANNON = (Keycode.S, Keycode.A, Keycode.S, Keycode.W, Keycode.A)
ARC_THROWER = (Keycode.S, Keycode.D, Keycode.S, Keycode.W, Keycode.A, Keycode.A)
QUASAR_CANNON = (Keycode.S, Keycode.S, Keycode.W, Keycode.A, Keycode.D)
AIRBURST_ROCKET = (Keycode.S, Keycode.W, Keycode.W, Keycode.A, Keycode.D)

# SKeycode.WPORT MECH
EX045_PATRIOT = (Keycode.A, Keycode.S, Keycode.D, Keycode.W, Keycode.A, Keycode.S, Keycode.S)
EXO49_EMANCIPATOR = (Keycode.A, Keycode.S, Keycode.D, Keycode.W, Keycode.A, Keycode.S, Keycode.W)

# MISSION STRATAGEMS
REINFORCE = (Keycode.W, Keycode.S, Keycode.D, Keycode.A, Keycode.W)
#REINFORCE = (Keycode.W, Keycode.S, Keycode.D, Keycode.A, Keycode.W)
SOS = (Keycode.W, Keycode.S, Keycode.D, Keycode.W)
RESUPPLY = (Keycode.S, Keycode.S, Keycode.W, Keycode.D)
HELLBOMB = (Keycode.S, Keycode.W, Keycode.A, Keycode.S, Keycode.W, Keycode.D, Keycode.S, Keycode.W)
SSSD = (Keycode.S, Keycode.S, Keycode.S, Keycode.W, Keycode.W)
SIESMIC_PROBE = (Keycode.W, Keycode.W, Keycode.A, Keycode.D, Keycode.S, Keycode.S)
UPLOAD_DATA = (Keycode.A, Keycode.D, Keycode.W, Keycode.W, Keycode.W)
EAGLE_REARM = (Keycode.W, Keycode.W, Keycode.A, Keycode.W, Keycode.D)
SEAF = (Keycode.D, Keycode.W, Keycode.W, Keycode.S)
FLAG = (Keycode.S, Keycode.W, Keycode.S, Keycode.W)

# DEFENSIVE
MG_101_EMPLACEMENT = (Keycode.S, Keycode.W, Keycode.A, Keycode.D, Keycode.D, Keycode.A)
MACHINE_GUN_SENTRY = (Keycode.S, Keycode.W, Keycode.D, Keycode.D, Keycode.W)
GATLING_SENTRY = (Keycode.S, Keycode.W, Keycode.D, Keycode.A)
MORTAR_SENTRY = (Keycode.S, Keycode.W, Keycode.D, Keycode.D, Keycode.S)
AUTOCANNON_SENTRY = (Keycode.S, Keycode.W, Keycode.D, Keycode.W, Keycode.A, Keycode.W)
ROCKET_SENTRY = (Keycode.S, Keycode.W, Keycode.D, Keycode.D, Keycode.A)
EMS_MORTAR_SENTRY = (Keycode.S, Keycode.W, Keycode.D, Keycode.S, Keycode.D)
ANTI_PERSONNEL_MINE = (Keycode.S, Keycode.A, Keycode.W, Keycode.D)
INCENDIARY_MINE = (Keycode.S, Keycode.A, Keycode.A, Keycode.S)
ANTI_TANK_MINE = (Keycode.S, Keycode.A, Keycode.W, Keycode.W)
TESLA_TOWER = (Keycode.S, Keycode.W, Keycode.D, Keycode.W, Keycode.A, Keycode.D)
SHIELD_GENERATOR_RELAY = (Keycode.S, Keycode.S, Keycode.A, Keycode.D, Keycode.A, Keycode.D)

# OFFENSIVE ORBITAL
ORBITAL_GATLING_BARRAGE = (Keycode.D, Keycode.S, Keycode.A, Keycode.W, Keycode.W)
ORBITAL_AIRBURST_STRIKE = (Keycode.D, Keycode.D, Keycode.D)
ORBITAL_HE120_BARRAGE = (Keycode.D, Keycode.D, Keycode.S, Keycode.A, Keycode.D, Keycode.S)
ORBITAL_HE380_BARRAGE = (Keycode.D, Keycode.S, Keycode.W, Keycode.W, Keycode.A, Keycode.S, Keycode.S)
ORBITAL_WALKING = (Keycode.D, Keycode.S, Keycode.D, Keycode.S, Keycode.D, Keycode.S)
ORBITAL_LASER = (Keycode.D, Keycode.S, Keycode.W, Keycode.D, Keycode.S)
ORBITAL_RAILCANNON_STRIKE = (Keycode.D, Keycode.W, Keycode.S, Keycode.S, Keycode.D)
ORBITAL_PRECISION_STRIKE = (Keycode.D, Keycode.D, Keycode.W)
ORBITAL_GAS_STRIKE = (Keycode.D, Keycode.D, Keycode.S, Keycode.D)
ORBITAL_EMS_STRIKE = (Keycode.D, Keycode.D, Keycode.A, Keycode.S)
ORBITAL_SMOKE_STRIKE = (Keycode.D, Keycode.D, Keycode.S, Keycode.W)
ORBITAL_NAPALM_BARRAGE = (Keycode.D, Keycode.D, Keycode.S, Keycode.A, Keycode.D, Keycode.W)

# OFFENSIVE EAGLE
EAGLE_STRAFING_RUN = (Keycode.W, Keycode.D, Keycode.D)
EAGLE_AIRSTRIKE = (Keycode.W, Keycode.D, Keycode.S, Keycode.D)
EAGLE_CLUSTER_BOMB = (Keycode.W, Keycode.D, Keycode.S, Keycode.S, Keycode.D)
EAGLE_NAPALM_STRIKE = (Keycode.W, Keycode.D, Keycode.S, Keycode.W)
EAGLE_SMOKE = (Keycode.W, Keycode.D, Keycode.W, Keycode.S)
EAGLE_110 = (Keycode.W, Keycode.D, Keycode.W, Keycode.A)
EAGLE_500KG = (Keycode.W, Keycode.D, Keycode.S, Keycode.S, Keycode.S)

# COLORS
YELLOW = 0x302000
GREEN = 0x002000 
RED = 0x200000
BLUE = 0x000020
ORANGE = 0xFF9714
