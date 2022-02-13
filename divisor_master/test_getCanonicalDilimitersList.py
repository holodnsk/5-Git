from divisor_master import getCanonicalDilimitersList


def test_getCanonicalDilimitersList():
    assert getCanonicalDilimitersList(78) == [2, 3, 13]