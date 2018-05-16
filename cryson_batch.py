#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Process a batch of pdb files through the CRYSON program to calculate
small-angle neutron scattering (SANS) curves.

Example here uses the 2KKJ.pdb file split into its 10 conformers.
Original pdb available from: https://www.rcsb.org/structure/2kkj

Requires CRYSON program within ATSAS tools (free, registration required).
Available from: https://www.embl-hamburg.de/biosaxs/cryson.html
'''

import os
import time

# Go to directory where pdb files are located
os.chdir('pdbs')

# Check that the CRYSON program exists
if os.path.isfile('cryson') is True:
    pass
else:
    print('Missing the CRYSON program. \n'
          + 'Ensure this program is in the "pdbs" directory or download from: \n'
          + 'https://www.embl-hamburg.de/biosaxs/cryson.html \n')
    raise SystemExit

n = 0

# Loop through all pdb files
while n < 10:
    name = '2kkj_' + str(n) + '.pdb'

    # Make the text file for inputs into crysol
    text = ('0 \n'
            + name + '\n'
            + '15 \n'
            + '17 \n'
            + '0.5 \n'
            + '100 \n'
            + '0.0 \n'
            + '1.0 \n'
            + 'N \n'
            + '0.1 \n'
            + '\n'
            + 'N \n'
            + '\n'
            + '\n'
            + '\n'
            )

    f = open('cryson_input.txt', 'w')
    f.write(text)
    f.close()

    # Run cryson for mac
    os.system('./cryson < cryson_input.txt')

    # Sleep 2 sec to allow cryson to finish
    time.sleep(2)

    n = n + 1

# Clean up unneeded files
os.system('rm *.alm')
os.system('rm *.flm')
os.system('rm *.sav')

# Move cryson calculations to cryson folder
os.system('mv *.log ../cryson')
os.system('mv *.int ../cryson')
