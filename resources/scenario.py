from flask import request
from flask_restful import Resource
import pysd
import numpy as np


class Scenario(Resource):
    model = pysd.read_vensim('sd/community corona 8.mdl')
    config = {
        'return_columns':['TIME','Susceptible','Infected','Deaths','Recovered'],
        'return_timestamps':np.arange(0, 300, 2).tolist(),
    }

    def get(self,run_name):
        if request:
            self.config.update(request.json)
        # self.config['params']['Behavioral Risk Reduction']=request.args.get('Behavioral Risk Reduction')
        try:
            return self.model.run(**self.config).to_json(),200
        except:
            return {'message':'failed to run the model'},500