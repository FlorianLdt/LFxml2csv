# LFxml2csv

A little example for how to convert an XML to CSV with Python.

I hope it can help some people facing some problems with XML parsing.

Have a nice day.

Florian

## Input file

This script has been used on the following XML file : https://donnees.roulez-eco.fr/opendata/annee/2016

## Output file

The result of the conversion is the following :

`id;id_pdv;nom_carburant;id_carburant;maj_carburant;prix_carburant`

`0;1000001;GAZOLE;1;2016-01-02T09:01:58;1026`

`1;1000001;GAZOLE;1;2016-01-04T10:01:35;1026`

`2;1000001;GAZOLE;1;2016-01-04T12:01:15;1026`

`3;1000001;GAZOLE;1;2016-01-05T09:01:12;1026`

`4;1000001;GAZOLE;1;2016-01-07T08:01:13;1026`

`5;1000001;GAZOLE;1;2016-01-07T09:01:12;1029`

`6;1000001;GAZOLE;1;2016-01-08T09:01:09;1029`

`...`

The input file contains mnore than 4 million lines (274.6 MB) and the conversion was made in 69 seconds.

## How to use it 

In the command line: `python2.7 LFxml2csv.py inputfile.xml outputfile.csv`.

Of course yopu can replace `inputfile` and `outputfile` by the names you want.

/ ! \ Make sure to specify the right path for the input and output files.
