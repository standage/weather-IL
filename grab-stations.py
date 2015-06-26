def test_filter_stations():
    assert filter_stations(' 8   K1H2 EFFINGHAM CNTY MEM   IL   39.07N    88.53W') == ('K1H2', 39.07, -88.53)
    assert filter_stations(' 8   KFOA FLORA MUNI AIRPORT   IL   38.66N    88.45W') == ('KFOA', 38.66, -88.45)
    assert filter_stations(' 8   KETB WEST BEND            WI   43.42N    88.13W') == ('KETB', 43.42, -88.13)


def main():
    pass


if __name__ == '__main__':
    main()
