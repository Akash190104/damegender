#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
#  This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

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

# DESCRIPTION: This script allows to measure accuracies from a json
# file downloaded from an api system with downloadjson.py

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_namsor import DameNamsor
from app.dame_genderize import DameGenderize
from app.dame_genderguesser import DameGenderGuesser
from app.dame_genderapi import DameGenderApi
from app.dame_nameapi import DameNameapi
from app.dame_utils import DameUtils

import argparse
import os
parser = argparse.ArgumentParser()
# dataset_guess is a dataset such as files/names/names_de/defemales.csv
# or files/names/min.csv.json
parser.add_argument('--dataset_guess', type=str, required=True,
                    default="files/names/min.csv",
                    help='csv guess file with names, surnames and gender')
parser.add_argument('--dataset_guess_row_name', type=int,
                    required=False, default=0)
parser.add_argument('--dataset_guess_row_surname', type=int,
                    required=False, default=1)
parser.add_argument('--dataset_guess_row_gender', type=int,
                    required=False, default=2)
parser.add_argument('--dataset_guess_delimiter', type=str,
                    required=False, default=",")
# dataset_test is a dataset such as files/names/names_tests/fifa.csv
# or files/names/allnoundefined.csv.mlp.json
parser.add_argument('--dataset_test', required=True,
                    help='generated by downloadjson.py or damegender2json.py')
parser.add_argument('--dataset_test_row_name', type=int,
                    required=False, default=0)
parser.add_argument('--dataset_test_row_surname', type=int,
                    required=False, default=1)
parser.add_argument('--dataset_test_row_gender', type=int,
                    required=False, default=2)
parser.add_argument('--dataset_test_row_gender_chars', type=str,
                    required=False, default="f,m")
parser.add_argument('--dataset_test_delimiter', type=str,
                    required=False, default=",")
parser.add_argument('--measure', default="accuracy",
                    choices=['accuracy', 'precision', 'recall', 'f1score'])
parser.add_argument('--api', required=True,
                    choices=['namsor', 'genderize',
                             'genderguesser', 'damegender',
                             'genderapi', 'nameapi', 'all'])

args = parser.parse_args()
du = DameUtils()

# set gender_values array
gender_values = args.dataset_test_row_gender_chars.split(",")
fem = gender_values[0]
mal = gender_values[1]


if (args.api == "all"):

    if (dg.config['DEFAULT']['namsor'] == 'yes'):
        dn = DameNamsor()
        dn.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                          measure=args.measure, api='Namsor',
                          gender_f_chars=fem, gender_m_chars=mal)

    if (dg.config['DEFAULT']['genderize'] == 'yes'):
        dg = DameGenderize()
        dg.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                          measure=args.measure, api='Genderize',
                          gender_f_chars=fem, gender_m_chars=mal)

    dgg = DameGenderGuesser()
    dgg.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                       measure=args.measure, api='Genderguesser',
                       gender_f_chars=fem, gender_m_chars=mal)

    ds = DameSexmachine()
    ds.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                      measure=args.measure, api='Damegender',
                      gender_f_chars=fem, gender_m_chars=mal)

    if (dg.config['DEFAULT']['genderapi'] == 'yes'):
        dga = DameGenderApi()
        dga.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                           measure=args.measure, api='Genderapi',
                           gender_f_chars=fem, gender_m_chars=mal)

    if (dg.config['DEFAULT']['nameapi'] == 'yes'):
        dna = DameNameapi()
        dna.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                           measure=args.measure, api='Nameapi',
                           gender_f_chars=fem, gender_m_chars=mal)

elif (args.api == "namsor"):
    dn = DameNamsor()
    dn.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                      measure=args.measure, api='Namsor',
                      gender_f_chars=fem, gender_m_chars=mal)

elif (args.api == "genderize"):
    dg = DameGenderize()
    dg.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                      measure=args.measure, api='Genderize',
                      gender_f_chars=fem, gender_m_chars=mal)

elif (args.api == "genderguesser"):
    dgg = DameGenderGuesser()
    dgg.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                       measure=args.measure, api='Genderguesser',
                       gender_f_chars=fem, gender_m_chars=mal)

elif (args.api == "damegender"):
    ds = DameSexmachine()
    ds.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                      measure=args.measure, api='Damegender',
                      gender_csv_row=args.dataset_test_row_gender,
                      delimiter_guessf=args.dataset_guess_delimiter,
                      delimiter_testf=args.dataset_test_delimiter,
                      gender_f_chars=fem, gender_m_chars=mal)

elif (args.api == "genderapi"):
    dga = DameGenderApi()
    dga.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                       measure=args.measure, api='Genderapi',
                       gender_f_chars=fem, gender_m_chars=mal)

elif (args.api == "nameapi"):
    dna = DameNameapi()
    dna.pretty_gg_list(guessf=args.dataset_guess, testf=args.dataset_test,
                       measure=args.measure, api='Nameapi',
                       gender_f_chars=fem, gender_m_chars=mal)
