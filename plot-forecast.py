import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

# Load station tags from stdin.
stns = []
locx = []
locy = []
temp = []
for line in sys.stdin:
    elems = line.split()
    stns.append(elems[0])  # station name
    locx.append(float(elems[1]))
    locy.append(float(elems[2]))
    temp.append(float(elems[3]))

mpl.rcParams['figure.figsize'] = [10, 10]

# Plot the stations, color-coded by temperature
plt.scatter(locx, locy, c=temp, marker='D')

# Print the name of each station
for i in range(len(stns)):
    plt.text(locx[i]+0.04, locy[i]+0.02, stns[i])

# The borders of IL in lat/lon coordinates are located in this file.
x, y = [], []
for line in open('illinois.txt', 'r'):
    fields = line.strip().split(' ')
    x.append(float(fields[0]))
    y.append(float(fields[1]))
plt.plot(x, y, 'k-')

plt.axis('equal')
plt.title('Weather Stations in Illinois')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
