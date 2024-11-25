def test_remaining_weeks():
    age = 48
    death_age = 90
    total_weeks = int(death_age * 52)
    age_weeks = int(age * 52)
    remaining_weeks = int(total_weeks - age_weeks)
    assert remaining_weeks == 1872

test_remaining_weeks()