import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./RESU/coil_energization.dat',delim_whitespace=True,header=None)

names_file = open('./RESU/coil_energization.dat.names')
columns = [line.split('res: ')[1].replace('\n','') for line in names_file.readlines() if 'res:' in line]
data.columns = columns

data['resistance 1'] = abs(data['v_component(1)']/data['i_component(1)'])
data['resistance 2'] = abs(data['v_component(2)']/data['i_component(2)'])
data['resistance 3'] = abs(data['v_component(3)']/data['i_component(3)'])
data['resistance 4'] = abs(data['v_component(4)']/data['i_component(4)'])

print (data)

plt.loglog(data['time']*1e3, data['r_component(1)'], label='Resistance 1 from Circuit')
plt.loglog(data['time']*1e3, data['resistance 1'], linestyle='dashed', marker="*", label='Computed resistance 1 |v/i|')
plt.loglog(data['time']*1e3, data['r_component(2)'], label='Resistance 2 from Circuit')
plt.loglog(data['time']*1e3, data['resistance 2'], linestyle='dashed', marker="o", label='Computed resistance 2 |v/i|')
plt.loglog(data['time']*1e3, data['r_component(3)'], label='Resistance 3 from Circuit')
plt.loglog(data['time']*1e3, data['resistance 3'], linestyle='dashed', marker="p", label='Computed resistance 3 |v/i|')
plt.loglog(data['time']*1e3, data['r_component(4)'], label='Resistance 4 from Circuit')
plt.loglog(data['time']*1e3, data['resistance 4'], linestyle='dashed', marker="^", label='Computed resistance 4 |v/i|')
plt.xlabel("Time (ms)")
plt.ylabel("Resistance ($\Omega$)")
plt.legend()

plt.savefig('./Python/resistanceEnergization.png')
plt.show()
