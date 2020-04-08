
timeSeries = Object.values(run['TIME']);
susceptibleSeries = Object.values(run['Infected']);
deathsSeries = Object.values(run['Deaths']);

var susceptibleData = {
    x: timeSeries,
    y: susceptibleSeries,
    type: 'scatter',
    name: 'Susceptible'
};

var deathsData = {
    x: timeSeries,
    y: deathsSeries,
    type: 'scatter',
    name: 'Deaths'
};

var layout = {
    title: {
        text:'COVID-19 Cases',
    },
    xaxis: {
        title: {
            text: 'Time [days]'
        },
    },
    yaxis: {
        title: {
            text: 'Cases [people]',
        }
    }
};

var data = [susceptibleData,deathsData];

Plotly.newPlot('myDiv', data, layout);