# :noTabs=true:
# (c) Copyright Rosetta Commons Member Institutions.
# (c) This file is part of the Rosetta software suite and is made available under license.
# (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
# (c) For more information, see http://www.rosettacommons.org. Questions about this can be
# (c) addressed to University of Washington UW TechTransfer, email: license@u.washington.edu.

## @author Sergey Lyskov

from rosetta import *
rosetta.init()



print 'testing ligand modeling'
params_list = Vector1(['test/data/ligand.params'])
res_set = generate_nonstandard_residue_set(params_list)
ligand_p = pose_from_pdb(res_set, "test/data/ligand_test.pdb")

scorefxn = create_score_function("ligand")
scorefxn(ligand_p)

print 'testing DNA modeling'
dna_p = Pose()
pose_from_pdb(dna_p, "test/data/dna_test.pdb")

scorefxn = create_score_function("dna")
scorefxn(dna_p)

