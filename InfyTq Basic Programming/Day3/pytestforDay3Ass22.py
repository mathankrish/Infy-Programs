

from Day3Ass22.py import find_leap_years

def test_find_leap_years_1():
    result=find_leap_years(2002)
    assert result == [2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]