import pandas as pd
import matplotlib.pyplot as plt

data_coil = pd.read_csv('./RESU/coil_energization.dat',delim_whitespace=True,header=None)
data_coil_extraction = pd.read_csv('./RESU/coil_extraction.dat',delim_whitespace=True,header=None)

names_file = open('./RESU/coil_extraction.dat.names')
columns = [line.split('res: ')[1].replace('\n','') for line in names_file.readlines() if 'res:' in line]
data_coil.columns = columns
data_coil_extraction.columns = columns

data = pd.concat([data_coil, data_coil_extraction])

data['resistance'] = abs(data['v_component(1)']/data['i_component(1)'])

print (data)

plt.loglog(data['time']*1e3, data['r_component(1)'], label='Resistance from Circuit')
plt.loglog(data['time']*1e3, data['resistance'], label='Computed resistance |v/i|')
plt.xlabel("Time (ms)")
plt.ylabel("Resistance ($\Omega$)")
plt.legend()

plt.savefig('./Python/all_resistance.png')
plt.show()
