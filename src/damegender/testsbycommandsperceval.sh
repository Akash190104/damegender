#!/bin/bash

# Copyright (C) 2019  David Arroyo Menéndez

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
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

rm -rf /tmp/clonedir

python3 git2gender.py https://github.com/davidam/orgguide-es.git --directory="/tmp/clonedir" > files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/git2gender1.txt files/tests/git2gender1-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "git2gender1 test is failing"
else
	echo "git2gender1 test is ok"
fi

rm -rf /tmp/clonedrupal

python3 git2gender.py  https://git.drupalcode.org/project/orgmode.git --directory="/tmp/clonedrupal" --language=us > files/tests/git2genderdrupal-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/git2genderdrupal.txt files/tests/git2genderdrupal-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "git2genderdrupal test is failing"
else
	echo "git2genderdrupal test is ok"
fi


cd files/mbox
wget -c http://mail-archives.apache.org/mod_mbox/httpd-announce/201706.mbox
cd ../..
python3 mail2gender.py http://mail-archives.apache.org/mod_mbox/httpd-announce/ > files/tests/mail2gender-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/mail2gender.txt files/tests/mail2gender-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
	echo "mail2gender test is failing"
else
	echo "mail2gender test is ok"
fi

rm -rf /tmp/clonedir
echo "cleaning temporary files"
rm files/tests/*$(date "+%Y")*.txt
