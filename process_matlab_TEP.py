# What needs to be done:
# 1) Merge each simout and xmv file
# 2) Label the attacks for each time duration

import numpy as np
import pandas as pd

### Setup column names from MATLAB script. First 40 are sensors, last 11 are actuators.
column_names = ['A Feed',
	'D Feed',
	'E Feed',
	'A and C Feed',
	'Recycle Flow',
	'Reactor Feed Rate',
	'Reactor Pressure',
	'Reactor Level',
	'Reactor Temperature',
	'Purge Rate',
	'Product Sep Temp',
	'Product Sep Level',
	'Product Sep Pressure',
	'Product Sep Underflow',
	'Stripper Level',
	'Stripper Pressure',
	'Stripper Underflow',
	'Stripper Temp',
	'Stripper Steam Flow',
	'Compressor Work',
	'Reactor Coolant Temp',
	'Separator Coolant Temp',
	'Comp A to Reactor',
	'Comp B to Reactor',
	'Comp C to Reactor',
	'Comp D to Reactor',
	'Comp E to Reactor',
	'Comp F to Reactor',
	'Comp A in Purge',
	'Comp B in Purge',
	'Comp C in Purge',
	'Comp D in Purge',
	'Comp E in Purge',
	'Comp F in Purge',
	'Comp G in Purge',
	'Comp H in Purge',
	'Comp D in Product',
	'Comp E in Product',
	'Comp F in Product',
	'Comp G in Product',
	'Comp H in Product',
	'D Feed (MV)',
	'E Feed (MV)',
	'A Feed (MV)',
	'A and C Feed (MV)',
	'Recycle (MV)',
	'Purge (MV)',
	'Separator (MV)',
	'Stripper (MV)',
	'Steam (MV)',
	'Reactor Coolant (MV)',
	'Condenser Coolant (MV)',
	'Agitator (MV)']

# These attacks did not execute properly in the MATLAB simulator and should be skipped
skip_list = [
	'cons_p2s_s4',
	'cons_p2s_s9',
	'cons_p2s_a11',
	'cons_p3s_s4',
	'cons_p3s_s9',
	'cons_p3s_a11',
	'cons_p5s_s4',
	'cons_p5s_s9',
	'cons_p5s_a11',
	'cons_p5s_s3',
	'cons_p5s_s17',
	'line_p3s_s9',
	'line_p5s_s9',
	'line_p5s_a11',
	]

hour = 2000

## Process benign dataset
sim_benign = np.loadtxt('simout_benign.csv', delimiter=',')
xmv_benign = np.loadtxt('xmv_benign.csv', delimiter=',')

Xbenign = np.hstack((sim_benign, xmv_benign))
df = pd.DataFrame(Xbenign, columns = column_names)
df.to_csv('TEP_train.csv', header=True, index=False)

## Add attack column, since we're done with training set
column_names.append('Atk')

attack_patterns = ['cons', 'csum', 'line']
attack_types = ['p2s', 'm2s', 'p3s', 'p5s']

pid_attack_numbers = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's23', 's25', 's40']
xmv_attack_numbers = ['a1', 'a2', 'a3', 'a4', 'a6', 'a7', 'a8', 'a10', 'a11']

for an in xmv_attack_numbers:
	for ap in attack_patterns:
		for at in attack_types:

			if f'{ap}_{at}_{an}' in skip_list:
				print(f'Skipping invalid attack {ap} {at} {an}!')
				continue

			print(f'Processing {ap} {at} {an}')

			## Process attack
			sim_attack = np.loadtxt(f'simout_{ap}_{at}_{an}.csv', delimiter=',')
			xmv_attack = np.loadtxt(f'xmv_{ap}_{at}_{an}.csv', delimiter=',')

			Yattack = np.zeros((len(sim_attack), 1))
			Yattack[5*hour : 7*hour] = 1

			Xattack = np.hstack((sim_attack, xmv_attack, Yattack))

			df1 = pd.DataFrame(Xattack, columns = column_names)
			df1.to_csv(f'TEP_test_{ap}_{at}_{an}.csv', header=True, index=False)

print('Done')
