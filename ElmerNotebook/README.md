# NOTES!!!

FEM solver: Elmerfem (http://www.elmerfem.org/blog/) <br />
Geometry builder and mesher: salome platform (https://www.salome-platform.org/) <br />
As 2022, tested with Elmerfem 9.0 and Salome 9.9.0 <br />

To make the *.sh files executable: "chmod u+x *.sh" <br />
1- Run the solver without log file: "bash run.sh" or "./run.sh" <br />
2- Run the solver with log file: "bash run.sh logfilename" or "./run.sh logfilename" <br />
3- Run the geometry builder and mesher alone: ./meshGeneration.sh <br />
4- Compile the User Defined Functions (UDF) alone: ./compileUDF.sh <br />
5- Run step 3 and 4 combined: "./main.sh" or "./main.sh logfilename"


# Electromagnetic and thermal model of a superconducting coil connected to an external circuit.

Background: A superconducting coil can experience a sudden loss of its superconducting state and may enter what is referred to as a "quench". A quench is ignited by a local dissipation of energy within the body of the coil followed by a rapid heat dissipation due to the local loss of the superconducting state. This local dissipation may lead to a propagating heat front throughout the coil winding infusing further dissipation. All the magnetic energy stored in the coil is then released within its body. To avoid physical damage (melting), a detection and protection system is required to detect quickly the quench and to act upon it by dumping the coil energy in an external resistor, for instance. The FEM model deals with the electromagnetic and thermal behavior of the coil while the external circuit model deals with the energization and dumping of the coil energy.

The external circuit is made of a DC power source supplying a current to a coil modeled by FEM in parallel with an external resistor. A resistance connecting the power supply to the coil is used to account for the current leads. Two controlled switches "k1" and "k2" are shown in the figure it is required to model the energization of the coil (C1a) and the dumping (C1b). The switching between one part of the circuits C1a and C1b is done by splitting the sif file into coil-energization.sif and coil-extraction.sif. The detection uses the voltage across the coil as a threshold on the activation of the protection system (dump resistor). It is part of the classic detection and protection schemes for superconducting coils.

Verification of the calculation of the magnetic field on the coil:
- Comparison Elmerfem and Onelab (Gmsh/GetDP) assuming a constant current density Je = 1e8 A/m^2
![Comparison Elmerfem and Onelab (Gmsh/GetDP)](Figures/comparison.png)

Electrical circuit for the entire system including the coil, the power supply and the dump resistor:
![Electrical circuit](Figures/quench-circuit.png)

# Testing the electrical circuits with quench model

Here the case study is superbend SB3-5 for the upgrade of the Swiss Light Source SLS2.0. The case study was provided by Ciro Calzolaio of the Magnet sections at the Paul Scherrer Institute (PSI, https://www.psi.ch/en). Two racetrack coils are connected in series on their power supply (PS1) and two circular coils are connected in series to their own power supply (PS2). The coils are within a yoke. Each set of coils has a dumping resistor in parallel (Rdp1 and Rdp2). The circuit is built with the tool elmer-circuitBuilder.py (https://pypi.org/project/elmer-circuitbuilder/).

The problem is divided in two parts:

1. Current ramp up to nominal values (coil-energization.sif). The ramp rate is 1000 A/s and thus some current is
   pushed to the dump resistor as well.
![Electrical circuit](Figures/)

2. Energy extraction via dump resistor in 150 ms.
![Electrical circuit](Figures/)
