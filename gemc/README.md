# Gibbs Ensemble Monte Carlo simulation for the computation of the R32 refrigerant.


This directory contains a Gibbs Ensemble Monte Carlo (GEMC) `mosdef_cassandra` script
that sets up a simulation from scratch using the MoSDeF tools. It was used for 
demonstration in the CECAM workshop in Germany on 9/28/23.

The file r32.xml contains one of the best performing force fields that resulted from
an [iterative method](https://doi.org/10.1021/acs.jcim.1c00448). The files with
the label `preeq` are pre-equilibrated simulations provided to speed up the
demonstration.
