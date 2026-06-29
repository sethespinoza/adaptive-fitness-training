from app.domain.strength import estimate_1rm, working_weight

def test_estimate_1rm_epley():
    assert round(estimate_1rm(200, 5), 1) == 233.3

def test_1rm_of_a_true_max_is_itself():
    assert estimate_1rm(300, 1) == 300

def test_working_weight_round_trips():
    one_rm = estimate_1rm(200, 5)
    assert round(working_weight(one_rm, 5), 1) == 200.0

def test_brzycki_rejects_high_reps():
    import pytest
    with pytest.raises(ValueError):
        estimate_1rm(100, 40, formula="brzycki")
