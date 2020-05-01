# import os

# raw = open("calibration/Calibration.out", "r").read()
# delimiter = ':MCCOOLING=1000'
# raw = raw[raw.find(delimiter)+len(delimiter):]

lines = open("calibration/Calibration.out", "r").readlines()
lines = [line.strip() for line in lines]

params={}
for line in lines:
    if line[0]!=':':
        terms = line.split('<=')[1].split('=')
        params.update({
            terms[0].strip():float(terms[1].strip())
        })

import json
with open("init_params.json","w+") as f:
    json.dump(params, f)

print(params)