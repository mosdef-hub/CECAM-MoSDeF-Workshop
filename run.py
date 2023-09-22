# Import Libraries
import mbuild as mb
import gmso
import hoomd
from pBuilder import Arginine, Glycine, Glutamine, Leucine, Alanine # R, G, Q, L, A
from pBuilder.polypeptide import Protein

from gmso.parameterization import apply

import warnings 
warnings.filterwarnings("ignore")

n_repeats = 2
chain = Protein()
nonrepeat = 'GGQGGAGQGGYGGLGSQGAGRGGLGGQ'
repeat = 'GAGAAAAAAGGAGQGGTGGLGSQGAGRGGL'
chain.name="Protein"
chain.build(nonrepeat + 2*repeat)
chain.translate(-chain.center) #translate_to, rotate, spin, rotate_dihedral

rotable_bond = list(chain.bonds())[301]
chain.rotate_dihedral(bond=rotable_bond, phi=3.14) 

water = mb.load("O", smiles=True)
water.name="H2O"
water_box = mb.fill_box(water, box=[5,5,5], n_compounds=100)

packed_box = mb.fill_box([chain, water], n_compounds=[1,1000], box=[10,10,10])

packed_box.save("solvated_protein.pdb", overwrite=True)
reloaded_pdb = mb.load("solvated_protein.pdb") 

packed_box.energy_minimize()

gaff_forcefield = gmso.ForceField("./forcefields/gaff_edits.xml")

tip3p_forcefield = gmso.ForceField("./forcefields/spce.xml")
tip3p_forcefield.combining_rule = "geometric"


# gmso_top = reloaded_pdb.to_gmso()
forcefield_matchingDict = {"Protein":gaff_forcefield, "H2O":tip3p_forcefield}

gmso_top = packed_box.to_gmso()
# try:


parameterized_top = apply(
    gmso_top, forcefield_matchingDict, identify_connections=True, 
) #Angles, dihedrals missing
# print(dir(gmso_top))
# print(gmso_top._impropers)
gmso_top._impropers = []
# except:
#     gmso_top = reloaded_pdb.to_gmso()
#     parameterized_top = apply(
#         gmso_top, forcefield_matchingDict, identify_connections=True, 
#         assert_angle_params=False, assert_dihedral_params=False
#     )
#     missing_angles = set()
#     for angle in gmso_top.angles:
#         if angle.angle_type is None:
#             missing_angles.add(angle.connection_members)
#             for i in range(3):
#                 site = angle.connection_members[i]
#                 print(site.atom_type.name, site.atom_type.description, site.residue)
#             print("###\n")


import unyt as u

from gmso.external import to_hoomd_forcefield, to_hoomd_snapshot

base_units = {
    "mass": u.g / u.mol,
    "length": u.nm,
    "energy": u.kJ / u.mol,
}

gmso_snapshot, snapshot_base_units = to_hoomd_snapshot(
    parameterized_top, base_units=base_units
)
gmso_forces, forces_base_units = to_hoomd_forcefield( #can't handle dimensionless parameters currently, PR incoming
    parameterized_top,
    r_cut=1.4,
    base_units=base_units,
    pppm_kwargs={"resolution": (64, 64, 64), "order": 7},
)


import hoomd
temp = 300 * u.K
kT = temp.to_equivalent("kJ/mol", "thermal").value

cpu = hoomd.device.CPU()
sim = hoomd.Simulation(device=cpu, seed=1)
# sim.create_state_from_gsd("top.gsd") # does not work
sim.create_state_from_snapshot(gmso_snapshot)
sim.operations.integrator = hoomd.md.Integrator(dt=0.001)
sim.operations.integrator.forces.extend(
    list(set().union(*gmso_forces.values()))[:-1]
)
bussi = hoomd.md.methods.thermostats.Bussi(kT=kT)
nvt = hoomd.md.methods.ConstantVolume(
    filter=hoomd.filter.All(), 
    thermostat=bussi
)
sim.operations.integrator.methods.append(nvt)

sim.state.thermalize_particle_momenta(filter=hoomd.filter.All(), kT=kT)
thermodynamic_properties = hoomd.md.compute.ThermodynamicQuantities(
    filter=hoomd.filter.All()
)

sim.operations.computes.append(thermodynamic_properties)
logger = hoomd.logging.Logger()
logger.add(thermodynamic_properties)

import os
if os.path.exists('trajectory.gsd'):
    os.remove("trajectory.gsd")
gsd_writer = hoomd.write.GSD(
    filename='trajectory.gsd',
    trigger=hoomd.trigger.Periodic(1000),
     mode='xb',
     filter=hoomd.filter.All(),
     logger=logger
)
sim.operations.writers.append(gsd_writer)
outlogger = hoomd.logging.Logger(categories=['scalar', 'string'])
outlogger.add(sim, quantities=['timestep', 'tps'])
outlogger.add(thermodynamic_properties, ['kinetic_temperature'])
table = hoomd.write.Table(
    trigger=hoomd.trigger.Periodic(period=100),
    logger=outlogger
)
sim.operations.writers.append(table)
sim.run(100000)