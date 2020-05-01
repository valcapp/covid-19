import pysd
import os
import json
import datetime

dir_name = os.path.dirname(__file__)
mdl_name = next((name for name in os.listdir( dir_name ) if name[-4:]=='.mdl' in name), None)

model = pysd.read_vensim(os.path.join(dir_name,mdl_name))

import numpy as np
config = {
    'return_columns':['TIME','Susceptible','Confirmed','Exposed','Infected','Deaths','Recovered'],
    'return_timestamps':np.arange(0, 300, 2).tolist()
}

json_file_path = os.path.join(dir_name,"init_params.json")
with open(json_file_path,"r") as f:
    default_params = json.loads(f.read())

#  some rounding just to be consistent with the page
default_params.update({
    'Behavioral Risk Reduction': round(round( default_params['Behavioral Risk Reduction'] /0.05)*0.05 , 2),
    'Potential Isolation Effectiveness': round( round( default_params['Potential Isolation Effectiveness']/0.05)*0.05 , 2)
})

def sd_run(form):
    params = default_params.copy()
    data = dict((key,param) for key,param in form.items() if key in params.keys())
    new_params = dict((key,float(param)) for key,param in data.items() if param)
    params.update(new_params)
    
    results = model.run(**config,params=params)
    
    selected_time = form.get('selected_time')
    if not selected_time:
        from datetime import date
        d0 = datetime.date(2020, 1, 1)
        today = datetime.date.today()
        selected_time = int((today - d0).days)

    return {
            'params':params,
            'results':results.to_json(),
            'selected_time' : selected_time
    }
