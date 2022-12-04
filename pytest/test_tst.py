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

print(os.getcwd())


def test_1():
	assert 2==2
