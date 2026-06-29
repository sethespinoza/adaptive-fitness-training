import math
from dataclasses import dataclass

MILE_IN_METERS = 1609.34

TRAINING_ZONES = {
    "easy": (0.59, 0.74),
    "marathon": (0.75, 0.84),
    "threshold": (0.83, 0.88),
    "interval": (0.95, 1.00),
    "repetition": (1.00, 1.06)
}

def vo2_from_velocity(v: float) -> float:
    return -4.60 + 0.182258 * v + 0.000104 * v ** 2

def percent_max_from_time(t: float) -> float:
    return 0.8 + 0.1894393 * math.exp(-0.012778 * t) + 0.2989558 * math.exp(-0.1932605 * t)

def vdot_from_race(distance_m: float, time_min: float) -> float:
    velocity = distance_m / time_min
    return vo2_from_velocity(velocity) / percent_max_from_time(time_min)

def velocity_for_target_vo2(target_vo2: float) -> float:
    """Invert VO2(v) quadratic to get velocity from a given target VO2."""
    a, b, c = 0.000104, 0.182258, -(4.60 + target_vo2)
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

def pace_per_mile(v: float) -> str:
    total_seconds = round(MILE_IN_METERS / v * 60)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"

@dataclass
class PaceZones:
    vdot: float
    zones: dict

def pace_zones_from_vdot(vdot: float) -> PaceZones:
    zones = {}
    for name, (low, high) in TRAINING_ZONES.items():
        fast = velocity_for_target_vo2(vdot * high)
        slow = velocity_for_target_vo2(vdot * low)
        zones[name] = (pace_per_mile(fast), pace_per_mile(slow))
    return PaceZones(vdot=vdot, zones=zones)



