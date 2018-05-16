## cryson-batch

#### Description: Two scripts to process pdb files through CRYSON and obtain a list of *R<sub>g</sub>* and *D<sub>max</sub>* values.


The example here uses the 2KKJ.pdb file split into its 10 conformers.  
Original pdb available from: https://www.rcsb.org/structure/2kkj


Requires CRYSON program within ATSAS tools (free, registration required).  
Available from: https://www.embl-hamburg.de/biosaxs/cryson.html


1. cryson_batch.py  
   Process a batch of pdb files through the CRYSON program to calculate small-angle neutron scattering (SANS) curves.


2. parse_Rg_Dmax.py  
   Parse out *R<sub>g</sub>* and *D<sub>max</sub>* values from CRYSON *.log files and write to file.
