#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# DESCRIPTION: This script allows to detect ethnicity from a surname


from app.dame_gender import Gender
from app.dame_ethnicity import DameEthnicity
import sys
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("surname", help="display the gender")
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()

results = []

de = DameEthnicity()
surname = args.surname.upper()
dicc = de.surname2ethnicity(surname)

if (dicc):
    print("USA's percentages about the race of %s: " % surname.capitalize())
    print("White: %s" % dicc['white'])
    print("Black: %s" % dicc['black'])
    print("Hispanic: %s" % dicc['hispanic'])
    print("Asian Pacific Indian American: %s" % dicc['api'])
    print("American Indian and Alaska Native: %s" % dicc['aian'])
    print("Various races: %s" % dicc['doublerace'])
else:
    print("This string %s is not a surname in USA" % surname.capitalize())
