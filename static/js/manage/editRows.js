// when clicking the edit button, hiding the showRow and show the EditRow for the specific run
$(document).ready(function(){
    // hide all editRows at the beginning
    $('.editRow').each(function(){
        $(this).hide();
    });

    $('.editButton').each(function(){
        $(this).click(function(){
            var runId = $(this).attr('id').slice(0,-10);
            rowToggle(runId);
        });
    });

    $('.escButton').each(function(){
        $(this).click(function(){
            var runId = $(this).attr('id').slice(0,-9);
            rowToggle(runId);
        });
    });
});

function rowToggle(runId){
    $("#"+runId+"showRow").toggle();
    $("#"+runId+"editRow").toggle();
}