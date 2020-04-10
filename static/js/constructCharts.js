
class InfDthChartClass{
    constructor(){
        this.layout = {
            title: {
                text:'Infected and Death Cases',
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
            },
        };
    }

    updateData(time, infected, deaths){
        const infectedData = {
            x: time,
            y: infected,
            type: 'scatter',
            name: 'Infected'
        };
        const deathsData = {
            x: time,
            y: deaths,
            type: 'scatter',
            name: 'Deaths'
        };
        this.data = [infectedData,deathsData];
        this.plot();
    }

    plot(){
        Plotly.newPlot('infDthChart', this.data, this.layout);
    }
}


class StackChartClass{
    constructor(){
        this.layout = {
            title: {
                text:'Stack Cases',
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
            },
            // width: "80%"
        };
    }

    updateData(time,s,e,i,r,d){
        const sData = {
            x: time,
            y: s,
            name: 'Susceptible',
            stackgroup: 'one',
            line:{color:'RoyalBlue'}
        };
        const eData = {
            x: time,
            y: e,
            name: 'Exposed',
            stackgroup: 'one',
            line:{color:'MediumPurple'}
        };
        const iData = {
            x: time,
            y: i,
            name: 'Infected',
            stackgroup: 'one',
            line:{color:'DarkOrange'}
        };
        const rData = {
            x: time,
            y: r,
            name: 'Recovered',
            stackgroup: 'one',
            line:{color:'ForestGreen'}
        };
        const dData = {
            x: time,
            y: d,
            name: 'Deaths',
            stackgroup: 'one',
            line:{color:'FireBrick'}
        };
        this.data = [sData,eData,iData,rData,dData];
        this.plot();
    }

    plot(){
        Plotly.newPlot('stackChart', this.data, this.layout);
    }
}


class SankChartClass{

    constructor(){
        this.layout = {
            title: "Flow of cases",
            font: {
                size: 10
            }
        };
        this.data = {
            type: "sankey",
            orientation: "h",
            node: {
                pad: 15,
                thickness: 30,
                line: {
                    color: "black",
                    width: 0.5
                    },
                label: ["Total Population", "Susceptible", "Exposed", "Infected", "Recovered", "Deaths"],
                color: ["LightCyan", "RoyalBlue", "MediumPurple", "DarkOrange", "ForestGreen", "FireBrick"]
            },
            link: {
                source: [0,0,0,0,0],
                target: [1,2,3,4,5],
                value: [100000,0,0,0,0]
            }
        };
    }

    updateData(flows){
        this.data.link.value = flows;
        this.plot();
    }

    plot(){
        Plotly.react('sankChart', [this.data], this.layout);
    }

}


var infDthChart = new InfDthChartClass();
var stackChart = new StackChartClass();
var sankChart = new SankChartClass();

 


