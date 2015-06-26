# Plotting the weather forecast in Illinois

## Background

Imagine we have a collaborator who has a script for plotting the temperature forecast for weather stations in Illinois.
Unfortunately, she has been manually downloading and formatting the National Weather Service data herself, which is very tedious and time-consuming.
She needs help writing some programs that will automatically download information about all of the weather stations in Illinois, download the latest forecast for those weather stations, and feed this data into her plotting program in a particular format, as described below.

```
K1H2	-88.53	+39.07	+72
KAAA	-89.33	+40.16	+75
KALN	-90.05	+38.88	+74
```

The script reads from standard input (stdin), and requires four tab-separated values for each weather station.

* The 4-letter label of the station.
* The longitude of the station (Illinois is west of the prime meridian, so this coordinate should be negative).
* The latitude of the station (Illinois is north of the equator, so this coordinate should be positive).
* The temperature, in Fahrenheit, of the next available forecast.

## Objective

For this exercise, we will split up into two groups.
Group 1 will write a program called `grab-stations.py` that will download and print the 4-letter label for each Illinois weather station and the corresponding coordinates.
Group 2 will write a program called `grab-forecast.py` that will download a national weather forecast, and then use the output from `grab-stations.py` to extract and print the temperature of the latest forecast for each station.

The objectives of this exercise are as follows.

* Learn how to write software using the Unix philosophy: i.e., how to pass data between programs with piping/stdin/stdout.
* Use test-driven development to write a computer program for a well-defined task.

## Goals

The page http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml has information about all of the National Weather Service weather stations in the US: a 4-letter label, a name, a 2-letter state abbreviation, and the latitude/longitude coordinates for that station.
The page http://www.nws.noaa.gov/mdl/gfslamp/lavlamp.shtml has an hourly forecast for each weather station for the next 24 hours.
We will then work together to write unit tests, defining what the behavior of our two programs should.
This will ensure they communicate properly with each other and the collaborator's plotting script.

## Stretch goals

Given time and interest, we may try to go further and reach one or more of the following "stretch goals".

* Randomly pair each participant from group 1 with a participant from group 2, and verify that their programs work together properly.
* Discuss the Git Flow model for collaborative development: have participants submit pull requests, and merge them back to the original repository.
* Make the scripts more user-friendly by adding a command-line interface with `argparse`.
