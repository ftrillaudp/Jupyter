import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./RESU/coil_energization.dat', delim_whitespace=True, header=None)

names_file = open('./RESU/coil_energization.dat.names')
data.columns = [line.split('res: ')[1].replace('\n', '') for line in names_file.readlines() if 'res:' in line]

plt.plot(data['time'], data['i_component(1)'], label='Racetrack 1')
plt.plot(data['time'], data['i_component(2)'], linestyle="dashed", label='Racetrack 2')
plt.plot(data['time'], data['i_rdp1'], label='Dump Resistor 1')
plt.plot(data['time'], data['i_is1'], label='Source')
plt.legend()
plt.savefig('./Python/ramp1.png')
plt.show()
