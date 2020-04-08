timeSeries = Object.values(run['TIME']);
susceptibleSeries = Object.values(run['Susceptible']);
exposedSeries = Object.values(run['Exposed']);
infectedSeries = Object.values(run['Infected']);
recoveredSeries = Object.values(run['Recovered']);
deathsSeries = Object.values(run['Deaths']);


infDthChart.updateData(timeSeries, infectedSeries, deathsSeries);
stkChart.updateData(timeSeries, susceptibleSeries, exposedSeries, infectedSeries, recoveredSeries, deathsSeries);