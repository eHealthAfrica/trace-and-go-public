define([
  'jquery',
  'jquery.validate',
  'underscore',
  'alerts',
  'initialize-ajax',
], function (jquery, validate, _, alerts, ajaxInit) {

  function getFormData(form) {
    var unindexedArray = form.serializeArray();
    var indexedArray = {};
    jquery.map(unindexedArray, function(n, i){
      indexedArray[n.name] = n.value;
    });
    return indexedArray;
  }

  function isPristine(form, originalFormData) {
    var formData = getFormData(form);
    return _.isEqual(formData, originalFormData);
  }

  function getRequestType() {
    var here = location.pathname;
    if (here === '/patients/add/') {
      return 'POST';
    } else {
      return 'PATCH';
    }
  }

  function postForm(formData) {
    jquery.ajax({
      url: '/patients/',
      type: "POST",
      data: JSON.stringify(formData),
      contentType: 'application/json',
      dataType: 'json',
      error: alerts.showAJAXFailureAlert,
      success: function () {
        alerts.showSuccessAlert('added', formData);
      }
    });
  }

  function patchForm(formData) {
    jquery.ajax({
      url: location.pathname,
      type: "POST",
      data: JSON.stringify(formData),
      contentType: 'application/json',
      dataType: 'json',
      headers: {'X-HTTP-Method-Override': 'PATCH'},
      error: alerts.showAJAXFailureAlert,
      success: function () {
        alerts.showSuccessAlert('edited', formData);
      }
    });
  }

  function handleInvalidForm(form) {
    alerts.showAlert("Could not save patient. See details below.", 'alert-danger');
    return false;
  }

  function handlePristineForm(form) {
    alerts.showAlert("Patient data already up to date", 'alert-warning');
    return false;
  }

  function handleValidForm(form) {
    ajaxInit.initializeAJAX();
    var formData = getFormData(form);
    var requestType = getRequestType();
    if (requestType === 'POST') {
      postForm(formData);
      form[0].reset();
    } else if (requestType === 'PATCH') {
      patchForm(formData);
    }
    return formData;
  }

  function submitPatientForm(form, originalFormData) {
    if (!form.valid()) {
      return handleInvalidForm(form);
    } else if (isPristine(form, originalFormData)) {
      return handlePristineForm(form);
    } else {
      return handleValidForm(form);
    }
  }

  return {
    getFormData: getFormData,
    submit: submitPatientForm
  };

});
