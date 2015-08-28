define(['jquery', 'jquery.validate'], function(jquery) {

  var errorMessages = {
    "phone_number": "This does not look like a phone number."
  };

  function validate (form) {
    jquery.validator.addMethod("phone_number", function (value, element) {
      return this.optional(element) || /^\+?[\d\s]{4,}$/i.test(value);
    }, errorMessages.phone_number);
    form.validate({
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
        },
        patient_id: {
          required: true
        },
        health_facility_id: {
          required: true
        }
      },
      messages: {
        "patient_status": "Please select one option."
      },
      highlight: function(element) {
        jquery(element).closest('.form-group').removeClass('has-success').addClass('has-error');
      },
      unhighlight: function(element) {
        jquery(element).closest('.form-group').removeClass('has-error').addClass('has-success');
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
