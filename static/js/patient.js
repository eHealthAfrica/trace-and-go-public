define([
  'jquery',
  'jquery.validate',
  'underscore',
  'validatePatientForm',
  'layout',
  'alerts',
  'initialize-ajax',
  'load-patient-form'
], function (jquery, validate, _, validatePatientForm, layout, alerts, ajaxInit, loadPatientForm) {

  function getFormData(form) {
    var unindexedArray = form.serializeArray();
    var indexedArray = {};
    jquery.map(unindexedArray, function(n, i){
      indexedArray[n.name] = n.value;
    });
    return indexedArray;
  }

  function isPristine(form) {
    var formData = getFormData(form);
    return _.isEqual(formData, ORIGINAL_FORM_DATA);
  }

  function getRequestType() {
    var here = location.pathname;
    if (here === '/patients/add/') {
      return 'POST';
    } else {
      return 'PATCH';
    }
  }

  function handleInvalidForm(form) {
    alerts.showAlert("Could not save patient. See details below.", 'alert-danger');
  }

  function handlePristineForm(form) {
    alerts.showAlert("Patient data already up to date", 'alert-warning');
  }

  function handleValidForm(form) {
    ajaxInit.initializeAJAX();
    var formData = getFormData(form);
    var requestType = getRequestType();

    if (requestType === 'POST') {
      jquery.ajax({
        url: '/patients/',
        type: "POST",
        data: JSON.stringify(formData),
        contentType: 'application/json',
        dataType: 'json',
        error: alerts.showAJAXFailureAlert,
        success: function () { alerts.showSuccessAlert('added', formData); }
      });
    } else if (requestType === 'PATCH') {
      jquery.ajax({
        url: location.pathname,
        type: "POST",
        data: JSON.stringify(formData),
        contentType: 'application/json',
        dataType: 'json',
        headers: {'X-HTTP-Method-Override': 'PATCH'},
        error: alerts.showAJAXFailureAlert,
        success: function () { alerts.showSuccessAlert('edited', formData); }
      });
    }
  }

  function getOptions() {
    return jquery.ajax({
      url: "/patients/.json",
      dataType: "json",
      type: "OPTIONS",
      success: function (data) {
        return data;
      }
    });
  }

  function loadForm(form) {
    getOptions().done(
      function(options) {
        loadPatientForm.populate(options, HEALTH_FACILITY_ID, PATIENT_STATUS);
        ORIGINAL_FORM_DATA = getFormData(form);
      });
  }

  function submitForm(form) {
    if (!form.valid()) {
      handleInvalidForm(form);
    } else if (isPristine(form)) {
      handlePristineForm(form);
    } else {
      handleValidForm(form);
    }
  }

  function initialize() {
    layout.adjustSidebar();
    var form = jquery('#patientForm');
    if (form.length) {
      loadForm(form);
      validatePatientForm.validate(form);
      form.submit(function(e) {
        e.preventDefault();
        submitForm(form);
      });
    }
  }

  return {
    initialize: initialize
  };

});
