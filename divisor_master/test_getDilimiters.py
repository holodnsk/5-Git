from divisor_master import getDilimiters


def test_getDilimiters():
    assert getDilimiters(12) == [1,2,3,4,6,12]