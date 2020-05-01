# rewquest data from api and filter (squeeze) them
import requests
raw_data = requests.get('https://api.covid19api.com/country/united-kingdom').json()
def squeeze(point):
    if point['Province']=='':
        return {
            'Confirmed': point['Confirmed'],
            'Deaths': point['Deaths'],
            'Recovered': point['Recovered'],
            'Active': point['Active'],
            'Date': point['Date']
        }
squeezed = [squeeze(point) for point in raw_data]
data = [point for point in squeezed if point]

# converted the fetched data into dataframe
import pandas as pd
df = pd.DataFrame({
    'time' : [i+22 for i in range(len(data))],
    'date' : [point['Date'] for point in data],
    'confirmed' : [point['Confirmed'] for point in data],
    'active' : [point['Active'] for point in data],
    'recovered' : [point['Recovered'] for point in data],
    'deaths' : [point['Deaths'] for point in data]
})

# save the dataframe as .csv
import os
curr_dir = os.getcwd()
parent_dir = os.sep.join(curr_dir.split(os.sep)[:-1])
xls_destination = os.sep.join([parent_dir,'sd','calibration','historical.csv'])
df.to_csv(xls_destination)

# visualize the dataframe
# import matplotlib.pyplot as plt
# plt.plot('time','confirmed',data = df)
# plt.plot('time','active',data = df)
# plt.plot('time','recovered',data = df)
# plt.plot('time','deaths',data = df)
# plt.legend()
# plt.show()



