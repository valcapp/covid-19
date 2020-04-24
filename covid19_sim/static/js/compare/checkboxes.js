// connect the Select Run checkbox list to charts, to enable the hiding function
$(document).ready(function(){

    //
    $( ".runsListItem input:checkbox" ).each(function(event){
        // runName = $(this).attr('id').slice(0,-"Checkbox".length);
        var targetChart = "#"+$(this).attr('id').slice(0,-"Checkbox".length)+"Chart";
        // targetChart = "#"+runName+"Chart.chartFrame.js-plotly-plot";
        // console.log(targetChart);
        // console.log($(targetChart));

        // initial update of charts in show
        if(this.checked) {
            $(targetChart).show();
        } else {
            $(targetChart).hide();
        }
        
        //dynamic update of charts in show
        $(this).change(function(){
            var targetChart = "#"+$(this).attr('id').slice(0,-"Checkbox".length)+"Chart";
            console.log(targetChart+" css display property was: "+$(targetChart).css("display"));
            console.log("something changed: "+targetChart+" should disappear.");
            $(targetChart).toggle('slow');
            // $(targetChart).css("display","none");
            console.log(targetChart+" css display property is now: "+$(targetChart).css("display"));
            $("label[for='" + $(this).attr('id') + "']").toggleClass("uncheckedLabel");
        });
    });
});