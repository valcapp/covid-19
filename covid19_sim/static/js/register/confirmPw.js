$(document).ready(function(){
    $('#confirmPassword').on('keyup', function () {
        if ($('#userPassword').val() == $(this).val()) {
            $('#confirmPwMessage').html('Passwords match').css('color', 'green');
            $('#registerButton').removeAttr("disabled");
        } else {
            $('#confirmPwMessage').html('Passwords do not match').css('color', 'red');
            $('#registerButton').prop('disabled', true);
        }
    });
});
