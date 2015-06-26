def test_parse_input():
    assert parse_input('KBMI\t40.48\t-88.93') == ('KBMI', 40.48, -88.93)
    assert parse_input('KDNV\t40.20\t-87.60') == ('KDNV', 40.20, -87.60)


def test_parse_temp():
    html = """ KDPA   WEST CHICAGO          GFS LAMP GUIDANCE   6/26/2015  1900 UTC            
 UTC  20 21 22 23 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 
 TMP  67 67 66 66 66 65 63 62 61 61 61 61 60 60 59 58 61 64 66 68 70 72 73 74 74 
 DPT  60 59 59 58 58 57 57 57 56 56 56 56 56 56 55 55 56 56 56 56 55 55 55 54 53 
 WDR  04 04 04 04 04 03 03 03 03 02 02 01 36 36 36 36 36 36 01 01 01 01 01 01 02 
 WSP  11 11 11 12 13 12 11 10 09 09 08 08 08 08 07 07 08 09 10 11 11 11 11 10 10 
 WGS  NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG 17 18 17 NG 
 PPO  17 46 46 45 42 38 33 18 17 15 17 15 13 11  6  4  1  0  0  0  0  0  0  0  0 
 PCO   N  Y  Y  Y  Y  Y  Y  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N 
 P06                                45                20                 1       
 LP2         9  8  6  4  6     2     1     0     1     0     0     0     0     0 
 LC2         N  N  N  N  N     N     N     N     N     N     N     N     N     N 
 CP2        26 23 24 19 15    10     7     6     5     0     0     0     0     0 
 CC2         M  L  L  L  L     N     N     N     N     N     N     N     N     N 
 CLD  OV OV OV OV OV OV OV OV OV OV OV OV OV OV OV OV OV OV BK BK SC SC SC FW FW 
 CIG   4  4  5  5  5  5  6  6  6  6  6  5  4  3  4  4  6  7  8  8  8  8  8  8  8 
 CCG   4  4  4  5  5  5  5  6  5  6  6  5  5  5  5  5  5  6  6  6  6  6  6  6  7 
 VIS   7  7  7  7  7  7  7  7  7  7  5  5  5  5  7  7  7  7  7  7  7  7  7  7  7 
 CVS   5  5  5  5  5  5  5  7  6  5  5  5  5  5  6  7  7  7  7  7  7  7  7  7  7 
 OBV   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N"""
    assert parse_temp(html) == 67

    html = """ KDSM   DES MOINES     ASOS   GFS LAMP GUIDANCE   6/26/2015  1900 UTC            
 UTC  20 21 22 23 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 
 TMP  75 74 74 73 72 72 71 70 68 67 66 65 64 63 63 62 63 65 68 71 73 75 76 77 78 
 DPT  63 63 63 63 63 63 62 62 61 61 60 60 59 59 59 58 58 59 59 60 60 59 59 59 59 
 WDR  05 05 05 05 04 04 05 04 03 02 01 36 36 36 36 36 36 36 36 36 36 35 35 35 35 
 WSP  10 10 09 09 09 08 06 06 05 05 05 05 05 06 05 05 04 05 05 06 07 07 07 07 08 
 WGS  NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG 
 PPO   5  4  5  4  2  1  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 
 PCO   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N 
 P06                                 2                 4                 3       
 LP2         3  1  0  0  0     0     0     0     0     0     0     0     0     0 
 LC2         N  N  N  N  N     N     N     N     N     N     N     N     N     N 
 CP2        12  5  4  0  0     0     0     1     1     1     1     0     0     0 
 CC2         L  N  N  N  N     N     N     N     N     N     N     N     N     N 
 CLD  OV OV OV OV OV BK SC FW FW SC BK BK BK BK SC SC FW FW FW SC SC SC SC SC SC 
 CIG   7  6  6  7  7  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  7  7 
 CCG   6  6  6  6  6  6  7  7  7  7  7  7  7  7  6  6  6  6  6  7  6  6  6  6  6 
 VIS   7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7 
 CVS   7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  6  6  5  7  7  7  7  7  7 
 OBV   N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N  N"""
    assert parse_temp(html) == 75


def main():
    pass


if __name__ == '__main__':
    main()
