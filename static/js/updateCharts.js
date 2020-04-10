var timeSeries = Object.values(run['TIME']);
var susceptibleSeries = Object.values(run['Susceptible']);
var exposedSeries = Object.values(run['Exposed']);
var infectedSeries = Object.values(run['Infected']);
var recoveredSeries = Object.values(run['Recovered']);
var deathsSeries = Object.values(run['Deaths']);

var flows = [];
for(i=0;i<timeSeries.length;i++){
    flows[i]=[
        susceptibleSeries[i],
        exposedSeries[i],
        infectedSeries[i],
        recoveredSeries[i],
        deathsSeries[i]
    ];
}

var timeSelector = document.querySelector("#timeSelector");
var selectedStep = timeSelector.value;

infDthChart.updateData(timeSeries, infectedSeries, deathsSeries);
stackChart.updateData(timeSeries, susceptibleSeries, exposedSeries, infectedSeries, recoveredSeries, deathsSeries);
sankChart.updateData(flows[selectedStep]);

timeSelector.addEventListener('change', function(event){
    console.log('This is the selected time stamp: ',event.target.value);
    var selectedStep = parseInt(event.target.value/2 -1);
    sankChart.updateData(flows[selectedStep]);
});