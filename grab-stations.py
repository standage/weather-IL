import requests

def test_filter_stations():
    assert filter_stations(' 8   K1H2 EFFINGHAM CNTY MEM   IL   39.07N    88.53W') == ('K1H2', 39.07, -88.53)
    assert filter_stations(' 8   KFOA FLORA MUNI AIRPORT   IL   38.66N    88.45W') == ('KFOA', 38.66, -88.45)
    assert filter_stations(' 8   KETB WEST BEND            WI   43.42N    88.13W') == ('KETB', 43.42, -88.13)

def filter_stations(line):
    label = line[5:9]
    lat = float(line[36:41])
    if line[41] == "S":
        lat = -1*lat
    long = float(line[46:51])
    if line[51] == "W":
        long = -1*long
    return (label, lat, long)
    
def main():
    data = requests.get('http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml')
    for line in data.text.splitlines():
        if ' IL ' in line:
	    label, lat, long = filter_stations(line)
	    print "%s\t%.2f\t%.2f" % (label, lat, long)
        
if __name__ == '__main__':
    main()
