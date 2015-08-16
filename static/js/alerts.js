define([
  'jquery'
], function(jquery) {

  function getPatientName(formData) {
    return formData.first_name + " " + formData.last_name;
  }

  function getSuccessMessage(verb, formData) {
    var patientName = getPatientName(formData);
    return ("Successfully "
            +verb
            +" patient "
            +"\""
            +patientName
            +"\"");
  }

  function showAlert(message, alertClass) {
    var elm = jquery("<div class='alert "+alertClass+"'>"+message+"</div>");
    jquery('#alerts').html('');
    jquery('#alerts').append(elm);
    return elm;
  }

  function showSuccessAlert(verb, formData) {
    var message = getSuccessMessage(verb, formData);
    var elm = showAlert(message, 'alert-success');
    elm.animate({opacity: 0},
                {duration: 3000,
                 complete: function () { location.href = '/patients/'; }
                });
  }

  function showAJAXFailureAlert () {
    showAlert("Could not connect to database, please try again later.", 'alert-danger');
  }
  
  return {
    showAlert: showAlert,
    showAJAXFailureAlert: showAJAXFailureAlert,
    showSuccessAlert: showSuccessAlert
  };

});
