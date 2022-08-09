import os
from tqdm import tqdm

os.system('rm ./Log/elmer-*.log')
cmd_elmer = 'ElmerSolver case.sif'
for i in tqdm(range(100), desc = 'ElmerSolver:'):
    pass
    os.system(cmd_elmer+' > ./Log/elmer-$(date +%s).log')
