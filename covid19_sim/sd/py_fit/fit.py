# import numpy as np

# load dataframe with data to calibrate to
# from data import df
import pandas as pd
df = pd.read_csv('historical.csv')
t = df['time'].to_numpy()



# load the sd model and config the return results
import sys
sys.path.append("..")
from model import model as sdm
config = {
    'return_columns':['Confirmed','Deaths'],
    'return_timestamps':t.tolist()
}


#  OPTIMIZATION MODEL
from symfit import Parameter, Variable, Fit

r0 = Parameter('r0',min=2,max=4)

# specify the parameters
# from read_voc import params
# sd_names = dict( (key.lower().replace(" ","_"),key) for key in params.keys() )
# p = dict(
#         (key,Parameter(key,**params[sd_names[key]]))
#         for key in sd_names.keys()
#     )
    
# for value in p.values():
#     print(type(value))

# sppecify the variables
x = Variable('x')
confirmed = Variable('confirmed')
deaths = Variable('deaths')

# specify the model (functions)
# def sd_sim(**p):
#     # print(p)
#     params = dict((sd_names[key],val) for key,val in p.items())
#     return sdm.run(**config,params=params)
def sd_sim(r0):
    return sdm.run(**config,params={'R0':r0})
func = {
    confirmed: sd_sim(r0)['Confirmed'][x],
    deaths: sd_sim(r0)['Deaths'][x]
}

# specify the data for the veriables
xdata = t
ydata = {
    'confirmed': df['confirmed'].to_numpy(),
    'deaths': df['deaths'].to_numpy()
}

print('I m about to fit')
# optimize the model
fit = Fit(func, x=xdata, **ydata)
fit_result = fit.execute()


# visualize results
confirmed_fit, deaths_fit = fit.model(x=xdata, **fit_result.params)
import matplotlib.pyplot as plt

plt.plot(xdata, confirmed_fit)
plt.plot(xdata, ydata['confirmed'])
plt.legend()
plt.show()

plt.plot(xdata, deaths_fit)
plt.plot(xdata, ydata['deaths'])
plt.legend()
plt.show()

