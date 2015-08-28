define([
  'jquery',
  'jquery.validate',
  'underscore',
  'validate-patient-form',
  'load-patient-form',
  'submit-patient-form',
  'search',
  'layout'
], function (
  jquery,
  validate,
  _,
  validatePatientForm,
  loadPatientForm,
  submitPatientForm,
  search,
  layout
) {
  function initialize() {
    search.initSearchForm();
    var form = jquery('#patientForm');
    if (form.length) {
      loadPatientForm.load(HEALTH_FACILITY_ID, PATIENT_STATUS)
        .done(function() {
          var originalFormData = submitPatientForm.getFormData(form);
          validatePatientForm.validate(form);
          form.submit(function(e) {
            e.preventDefault();
            originalFormData = submitPatientForm.submit(form, originalFormData) || originalFormData;
          });
        });
    }
    layout.adjustSidebar();
  }

  return {
    initialize: initialize
  };

});
