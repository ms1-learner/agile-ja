def test_power_dict():
    import power_dict

    expected_outputs = {
        1: 1,
        2: 4,
        3: 9,
        4: 16,
        5: 25,
        6: 36,
        7: 49,
        8: 64,
        9: 81,
        10: 100,
    }

    assert power_dict.result == expected_outputs
