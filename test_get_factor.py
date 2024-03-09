from gibbs_sampling import get_factor

SAMPLE_1 = {"A": "a0", "B": "b1", "C": "c0", "D": "d0", "E": "e0", "F": "f0"}
SAMPLE_2 = {"A": "a1", "B": "b0", "C": "c1", "D": "d1", "E": "e1", "F": "f1"}

def test_sample1():
    variable = "A"
    result = get_factor(SAMPLE_1, variable)
    assert result == {"a0": 25, "a1": 1000}
    variable = "D"
    result = get_factor(SAMPLE_1, variable)
    assert result == {"d0": 1, "d1": 1250}
    variable = "E"
    result = get_factor(SAMPLE_1, variable)
    assert result == {"e0": 20, "e1": 50}
    variable = "F"
    result = get_factor(SAMPLE_1, variable)
    assert result == {"f0": 20, "f1": 100}

def test_sample2():
    variable = "A"
    result = get_factor(SAMPLE_2, variable)
    assert result == {"a0": 500, "a1": 250}
    variable = "D"
    result = get_factor(SAMPLE_2, variable)
    assert result == {"d0": 35, "d1": 50}
    variable = "E"
    result = get_factor(SAMPLE_2, variable)
    assert result == {"e0": 250, "e1": 2000}
    variable = "F"
    result = get_factor(SAMPLE_2, variable)
    assert result == {"f0": 5000, "f1": 200}
