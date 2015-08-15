define(['jquery', 'jquery.validate'], function(jquery) {

  var errorMessages = {
    "phone_number": "This doesn't look like a phone number, please try again."
  };

  function validate () {
    jquery.validator.addMethod("phone_number", function (value, element) {
      return this.optional(element) || /^\+?[\d\s]{4,}$/i.test(value);
    }, errorMessages.phone_number);
    jquery('#patientForm').validate({
      rules: {
        first_name: {
          required: true
        },
        last_name: {
          required: true
        },
        contact_phone_number: {
          required: true,
          phone_number: true
        },
        patient_status: {
          required: true
        }
      },
      messages: {
        "patient_status": "Please select one option."
      },
      highlight: function(element) {
        $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
      },
      unhighlight: function(element) {
        $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
      },
      errorElement: 'span',
      errorClass: 'help-block',
      errorPlacement: function(error, element) {
        if (element.attr('type') === 'radio') {
          error.insertBefore("input:first");
        }
        else {
          error.insertAfter(element);
        }
      }

    });
  }

  return {
    validate: validate
  };

});
