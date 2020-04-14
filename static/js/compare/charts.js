// console.log(runs['Last Run']);
var data = {};
const colKeys =['Susceptible', 'Exposed', 'Infected','Recovered','Deaths'];

// populate the data obj: first key is the the run name (runName), the following index is the time step. Each of these time steps contains the array of values corresponding to the different variables (colKeys)
for (let runName of runNames){
    run = JSON.parse(runs[runName].run);
    data[runName]=[];
    for(var i=0 ; i<Object.keys(run[colKeys[0]]).length ; i++){
        // console.log(i);
        let tStamp = [];
        for(let colKey of colKeys){
            tStamp.push(Object.values(run[colKey])[i]);
        }
        // console.log(tStamp);
        data[runName].push(tStamp);
    } 
}
// console.log("data: ",data);
// console.log("data['Last Run']: ",data['Last Run']);

// define the pieChartClass
class pieChartClass{
    constructor(runName){
        this.runName = runName;
        this.layout = {
            // title: runName,
            height: 400,
            width: 500,
            margin: {"t": 40, "b":40, "l":40, "r":40},
            showlegend:false,
            annotations: [{
                // font: {
                //     size: 20
                //     },
                showarrow: false,
                text: this.runName,
                x: 0.5,
                y: 0.5
            }],
        };
        this.data = [{
            type: 'pie',
            values: [100000,0,0,0,0],
            labels: colKeys,
            marker: {
                colors: ["RoyalBlue", "MediumPurple", "DarkOrange", "ForestGreen", "FireBrick"]
            },
            textinfo: "label+percent",
            // text: this.runName,
            textposition: 'inside',
            hole: 0.4
        }];
    }

    updateData(tStamp){
        this.data[0].values = tStamp;
        this.plot();
    }

    plot(){
        Plotly.newPlot(this.runName, this.data, this.layout);
    }

}

// declare the dictionary of charts and time selector
var pieCharts={};
var timeSelector = document.querySelector("#timeSelector");
var selectedStep = parseInt(timeSelector.value/2 -1);

// create the time charts
runNames.forEach(runName => {
    pieCharts[runName] = new pieChartClass(runName);
    // console.log(data[runName][selectedStep]);
    // console.log(data[runName][148]);
    pieCharts[runName].updateData(data[runName][selectedStep]);
});

// make sure that pie charts are updated when changing the time input
$(document).ready(function(){
    timeSelector.addEventListener('change', function(event){
        // console.log('This is the selected time stamp: ',event.target.value);
        selectedStep = parseInt(event.target.value/2 -1);
        for(var runName in pieCharts){
            pieCharts[runName].updateData(data[runName][selectedStep]);
        }
    });
});

