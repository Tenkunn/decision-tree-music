import pandas as pd
import numpy as np
from pprint import pprint

music = pd.read_csv("data/test.csv", delimiter=",")
pprint(music)