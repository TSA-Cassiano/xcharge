#(note to myself) to run: pytest
#                 to run with print statements: pytest -s
import os
import subprocess
import pandas as pd
import numpy as np
import io
import pytest
import sys

##################################

print('working dir', os.getcwd())

def run_job(config_test,log_name):
	lab = []
	for test in config_test:
		label = '_'.join([str(x) for x in test])
		param = ' '.join([str(x) for x in test])
		name  = 'Simulation_'+log_name.split('_')[-1].split('.')[0]+'_'+label+'.txt'
		lab.append(name)
		command = "kmc "+log_name+' '+label+' '+param
		subprocess.run(command, shell=True)
	return [(lab)]
	
simuls = run_job([[1000,10]],"input_test1.py")

txt_files = [i for i in os.listdir('.') if (os.path.isfile(i)) and ('.txt' in i.lower())]
print('txt files',txt_files)	
def test_1():
	assert 2==2
