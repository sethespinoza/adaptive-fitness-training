from app.domain.fitness import vdot_from_race, pace_zones_from_vdot

def test_vdot_24min_5k():
    vdot = vdot_from_race(distance_m=5000, time_min=24.0)
    assert 39.5 < vdot < 41.0

def test_faster_time_gives_higher_vdot():
    assert vdot_from_race(5000, 20.0) > vdot_from_race(5000, 24.0)

def test_zones_ordered_fastest_to_slowest():
    zones = pace_zones_from_vdot(40.2).zones

    def pace_to_seconds(pace: str) -> int:
        minutes, seconds = pace.split(":")
        return int(minutes) * 60 + int(seconds)
    
    assert pace_to_seconds(zones["repetition"][0]) < pace_to_seconds(zones["easy"][1])
    
