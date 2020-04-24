$('#runName').on('keypress', function (event) {
    var regex = new RegExp(/[a-zA-Z0-9]/);
    var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
    // console.log(`Is ${key} allowed? `,regex.test(key));
    if (!regex.test(key)) {
        event.preventDefault();
        return false;
    }
});