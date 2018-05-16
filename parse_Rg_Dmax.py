#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Parse out Rg and Dmax values from CRYSON *.log files and write to file.

See cryson_batch.py

CRYSON program available from:
https://www.embl-hamburg.de/biosaxs/cryson.html
'''

import os

# Go to directory where pdb files are located
os.chdir('cryson')

# Start file with this header
Rg_Dmax_list = '''Rg = Rg from the slope of net intensity from CRYSON
Dmax = Envelope diameter from CRYSON

count Rg Dmax
'''

n = 0

# Loop through all CRYSON files
while n < 10:
    name = '2kkj_' + str(n) + '00.log'

    try:
        s = open(name, 'r')
        lines = s.readlines()
        s.close()

        rline = lines[-10:-9]
        dline = lines[-25:-24]

        #Grab Rg value
        Rg = ''.join(rline)
        Rg = Rg[-6:]

        #Grag Dmax value
        Dmax = ''.join(dline)
        Dmax = Dmax[-10:-5]

        Rg_Dmax_list += str(n) + ' ' + Rg.strip('\n') + ' ' + Dmax + '\n'
    except IOError:
        pass
        
    n = n + 1

# Go back up one level to write file
os.chdir('..')

f = open('Rg_Dmax_values.txt', 'w')
f.write(Rg_Dmax_list)
f.close()
