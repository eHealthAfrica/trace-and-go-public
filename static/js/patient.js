define(['jquery', 'jquery.validate', 'validatePatientForm'], function (jquery, validate, validatePatientForm) {

  function submit (form) {

    function getFormData(form) {
      var unindexed_array = form.serializeArray();
      var indexed_array = {};
      $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
      });
      return indexed_array;
    }

    console.log(getFormData(form));

  }

  function listenForSubmit () {
    var btn = jquery('#save');
    btn.click(function () {
      var form = jquery('#patientForm');
      submit(form);
    });
  }

  jquery(function () {
    console.log(validatePatientForm);
    validatePatientForm.validate();
    listenForSubmit();
  });

});
