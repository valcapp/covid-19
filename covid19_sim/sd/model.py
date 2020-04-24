import pysd
import os
import json

dir_name = os.path.dirname(__file__)
mdl_name = next((name for name in os.listdir( dir_name ) if name[-4:]=='.mdl' in name), None)


model = pysd.read_vensim(os.path.join(dir_name,mdl_name))

import numpy as np
config = {
    'return_columns':['TIME','Susceptible','Exposed','Infected','Deaths','Recovered'],
    'return_timestamps':np.arange(0, 300, 2).tolist()
}
default_params = {
    'Behavioral Risk Reduction':0,
    'Potential Isolation Effectiveness':0
}

def sd_run(form):
    params = default_params.copy()
    data = dict((key,param) for key,param in form.items() if key in params.keys())
    new_params = dict((key,float(param)) for key,param in data.items() if param)
    params.update(new_params)
            
    results = model.run(**config,params=params)
    
    selected_time = form.get('selected_time')
    if not selected_time:
        selected_time = 40

    return {
            'params':params,
            'results':results.to_json(),
            'selected_time' : selected_time
    }
