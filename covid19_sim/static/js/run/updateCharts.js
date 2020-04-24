var timeSeries = Object.values(run['TIME']);

// const today = new Date();
// const dayParser = (day) => new Date( today.getTime() + parseInt(day)*24000*3600);
// const dateParser = (date) => date.toUTCString().slice(5,16);

var dateSeries = timeSeries.map(dateParser);
// console.log(dateSeries);

var susceptibleSeries = Object.values(run['Susceptible']);
var exposedSeries = Object.values(run['Exposed']);
var infectedSeries = Object.values(run['Infected']);
var recoveredSeries = Object.values(run['Recovered']);
var deathsSeries = Object.values(run['Deaths']);

var timeSelector = document.querySelector("#timeSelector");
var selectedDate = dayParser(timeSelector.value);
// $('#selectedTimeOutput').attr('value',selectedDate);
var selectedStep = stepParser(timeSelector.value);

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


infDthChart.updateData(dateSeries, infectedSeries, deathsSeries);
stackChart.updateData(dateSeries, susceptibleSeries, exposedSeries, infectedSeries, recoveredSeries, deathsSeries);
sankChart.updateData(flows[selectedStep]);

timeSelector.addEventListener('change', function(event){
    // console.log('This is the selected time stamp: ',event.target.value);
    var selectedStep = parseInt(event.target.value/2 -1);
    sankChart.updateData(flows[selectedStep]);
});