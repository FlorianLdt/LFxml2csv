#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import argparse
import time

# Save command line arguments in an array (0: XML input file | 1: CSV output file)
parser = argparse.ArgumentParser()
parser.add_argument ("infile", metavar="file", nargs="+", type=str, help="data file") 
args = parser.parse_args()

argsArray = []
for filename in args.infile:
    argsArray.append(filename)


start_date = time.time()

print("===   Conversion in progress...   ===")

tree = ET.parse(argsArray[0])
pdv_liste = tree.getroot()

# Create an empty CSV file with name given in command line and write the header in that file
file = open(argsArray[1],"w") 
header = "id;id_pdv;nom_carburant;id_carburant;maj_carburant;prix_carburant\n"
file.write(header)

# Variable used for the first value of each line 'id' which must remains unique
auto_increm = 0

# Loop used to navigate into each node of the XML file
# Test if a value is empty and replace it by 'NIL'
for pdv in pdv_liste:
    id_pdv = pdv.get("id")
    if id_pdv is None or id_pdv == "":
        id_pdv = "NIL"
    for prix in pdv.iter('prix'):
    	nom = prix.get("nom")
        if nom is None or nom == "":
            nom = "NIL"
    	id_carburant = prix.get("id")
        if id_carburant is None or id_carburant == "":
    	   id_carburant = "NIL"
    	maj = prix.get("maj")
        if maj is None or maj == "":
    	   maj = "NIL"
    	valeur = prix.get("valeur")
        if valeur is None or valeur == "":
    	   valeur = "NIL"

        # Create the CSV line with each element and write it in the CSV file
    	line = (str(auto_increm) + ";" + id_pdv + ";" + nom.upper() + ";" + id_carburant + ";" + maj + ";" + valeur+"\n")
    	file.write(line)

	auto_increm += 1

end_time = time.time()
delta_time = end_time - start_date
print("===   Converted in %s seconds  ===" % (round(delta_time,3)))
    
