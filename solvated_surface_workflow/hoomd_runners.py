"""Run HOOMD simulations for solvated surfaces."""
# Import Libraries
import os

import signac
import hoomd
import gsd
import unyt as u
import numpy as np

def example_run(job, parameterized_top, snapshot, forces, dt=0.00005):
    """Short 100 step run."""
    filter_ = hoomd.filter.Tags(list(np.arange(1900, parameterized_top.n_sites+1))) 
    cpu = hoomd.device.CPU()
    sim = hoomd.Simulation(device=cpu, seed=int(job.sp.seed/1000))
    sim.create_state_from_snapshot(snapshot)
    temp = 30 * u.K # start at low temp
    kT = temp.to_equivalent("kJ/mol", "thermal").value
    sim.state.thermalize_particle_momenta(filter=filter_, kT=kT)
    integrator = hoomd.md.Integrator(
        dt=dt,
        forces=list(set().union(*forces.values())),
    )                      
    langevin = hoomd.md.methods.Langevin(
        filter=filter_,
        kT=kT,
        default_gamma=100                     
    ) 
    integrator.methods.append(langevin)
    sim.operations.integrator = integrator
    outlogger = hoomd.logging.Logger(categories=['scalar', 'string'])
    outlogger.add(sim, quantities=['timestep', 'tps'])
    thermodynamic_properties = hoomd.md.compute.ThermodynamicQuantities(
        filter=filter_
    )
    sim.operations.computes.append(thermodynamic_properties)
    outlogger.add(thermodynamic_properties, ['kinetic_temperature', "potential_energy"]) 
    table = hoomd.write.Table(
        trigger=hoomd.trigger.Periodic(period=10), 
        logger=outlogger
    )                           
    sim.operations.writers.append(table) 

    sim.run(100)
    hoomd.write.GSD.write(state=sim.state,
      mode='xb',
      filename=job.fn('100steps-out.gsd')
    ) 
    print("Finished 100 Steps of HOOMD-blue run")
    return sim

def nvt_run(job, parameterized_top, snapshot, forces):
    """Full NVT Simulation."""
    filter_ = hoomd.filter.Tags(list(np.arange(1900, parameterized_top.n_sites+1))) 
    cpu = hoomd.device.CPU()
    sim = hoomd.Simulation(device=cpu, seed=job.sp.seed)
    sim.create_state_from_snapshot(snapshot)
    temp = 30 * u.K # start at low temp
    kT = temp.to_equivalent("kJ/mol", "thermal").value
    sim.state.thermalize_particle_momenta(filter=filter_, kT=kT)
    integrator = hoomd.md.Integrator(
        dt=0.00005,
        forces=list(set().union(*forces.values())),
    )                      
    langevin = hoomd.md.methods.Langevin(
        filter=filter_,
        kT=kT,
        default_gamma=100                     
    )
    integrator.methods.append(langevin)
    sim.operations.integrator = integrator
    outlogger = hoomd.logging.Logger(categories=['scalar', 'string'])
    outlogger.add(sim, quantities=['timestep', 'tps'])
    thermodynamic_properties = hoomd.md.compute.ThermodynamicQuantities(
        filter=filter_
    )
    sim.operations.computes.append(thermodynamic_properties)
    outlogger.add(thermodynamic_properties, ['kinetic_temperature', "potential_energy"]) 
    table = hoomd.write.Table(
        trigger=hoomd.trigger.Periodic(period=1000), 
        logger=outlogger
    )                           
    sim.operations.writers.append(table) 

    sim.run(50000)
    sim.operations.integrator.dt = 0.0005
    sim.run(25000)
    sim.operations.integrator.dt = 0.001 
    sim.run(10000) 
    
    #### MINIMIZATION DONE ########
    
    temp = job.sp.temperature * u.K
    kT = temp.to_equivalent("kJ/mol", "thermal").value
    sim.state.thermalize_particle_momenta(filter=filter_, kT=kT)
    langevin = hoomd.md.methods.Langevin(
        filter=filter_, 
        kT=kT, 
        default_gamma=1
    )
    sim.operations.integrator.methods = [langevin]
    sim.run(10000) 
    
    
    ##### Equilibration at full temperature #######
    mttk = hoomd.md.methods.thermostats.MTTK(kT, tau=1)
    nvt = hoomd.md.methods.ConstantVolume(filter_, mttk)
    # add in thermo logger
    sim.operations.integrator.methods = [nvt]
    gsd_writer = hoomd.write.GSD(
        filename=job.fn('trajectory-nvt.gsd'),
        trigger=hoomd.trigger.Periodic(5000),
        mode='wb'
    )
    thermo_logger = hoomd.logging.Logger(categories=['scalar', 'string'])
    thermo_logger.add(sim, quantities=['timestep', 'tps'])
    thermo_logger.add(thermodynamic_properties, ['kinetic_temperature', "potential_energy"]) 
    gsd_writer.logger = thermo_logger
    sim.operations.writers.append(gsd_writer)
    sim.run(500000)
    hoomd.write.GSD.write(state=sim.state,
      mode='xb',
      filename=save_dir+'production-out.gsd'
    ) 
    outlogger.flush()
    thermo_logger.flush()
    print("Finished 0.5 ns Steps of HOOMD-blue run")
    return sim

    
    
    
