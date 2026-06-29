def estimate_1rm(weight: float, reps: int, formula: str = "epley") -> float:
    if reps <= 0:
        raise ValueError("reps must be positive")
    if reps == 1:
        return weight
    if formula == "epley":
        return weight * (1 + reps / 30)
    if formula == "brzycki":
        if reps >= 37:
            raise ValueError("Brzycki breaks down at reps >= 37")
        return weight * 36 / (37 - reps)
    raise ValueError(f"unknown formula: {formula}")

def pct_1rm_for_reps(reps: int) -> float:
    """ Inverse Epley: what %1RM produces failure at this rep count."""
    return 1 / (1 + reps / 30)

def working_weight(one_rm: float, target_reps: int) -> float:
    return one_rm * pct_1rm_for_reps(target_reps)
