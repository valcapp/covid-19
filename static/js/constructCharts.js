
class InfDthPlot{
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
            }
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
        Plotly.newPlot('infDth', this.data, this.layout);
    }
}


class StackPlot{
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
            }
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
        Plotly.newPlot('stkChrt', this.data, this.layout);
    }
}


var infDthChart = new InfDthPlot();
var stkChart = new StackPlot();



