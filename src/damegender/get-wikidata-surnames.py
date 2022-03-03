#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2022  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import requests
from SPARQLWrapper import SPARQLWrapper, JSON
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("name", help="display the gender")
parser.add_argument('total', default="es",
                    choices=['at', 'au', 'be', 'ca', 'ch',
                             'cn', 'de', 'dk', 'es', 'fi',
                             'fr', 'gb', 'ie', 'is', 'no', 'nz',
                             'mx', 'pt', 'ru', 'se', 'si',
                             'uy', 'us'])
# More about iso codes on https://www.iso.org/obp/ui/
parser.add_argument('--version', action='version', version='0.4')
# parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()


if (args.total == "at"):
    string = "Q40"
elif (args.total == "au"):
    string = "Q408"
elif (args.total == "be"):
    string = "Q31"
elif (args.total == "ca"):
    string = "Q16"
elif (args.total == "ch"):
    string = "Q39"
elif (args.total == "cn"):
    string = "Q148"
elif (args.total == "de"):
    string = "Q183"
elif (args.total == "dk"):
    string = "Q35"
elif (args.total == "es"):
    string = "Q29"
elif (args.total == "es"):
    string = "Q29"
elif (args.total == "fi"):
    string = "Q33"
elif (args.total == "fr"):
    string = "Q142"
elif (args.total == "gb"):
    string = "Q145"
elif (args.total == "ie"):
    string = "Q27"
elif (args.total == "is"):
    string = "Q189"
elif (args.total == "no"):
    string = "Q20"
elif (args.total == "nz"):
    string = "Q664"
elif (args.total == "pt"):
    string = "Q45"
elif (args.total == "ru"):
    string = "Q159"
elif (args.total == "se"):
    string = "Q34"
elif (args.total == "si"):
    string = "Q215"
elif (args.total == "uy"):
    string = "Q77"

url = 'https://query.wikidata.org/sparql'
query = """
SELECT ?name ?nameLabel ?count
WITH {
  SELECT ?name (count(?person) AS ?count) WHERE {
    ?person wdt:P734 ?name .
    ?person wdt:P27 wd:""" + string + """ .
  }
  GROUP BY ?name
  ORDER BY DESC(?count)
} AS %results
WHERE {
  INCLUDE %results
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?count)
"""

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

results = get_results(url, query)

print("Dumping results to surnames-country.csv")

fo = open("surnames-country.csv", "w")
for result in results["results"]["bindings"]:
    fo.write(result['nameLabel']['value'] + "," + result['count']['value'] +  "\n");

# Cerramos el archivo fichero.txt
fo.close()


# r = requests.get(url, params = {'format': 'json', 'query': query2})
# data = r.json()
# print(data)