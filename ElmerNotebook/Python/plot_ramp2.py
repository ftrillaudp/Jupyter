import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./RESU/coil_energization.dat',delim_whitespace=True,header=None)

names_file = open('./RESU/coil_energization.dat.names')
data.columns = [line.split('res: ')[1].replace('\n','') for line in names_file.readlines() if 'res:' in line]

print (data)
plt.plot(data['time'], data['i_component(3)'], label='Coil 3')
plt.plot(data['time'], data['i_component(4)'], linestyle="dashed", label='Coil 4')
plt.plot(data['time'], data['i_rdp2'], label='Dump Resistor 2')
plt.plot(data['time'], data['i_is2'], label='Source')
plt.legend()
plt.savefig('./Python/ramp2.png')
plt.show()
