import sys
from elmer_circuitbuilder import *

def main(argv=None):
    output_file = "circuits.definitions_tmp"
    # ---------------------------------------------------------------------------
    c = number_of_circuits(1)
    # ---------------------------------------------------------------------------
    c[1].ref_node = 1
    PS1 = I("IS1", 1, 2, 1.0)
    Rcl1 = R("Rcl1", 2, 3, 1.0)
    FEM_1 = ElmerComponent("Coil1", 3, 1, 1, ["Coil1"])
    # FEM_1 = ElmerComponent("Coil1", 3, 4, number of the Component field in sif == 1 associated to coil 1, ["Coil1"])
    FEM_1.is3D()
    FEM_1.stranded(1, 0)
    FEM_1.isClosed()
    c[1].components.append([PS1, Rcl1, FEM_1])
    # ---------------------------------------------------------------------------
    generate_elmer_circuits(c, output_file)
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
